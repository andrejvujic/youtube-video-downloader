from pytube import YouTube
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import uuid

video_url = "https://www.youtube.com/watch?v=xWOoBJUqlbI"


def get_uuid():
    return str(uuid.uuid4())


def download_video(video_url=""):
    OUTPUT_PATH = "outputs/"
    FILE_NAME = get_uuid()
    try:
        yt = YouTube(video_url)
    except:
        return

    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(output_path=OUTPUT_PATH, filename=FILE_NAME)

    upload_video(file_name=FILE_NAME)


def upload_video(file_name):
    STORAGE_BUCKET = 'yt-dwld.appspot.com'

    credentials = credentials.Certificate('service-account.json')
    firebase_admin.initialize_app(credentials, {
        'storageBucket': STORAGE_BUCKET,
    })


download_video(video_url=video_url)
