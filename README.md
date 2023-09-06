# YouTube Video Downloader
This script downloads videos from YouTube. It takes a list of links to videos as input and downloads the highest resolution video in MP4 format to the specified download destination.

## Usage
To use the script, you will need to install the following Python libraries:

`pytube`
`colored`

Once you have installed the required libraries, you can run the script by passing the path to the file containing the list of YouTube links as the first argument and the download destination as the second argument. For example, to download the videos in the links.txt file to the Downloads folder, you would run the following command:

`python youtube_downloader.py links.txt Downloads`
### Example
The following is an example of a links.txt file:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=ub82Xr2h2UM
```

If you run the script with this file as input, it will download the two videos to the Downloads folder.

### Notes

* The script only downloads videos in MP4 format.
* The script does not check if the videos are available in MP4 format. If the video is not available in MP4 format, the script will not download it.
* The script does not handle errors gracefully. If there is an error downloading a video, the script will simply skip that video.
