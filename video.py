import os
from pytube import YouTube, request
from tqdm import tqdm
import time

def fetch_stream(youtube: YouTube, quality):
    streams = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')

    if len(streams) == 0:
        return

    stream = None
    if quality == 1:
        stream = streams.get_lowest_resolution()
    elif quality == 3:
        stream = streams.get_highest_resolution()
    else:
        stream = streams[len(streams)//2]
    
    return stream
        

def download_video(url, output_path, quality):
    # Changing to update progressbar after each 100 KB
    request.default_range_size = 3 * 1024 * 1024
    
    yt = YouTube(url)
    video = fetch_stream(yt, quality)

    # There was no stream
    if not video:
        print(f"Error: Couldn't find a suitable stream for '{yt.title}'")
        return

    # Printing before the progressbar appears
    print(f"Downloading '{video.title}'")
    
    total_size = video.filesize
    bytes_downloaded = 0
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, ncols=100)
    
    def update_progress(stream, chunk, remaining):
        nonlocal bytes_downloaded
        bytes_downloaded += len(chunk)
        progress_bar.update(len(chunk))

    yt.register_on_progress_callback(update_progress)
        
    try:
        video.download(output_path=output_path)
        return total_size
    except Exception as e:
        print("Error:", str(e))
    finally:
        progress_bar.close()

def main():
    download_video('https://youtu.be/Iygg5gsOZ80?si=Zb8a7ZS7wt75wC_B', 'F:\\Videos', 3)

if __name__ == "__main__":
    main()
