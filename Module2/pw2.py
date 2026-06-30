import yt_dlp

def download_dash_stream():
    print("--- MPEG-DASH Video Downloader ---")
    
    # 1. Use the live .mpd link you just found
    mpd_url = "https://sec-prod-mediacdn.pw.live/47df9f99-6347-470c-b969-519312f8d039/master.mpd?URLPrefix=aHR0cHM6Ly9zZWMtcHJvZC1tZWRpYWNkbi5wdy5saXZlLzQ3ZGY5Zjk5LTYzNDctNDcwYy1iOTY5LTUxOTMxMmY4ZDAzOQ&Expires=1782500792&KeyName=pw-prod-key&Signature=ROtRD1PjtYHrV62x4WQrJl053U5Tq8ALz_bJf8wDPZ_HSdmc6KsSd4DPMemvBsjFFh7bydW2avwblCwrhNhKCQ"
    # 2. Grab your fresh Bearer token from the TOKEN_CONTEXT cookie
    token = input("Paste your Authorization Token (Bearer ey...): ").strip()
    
    ydl_opts = {
        'outtmpl': 'downloaded_lecture.%(ext)s',
        'http_headers': {
            'Authorization': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        },
        # Combine best video and best audio into a single output container
        'format': 'bestvideo+bestaudio/best',
    }
    
    print("\nInitializing download via DASH Manifest parser...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([mpd_url])

if __name__ == "__main__":
    download_dash_stream()