from pytube import YouTube
import uuid

video_url = "https://www.youtube.com/watch?v=xWOoBJUqlbI"


def get_uuid():
    return str(uuid.uuid4())


def download_video(video_url=""):
    OUTPUT_PATH = "outputs/"
    FILE_NAME = get_uuid()
    try:
        yt = YouTube(video_url)
        print("video initialized")
    except:
        print("error while initializing")
        return

    print("video downloading")
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(output_path=OUTPUT_PATH, filename=FILE_NAME)
    print("video downloaded")


download_video(video_url=video_url)
