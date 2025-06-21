import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

api = YouTubeTranscriptApi()
formatter = TextFormatter()

def get_safe_string(s: str):
    return "".join(c if c.isalnum() or c in " _-" else "_" for c in s).replace(" ", "_")

def get_youtube_transcript(video_id, playlist_id, video_title):
    try:
        # Fetch the transcript
        transcript = api.fetch(video_id, languages=['en', 'de'])

        # Format the transcript into plain text
        formatted_transcript = formatter.format_transcript(transcript)

        safe_playlist_title = get_safe_string(s= playlist_id)
        safe_video_title = get_safe_string(s = video_title)

        # Create the directory for the playlist if it doesn't exist
        playlist_dir = f"transcripts/{safe_playlist_title}_transcripts"
        os.makedirs(playlist_dir, exist_ok=True)

        # Save the transcript to a file inside the new directory
        file_path = os.path.join(playlist_dir, f"{safe_video_title}_transcript.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(formatted_transcript)

        print(f"Transcript saved as {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

