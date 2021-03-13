from pytube import YouTube
from flask import Flask, request, send_file
import uuid


def get_uuid():
    return str(uuid.uuid4())


app = Flask(__name__)


@app.route('/')
def root():
    return "goto to /download to download your first video"


@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get('video_url', default="")
    FILE_NAME = get_uuid()

    try:
        yt = YouTube(video_url)
        print("video initialized")
    except:
        print("error while initializing")
        return

    print("video downloading")
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(output_path="downloads/", filename=FILE_NAME)
    print("video downloaded")
    return send_file(f"downloads/{FILE_NAME}.mp4", as_attachment=True)
