from pytube import Playlist
from main import get_youtube_transcript
from dotenv import load_dotenv

import os

load_dotenv()

PLAYLIST_URL = os.getenv('PLAYLIST_URL')

def get_video_urls(playlist_url: str) -> list:
    print("Extracting URLs")
    playlist_id = Playlist(playlist_url).title
    video_links = Playlist(playlist_url).video_urls
    print(f"URLs extracted: {len(video_links)}")
    return video_links, playlist_id

import yt_dlp

def extract_video_ids(urls: list) -> tuple[list, list]:
    video_ids = []
    video_titles = []
    print("Extracting Video IDs using yt-dlp")

    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                info = ydl.extract_info(url, download=False)
                video_id = info.get("id")
                title = info.get("title")

                if video_id and title:
                    video_ids.append(video_id)
                    video_titles.append(title)
                    print(f"✅ Extracted: {title}")
                else:
                    print(f"⚠️  Skipped (no ID or title): {url}")
            except Exception as e:
                print(f"❌ Skipping video: {url} due to error: {e}")
                continue

    print(f"Extracted {len(video_ids)} valid video IDs.")
    return video_ids, video_titles



if __name__ == "__main__":
    video_urls, playlist_id = get_video_urls(PLAYLIST_URL)
    video_ids, video_titles = extract_video_ids(video_urls)
    for video_id, video_title in zip(video_ids, video_titles):
        get_youtube_transcript(video_id=video_id, playlist_id=playlist_id, video_title = video_title)