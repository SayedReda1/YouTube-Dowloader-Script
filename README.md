# YouTube Video & Playlist Downloader
This script is designed to download YouTube video and playlist with just one command

### How to use
Open help menu by writing the following command:

    download.exe -h

#### Options
| option             | details                                               |
|--------------------|-------------------------------------------------------|
| *-h --help*        | to show the help menu with all options explained.
| *-v --video [url]* | to download a video with specific url.
| *-p --playlist [url]* | to download an entire playlist with specific url.
| *-o --output [path]* | to specify a path to download the video or playlist in [cwd by default].
| *-d --dir [title]* | to create a folder with specific title and save the output in.

### Examples
To download a video with the highest quality available:

    download.exe -v [url] -q 3

To download a playlist with an average quality to a specific path:

    download.exe -p [url] -q 2 -o [path]
