import os
from pytube import Playlist
import video

def generate_path(path, dirname):
    path = os.path.abspath(path)
    if dirname:
        path = os.path.join(path, dirname)
        if not os.path.exists(path):
            os.mkdir(path)
    return path

def download_playlist(url, dirname = None, path = '.', quality = 3):
    playlist = Playlist(url)
    
    print("="*50)
    print(f"{playlist.title[:50]} ".ljust(50, '='))
    print("="*50)
    
    # Details
    print(f"Total Videos: {playlist.length}")
    if input("Are you sure to download? [Y/n] ").strip().lower() != 'y':
        print("Exiting...")
        return
    print("="*50)

    # Creating the dir
    path = generate_path(path, dirname)
    
    # Starting to download
    total_size = 0
    n = 0
    for i, url in enumerate(playlist.url_generator(), 1):
        print(f"\n[{i}/{playlist.length}]", end=' ')
        filesize = video.download_video(url, path, quality)
        if filesize:
            total_size += filesize
            n += 1
    print("Done")

    # Summary
    print("="*50)
    print(f"Total Size: {total_size/1024**2:.2f} MB")
    print(f"Downloaded videos: {n}")
    print(f"Saved in '{path}'")
    print("="*50)

def main():
    path = "F:\\Videos"
    download_playlist("https://youtube.com/playlist?list=PLhfrWIlLOoKOf1Ru_TFAnubVuWc87i-7z&si=FjFGl5RKdxcaV2AR", path, True)


if __name__ == "__main__":
    main()