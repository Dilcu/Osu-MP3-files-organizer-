import os
import fnmatch
import shutil
import mutagen 
from mutagen.mp3 import MP3 

song_dir = 'C:\\Users\\Euclid\\Desktop\\songs - onthespot\\temp' # your directory path
destination = 'C:\\Users\\Euclid\\Desktop\\songs - onthespot\\Arcane - OST' # desired directory to move files (CHANGE WHEN NEEDED)


#AUDIO LENGTH CALCULATOR
def audio_duration(length): 
    hours = length // 3600  # calculate in hours 
    length %= 3600
    mins = length // 60  # calculate in minutes 
    length %= 60
    seconds = length  # calculate in seconds 
  
    return hours, mins, seconds  # returns the duration

#AUDIO DURATION CHECKER
def audio_checker(path):
    try:
        audio = MP3(path)
        audio_info = audio.info
        length = int(audio_info.length)
        hours, mins, seconds = audio_duration(length)

        if hours == 0 and mins == 0 and seconds < 59:
            print(f"AUDIO TOO SHORT! Skipping: {path}")
            return None
        else:
            return path
    except mutagen.MutagenError as e:
        print(f"Error reading audio file: {path}. Skipping file. Error: {e}")
        return None 

#DIRECTORY HANDLING
def dir_manip(song_directory):
    for path, dirs, files in os.walk(song_directory):
        for file in files:
            if fnmatch.fnmatch(file, '*.mp3'):
                fullpath = os.path.join(path, file)
                newpath = audio_checker(fullpath)
                if newpath:
                    shutil.copy(newpath, destination)
                    print(f"Copied: {newpath}")


            #shutil.copy(fullpath,destination)
            #print(fullpath)
            #print(fullpath + " " + 'Total Duration: {}:{}:{}'.format(hours, mins, seconds))
            
dir_manip(song_dir)

            

