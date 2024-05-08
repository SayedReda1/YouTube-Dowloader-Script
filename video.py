import os
from pytube import YouTube, request
from tqdm import tqdm
import time

def download_video(url, output_path):
    # Changing to update progressbar after each 100 KB
    request.default_range_size = 3 * 1024 * 1024

    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    
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
    except Exception as e:
        print("Error:", str(e))
    finally:
        progress_bar.close()

def main():
    url = input("Enter YouTube video URL: ")
    output_path = input("Enter the path to save the video: ")
    
    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)
    
    download_video(url, output_path)

if __name__ == "__main__":
    main()
