import os
import argparse
import validators
import video, playlist

# URL
# Video or playlist
# quality
# path
def get_args():
    parser = argparse.ArgumentParser(description="This script downloads youtube videos and playlists with given quality and output path")
    parser.add_argument("-v", "--video", type=str, help="Enter YouTube video URL")
    parser.add_argument("-p", "--playlist", type=str, help="Enter YouTube playlist URL")
    parser.add_argument("-o", "--output", default=".", type=str, help="Enter the path to save the video - current dir is default path")
    parser.add_argument("-d", "--dir", default=None, type=str, help="Enter a directory name to create and save the downloaded video/playlist")
    parser.add_argument("-q", "--quality", default=3, type=int, help="Enter required quality as 1:3 - 3 highest quality and 1 is lowest quality -> 3 is default")
    return parser.parse_args()

def is_url(url_string: str) -> bool:
    result = validators.url(url_string)
    if isinstance(result, validators.ValidationError):
        return False
    
    return result


def main():
    # getting args
    args = get_args()
    path = os.path.abspath(args.output.strip())

    # Cannot provide video and playlist urls
    if args.video and args.playlist:
        print("Error: you can only specify a video or a playlist")
        return
    # Cannot provide none of the urls
    if not args.video and not args.playlist: 
        print("Error: you must specify a video or a playlist")
        return

    # validating output path
    if not os.path.exists(path):
        print(f"Error: {path} does not exist")
        return

    # Validating quality
    if args.quality < 1 or args.quality > 3:
        print(f"Error: {args.quality} is not a valid quality")
        return

    # Creating directory
    if args.dir:
        try:
            path = os.path.join(path, args.dir.strip())
            if not os.path.exists(path):
                os.mkdir(path)
        except Exception as e:
            print("Error:", str(e))
            return

    # Starting to download
    if args.video:
        # validate video url
        if (is_url(args.video.strip())):
            video.download_video(args.video.strip(), path, args.quality)
        else:
            print("Entered video url is invalid")

    else:
        # validate video url
        if (is_url(args.playlist.strip())):
            playlist.download_playlist(args.playlist.strip(), path, args.quality)
        else:
            print("Entered playlist url is invalid")


if __name__ == "__main__":
    main()