import os
import re
import urllib.parse
import requests
from Crypto.Cipher import AES

def download_hls_video():
    print("--- Generalized HLS Decryption Downloader ---")
    
    m3u8_url = input("Paste your complete, live .m3u8 URL (with all query parameters): ").strip()
    auth_token = input("Paste your Authorization Token (e.g., 'Bearer ey...'): ").strip()
    
    if not m3u8_url:
        print("A valid URL is required.")
        return

    # Extract query parameters (?URLPrefix=...&Expires=...) to append to segments later
    parsed_url = urllib.parse.urlparse(m3u8_url)
    url_query = parsed_url.query
    
    # 1. Manifest Header (Requires Authorization)
    manifest_headers = {
        "Authorization": auth_token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # 2. CDN Segment Header (Must NOT include Authorization, otherwise CDN throws 400/403)
    cdn_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print("\nFetching playlist manifest...")
    response = requests.get(m3u8_url, headers=manifest_headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch manifest. Status: {response.status_code}")
        return
        
    lines = response.text.splitlines()
    
    key_uri = None
    key_bytes = None
    segments = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("#EXT-X-KEY"):
            uri_match = re.search(r'URI="([^"\s]+)"', line)
            if uri_match:
                key_uri = uri_match.group(1)
                key_uri = urllib.parse.urljoin(m3u8_url, key_uri)
        elif line and not line.startswith("#"):
            # Resolve the relative path base
            base_segment_url = urllib.parse.urljoin(m3u8_url, line)
            
            # Re-attach the CDN signature parameters to the individual segment string
            if url_query and "?" not in line:
                segment_url = f"{base_segment_url}?{url_query}"
            else:
                segment_url = base_segment_url
                
            segments.append(segment_url)
            
    print(f"Found {len(segments)} segments to process.")
    
    if key_uri:
        print("Fetching decryption key...")
        # Key needs the bearer token authorization
        key_resp = requests.get(key_uri, headers=manifest_headers)
        if key_resp.status_code == 200:
            key_bytes = key_resp.content
            print("Successfully retrieved decryption key.")
        else:
            print(f"Error retrieving key (Status {key_resp.status_code}). Decryption will fail.")
            return

    output_filename = "output_video.ts"
    print(f"Streaming segments to '{output_filename}'...")
    
    with open(output_filename, "wb") as outfile:
        for idx, seg_url in enumerate(segments):
            print(f"Processing chunk {idx + 1}/{len(segments)}...", end="\r")
            
            # Download segment using clean CDN headers + appended query signature
            seg_resp = requests.get(seg_url, headers=cdn_headers)
            if seg_resp.status_code != 200:
                print(f"\nError downloading segment {idx + 1}: Status {seg_resp.status_code}")
                continue
                
            data = seg_resp.content
            
            if key_bytes:
                iv = idx.to_bytes(16, byteorder='big')
                cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
                data = cipher.decrypt(data)
                
                pad_len = data[-1]
                if pad_len < 16 and all(x == pad_len for x in data[-pad_len:]):
                    data = data[:-pad_len]
                    
            outfile.write(data)
            
    print(f"\nFinished! Output saved as '{output_filename}'")

if __name__ == "__main__":
    download_hls_video()