from flask import Flask
from routes.videos import bp as videos_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(videos_bp, url_prefix='/api/videos')
# c
if __name__ == '__main__':
    app.run(debug=True) 