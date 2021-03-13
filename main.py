from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=xWOoBJUqlbI"


def download_video(video_url=""):
    OUTPUT_PATH = "outputs/"

    try:
        yt = YouTube(video_url)
    except:
        return

    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(output_path=OUTPUT_PATH)


download_video(video_url=video_url)
