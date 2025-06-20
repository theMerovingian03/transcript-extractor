from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

api = YouTubeTranscriptApi()

def get_youtube_transcript(video_id):
    try:
        # Fetch the transcript
        transcript = api.fetch(video_id, languages=['en', 'de'])
        # Format the transcript into plain text
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        # Save the transcript to a file
        with open(f"transcripts/{video_id}_transcript.txt", "w", encoding="utf-8") as file:
            file.write(formatted_transcript)
        
        print(f"Transcript saved as {video_id}_transcript.txt")
    except Exception as e:
        print(f"An error occurred: {e}")