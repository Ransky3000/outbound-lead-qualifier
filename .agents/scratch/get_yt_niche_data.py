import os
import sys
import json
import cv2
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi

def download_transcript(video_id, output_path):
    print(f"Downloading transcript for {video_id}...")
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        try:
            transcript = transcript_list.find_transcript(['en', 'fil', 'tl'])
        except Exception:
            transcript = next(iter(transcript_list))
            
        data = transcript.fetch()
        lines = []
        for x in data:
            start_sec = x.start
            minutes = int(start_sec // 60)
            seconds = int(start_sec % 60)
            lines.append(f"[{minutes:02d}:{seconds:02d}] {x.text}")
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Transcript saved to {output_path}. Total lines: {len(lines)}")
    except Exception as e:
        print(f"Error downloading transcript: {e}")

def download_video(video_id, output_filename):
    print(f"Downloading video {video_id} in low quality...")
    try:
        ydl_opts = {
            'format': 'worst',  # Get lowest resolution
            'outtmpl': output_filename,
            'extractor_args': {'youtube': {'player_client': ['android']}},
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://youtu.be/{video_id}"])
        print("Video download complete!")
        return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False

def extract_frames(video_path, output_dir, interval_seconds=30):
    print(f"Extracting frames from {video_path} to {output_dir} every {interval_seconds} seconds...")
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            print("Error: FPS is 0 or could not read video properties.")
            return
            
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration_seconds = frame_count / fps
        print(f"FPS: {fps}, Total frames: {frame_count}, Duration: {duration_seconds:.2f} seconds")
        
        interval_frames = int(fps * interval_seconds)
        count = 0
        saved_count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            if count % interval_frames == 0:
                current_sec = count / fps
                minutes = int(current_sec // 60)
                seconds = int(current_sec % 60)
                filename = os.path.join(output_dir, f"frame_{minutes:02d}_{seconds:02d}.jpg")
                cv2.imwrite(filename, frame)
                saved_count += 1
                
            count += 1
            
        cap.release()
        print(f"Extracted {saved_count} frames successfully!")
    except Exception as e:
        print(f"Error extracting frames: {e}")

if __name__ == "__main__":
    video_id = "Y3PcRp5RFzk"
    transcript_path = r"C:\Users\USER\Desktop\Ranian's file\Mission Control\The niche\transcript_raw.txt"
    video_path = "video_low_niche.mp4"
    screenshots_dir = r"C:\Users\USER\Desktop\Ranian's file\Mission Control\The niche\screenshots"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(transcript_path), exist_ok=True)
    
    download_transcript(video_id, transcript_path)
    if download_video(video_id, video_path):
        extract_frames(video_path, screenshots_dir, interval_seconds=30)
        if os.path.exists(video_path):
            os.remove(video_path)
            print("Temporary video file removed.")
