import os
from pytubefix import Playlist

# Initialize counter for downloaded files
filesDownloaded = 0

# Read and store user input
url = input("Enter the URL of the playlist you want to download: ")

# Get the video 
try:
    pl = Playlist(url) 
except:
    print("Error: Invalid URL. Please enter a valid YouTube playlist URL.")
    exit()

# Get the number of videos in the playlist
length = pl.length

# Create a folder to store the audio files
os.makedirs(pl.title, exist_ok=True)

# Change the current working directory to the folder
os.chdir(pl.title)

print(f"Downloading {pl.title}...")

# Loop through the videos in the playlist and download the audio files
for video in pl.videos:
    try:    
        # Filter the video streams for getting just the audio file
        stream = video.streams.get_audio_only()

        # Download the audio file
        filename = stream.download(mp3=True)

        if os.path.exists(filename):
            filesDownloaded += 1
    except Exception as e:
        print(f"Error downloading {video.title}: {e}")

print(f"Downloaded {filesDownloaded} files out of {length} files.")
print("Download complete!")