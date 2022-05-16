# PyPlayer

## Introduction

Thank you for using PyPlayer to download and play audio.

- PyPlayer is a yt-dlp powered python program capable of downloading youtube URLs to mp3 and wav formats.

- PyPlayer is also a pygame powered python audio player capable of playing 8 simultaneous sounds from your local files and independently controlling their volumes.

-PyPlayer can also stream a single youtube audio at a time from a URL without saving the file in your computer.

## How to Use

When launched, PyPlayer will offer a menu with various options:

### 1. Download Youtube audio

PyPlayer will ask for a Youtube URL and will check if it's valid. If it is, it will ask for an audio codec between 'mp3' or 'wav'. Finally it will ask for a file name to save the audio as. If left blank, the default youtube video title will be used. ALL AUDIO FILES ARE DOWNLOADED TO THE AUDIO FOLDER.

### 2. Play stored audio file

PyPlayer will ask for a file name and will search the audio folder for audio files with mp3 or wav extension that contain that file name. Upon finding one, it will ask to confirm the selection to make sure it's the right one. If the user confirms the selection, the audio will start playing. If the user doesn't confirm the selection, PyPlayer will keep searching for more files that contain that file name until all files in the audio folder have been searched, repeating the confirmation process upon finding new files.

All Audio files start playing at 50% volume.

Up to 8 audio files (they can be instances of the same audio file) can be initialized and play simultaneously.

### 3. Stream Youtube audio

PyPlayer will ask for youtube video details the same way as in '1. Download Youtube audio'. It will then download the audio file and play it. When a key is pressed, playback will stop and the file will be deleted, leaving no trash files behind.

As of this PyPlayer version, Stream Youtube audio will play a sound on top of what was already playing, but the audio stream has to be finished before going back to the menu again.

### 4. Change Channel volume

PyPlayer will list all active audio channels and the name of the file they're playing. Upon choosing a channel by typing the channel number, a prompt to configure the volume percentage of the channel will appear. Only the volume of the selected channel will be changed, the rest will remain the same.

### 5. Stop Channel
PyPlayer will list all active audio channels and the name the file they're playing. Upon choosing a channel by typing the channel number, the selected channel will stop playing its audio and its volume will be reset to 50%

### 6. Stop All
PyPlayer will stop all audio channels and reset their volume to 50%.

### 7. Exit
Exits the program

## Supported Formats
mp3 and wav are the only two codecs supported.

- wav is heavy and uncompressed, at around 10MB/minute. The program can run these files directly so all commands related to wav files are instantaneous. It is recommended to use Wav if possible for all files that will be stored locally in the audio folder for local playing afterwards.

- mp3 is considerably ligther than wav and compressed. The program has to process these files before playing them, and encode them when downloading them, meaning that it will take some time when downloading a file in mp3 format or loading it into a Channel for playback. Please be patient if you choose to do so. It is recommended that this format is used only for files that will be downloaded and then copied somewhere else for storage, that is, file that won't be normally played with PyPlayer.

## Contact

Thank you for using PyPlayer!

Please send bug reports and feature requests at mogaoscar@gmail.com
If you want to help develop a frontend, also contact me at mogaoscar@gmail.com
