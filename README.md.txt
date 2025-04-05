# 🎧 MP3 File Organizer & Filter for Osu! Beatmaps

This is a simple Python script I created to extract `.mp3` files from my Osu! beatmaps folder 
so I can use them in my personal music playlist. It filters out audio files that are shorter than 59 seconds (like hitsounds or intros) 
to keep the playlist clean and full-length.

Although it was built with Osu! in mind, this tool works with any directory of `.mp3` files, making it useful for general-purpose audio filtering and organizing.

## 🎯 What It Does

- Scans a given directory (recursively) for `.mp3` files
- Filters out short files (less than 59 seconds)
- Copies the valid `.mp3` files to a destination folder
- Useful for:
  - Extracting songs from Osu! beatmaps
  - Cleaning music folders
  - Creating custom playlists

## 📦 Requirements

- Python 3.x
- [`mutagen`](https://mutagen.readthedocs.io/en/latest/) (for reading audio metadata)

Install dependencies using:

```bash
pip install -r requirements.txt
