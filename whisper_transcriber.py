import whisper

model = whisper.load_model("base")

def transcribe(video_url):
    # Download video or stream
    result = model.transcribe(video_url)
    return result['text'] 