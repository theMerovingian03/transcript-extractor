from pytube import Playlist, extract
from main import get_youtube_transcript

def get_video_urls(playlist_url: str) -> list:
    video_links = Playlist(playlist_url).video_urls
    return video_links

def extract_video_ids(urls: list) -> list:
    video_ids = []
    for url in urls:
        id = extract.video_id(url=url)
        video_ids.append(id)
    return video_ids

if __name__ == "__main__":
    video_urls = get_video_urls('<your_playlist_url>')
    video_ids = extract_video_ids(video_urls)
    for video_id in video_ids:
        get_youtube_transcript(video_id=video_id)