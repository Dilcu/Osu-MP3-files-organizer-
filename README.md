<h1>ABOUT THE PROJECT</h1>
<p>This <b>Python</b> program that I've created was to initially scrape the .mp3 files from the songs folder of the rhythm game that I'm always playing, which is Osu!</p>

![image](https://github.com/user-attachments/assets/f64e5745-1004-4ee8-9292-7ec60b5a0084)

<p>I'm always fond of the songs or as the game calls it "Beatmaps" since the genre of the music those beatmaps use is the type of genre that I listen to on different common music streaming platforms.</p>
<p>That is why instead of manually searching on the internet on what music those beatmaps used and manually downloading those music from the internet, I've create a program that could directly find the music that the beatmap is using (usually the .mp3 files), then copy those files from a specific folder that I want those music to be on, either creating dedicated folders for certain genres or just a folder to store those music.</p>


<h2>Features:</h2>

* Scans a given directory (recursively) for `.mp3` files
* Filters out short files since some beatmaps are just short (less than 59 seconds)
* Copies the valid `.mp3` files to a destination folder
<br>
<p>But since the structure of this program is not specifically design for Osu! use only, this program could also be used on any file directories. You could copy certain .mp3 files from a designated file path, making sure that the duration checker is adjust to preference, then paste it to what ever directory you wanted those files to be on depening on your preference.</p>

<br>
<br>
<hr>

**<h1>⚙️ HOW TO USE</h1>**
1. Clone the repo or download the script.

2. Set the paths in the script:
   - song_dir = 'C:\\Path\\To\\osu!\\Songs'         # Your Osu! beatmaps folder
   - destination = 'C:\\Path\\To\\Music\\Playlist'  # Where you want the MP3s to go

3. _Run the script_
    - either using bash:
      python mp3_organizer.py

    - or on the actual VS code IDE:

![image](https://github.com/user-attachments/assets/23567131-7973-4129-baa8-51ed9688bbde)

4. Done! All valid .mp3 files will be copied to your destination folder.

<em>Take not that this program is only cloning or copying the file/s from the intial path (in this case from the Osu! beatmaps folder) to the destination path. The script is not moving the files from the initial to the desitnation path.</em>
