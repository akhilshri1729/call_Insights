from blob_utils import upload_file, upload_text
from speech_to_text import transcribe_audio
from openai_utils import get_insights

audio_files = ["data/call_recording_01.wav"]

for file in audio_files:
    print(f"\n🎧 Processing: {file}")

    # Upload audio
    upload_file(file)

    # Transcribe
    transcript = transcribe_audio(file)

    # Store transcript
    upload_text(transcript, f"transcripts/{file}.txt")

    # Get insights
    insights = get_insights(transcript)

    # Store insights
    upload_text(insights, f"insights/{file}.txt")

    print("✅ Done")
