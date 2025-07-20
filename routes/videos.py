from flask import Blueprint, request, jsonify
from models import videos
from cloudinary_client import upload_video
from whisper_transcriber import transcribe
from translator import translate
import tempfile
from bson import ObjectId

bp = Blueprint('videos', __name__)

@bp.route('/upload', methods=['POST'])
def upload():
    try:
        from models import videos
        if videos is None:
            return jsonify({'error': 'MongoDB is not connected. Check your MONGO_URI and server.'}), 500
        file = request.files['video']
        # Validate file extension
        if not file.filename.lower().endswith('.mp4'):
            return jsonify({'error': 'Only .mp4 files are allowed'}), 400
        temp = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        file.save(temp.name)
        # Transcribe using the local file path before uploading
        text = transcribe(temp.name)
        url = upload_video(temp.name)
        local_text = translate(text)
        doc = {
            'video_url': url,
            'transcript_en': text,
            'transcript_local': local_text,
        }
        vid_id = videos.insert_one(doc).inserted_id
        return jsonify({'id': str(vid_id)})
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@bp.route('/', methods=['GET'])
def list_videos():
    docs = videos.find()
    out = []
    for d in docs:
        out.append({'id': str(d['_id']), 'video_url': d['video_url']})
    return jsonify(out)

@bp.route('/<id>', methods=['GET'])
def get_video(id):
    d = videos.find_one({'_id': ObjectId(id)})
    if not d:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({
        'video_url': d['video_url'],
        'captions': d['transcript_local'],
    }) 