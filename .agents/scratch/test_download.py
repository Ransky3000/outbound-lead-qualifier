import yt_dlp

def test():
    # Try different client configurations
    opts_list = [
        {
            # Option 1: Standard web client fallback
            'format': 'worst',
            'outtmpl': 'test_video.mp4',
            'extractor_args': {'youtube': {'player_client': ['web']}},
        },
        {
            # Option 2: Android client fallback
            'format': 'worst',
            'outtmpl': 'test_video.mp4',
            'extractor_args': {'youtube': {'player_client': ['android']}},
        },
        {
            # Option 3: iOS client fallback
            'format': 'worst',
            'outtmpl': 'test_video.mp4',
            'extractor_args': {'youtube': {'player_client': ['ios']}},
        }
    ]
    
    for i, opts in enumerate(opts_list, 1):
        print(f"Testing Option {i}...")
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download(["https://youtu.be/Q46OLxFshAQ"])
            print(f"Option {i} succeeded!")
            return True
        except Exception as e:
            print(f"Option {i} failed: {e}")
            
    return False

if __name__ == "__main__":
    test()
