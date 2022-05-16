#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:38:48 2022

@author: Mogaoscar
"""

import pygame as pg
from pydub import AudioSegment, effects 
import yt_dlp as ytdl
import os
        
def normalize_sound(path,codec):
    rawsound = AudioSegment.from_file(path, codec)  
    normalizedsound = effects.normalize(rawsound)  
    normalizedsound.export(path, format=codec)

def is_supported(url):
    extractors = ytdl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(url) and e.IE_NAME != 'generic':
            return True
    return False


def clear_console():    
    from sys import platform
    
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')


def select_options (opt,SUPPORTED_CODEC,PATH):    
    
    opt.video_url = input("\nPlease enter youtube video URL: ")
    if not is_supported (opt.video_url):
        input ("\n\nURL is not valid or link is broken...\nPress ENTER to return to the MENU...")
        return False
    
    opt.codec = input(f"\n\nPlease enter preferred codec ({SUPPORTED_CODEC})...: ")
    while opt.codec not in SUPPORTED_CODEC:
        print (f"\n\n{opt.codec} is not a valid codec.")
        opt.codec = input(f"\nPlease enter preferred codec ({SUPPORTED_CODEC}): ")
    
    opt.filename = str(input ("\nPlease enter the name for the audio file that will be downloaded (empty for original video title): "))
    while not isinstance(opt.filename, str) and opt.filename != '':
        print (f"\n\n'{opt.filename}' is not a valid name.")
        opt.filename = input ("\nPlease enter the name for the audio file that will be downloaded: ")
    if opt.filename == '':
        video_info = ytdl.YoutubeDL().extract_info(
           url = opt.video_url, download=False
       )
        opt.filename = f"{PATH}/{video_info['title']}.{opt.codec}"
    else:
        opt.filename = f"{PATH}/{opt.filename}.{opt.codec}"
       
    return True
    
def download_audio (opt):    
    yt_options={
       'format':'bestaudio/best',
       'outtmpl': opt.filename,
       'postprocessors': [{
           'key': 'FFmpegExtractAudio',
           'preferredcodec': opt.codec,
           'preferredquality': '192',
       }],
   }
   
    print (opt.codec)
    print (opt.filename)
    print (opt.video_url)
    with ytdl.YoutubeDL(yt_options) as ydl:
       ydl.download(opt.video_url)
    
    normalize_sound(opt.filename, opt.codec)
    

def find_file (SUPPORTED_CODEC,PATH):    
    
    # Prompts the user to input a search term
    # Searches a file in '/audio' that contains that search term in its name
    # Returns path to selected file if found.
    # Returns boolean False if not found
    
    file_name = input ("\n\nPlease write the name of the file you want to play: ")
    
    for file in os.listdir(PATH):
        if file_name.lower() in file.lower() and file.endswith(tuple(SUPPORTED_CODEC)) and not file.startswith('.'):
            selector = input (f"\n{file} was found. Confirm? (y/n): ")
            while selector in ['y', 'Y','n','N']:
                if selector in ['Y','y']:
                    soundfile=f"{PATH}/{file}"
                    break
                elif selector in ['N','n']:
                    print ("\nSearching further...\n")
                    break
    
    if 'soundfile' in locals():        
        return soundfile
    
    else:
        return False


def stream_audio (opt,SUPPORTED_CODEC,PATH):
    select_options(opt,SUPPORTED_CODEC,PATH)
    download_audio (opt)
    pg.mixer.music.load(opt.filename)
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.1)
    
    input("\nPress ENTER to STOP music\n")
    
    pg.mixer.music.stop()
    os.remove(opt.filename)
    

def play(soundfile,CHANNELS,SOUNDS):
    try:        
        i=0
        while CHANNELS[i].get_busy():
            i+=1    
        
        SOUNDS[i]=soundfile
        Sound=pg.mixer.Sound(SOUNDS[i]) 
        CHANNELS[i].play(Sound)
        CHANNELS[i].set_volume(0.05) #This is user volume 50%
            
    except:
        input ("Something went wrong in the 'play()' function")
        return False
    else:   
        print(f"\nNow playing {soundfile}") 
        return True
    
def find_active_channels (CHANNELS,SOUNDS):
    i = 0
    channelid = 0
    while channelid < len(CHANNELS):
        if CHANNELS[channelid].get_busy():
            print (f"Channel {channelid} -- {SOUNDS[channelid]}\n")
            active_channel = channelid
            i+=1
        channelid+=1
    
    return active_channel, i
    

def change_volume(CHANNELS,SOUNDS):
    clear_console()
    
    active_channel, total_active_channels = find_active_channels (CHANNELS,SOUNDS)
    
    if total_active_channels>1:   
        active_channel = int(input("\nSelect in which channel to change the volume: "))
    
    if total_active_channels==0:
        return
    
    volume = float(input("\n\nEnter volume (0-100): "))
    
    if volume > 100: volume = 100
    elif volume <0: volume = 0
    
    volume = volume * 0.001 #So that Volume is actually between 0% and 10% of what pygame outputs.
    CHANNELS[active_channel].set_volume(volume)    
    

def stop(CHANNELS,SOUNDS,fadeout):
    clear_console()
    
    active_channel, total_active_channels = find_active_channels (CHANNELS,SOUNDS)
    
    
    if total_active_channels>1:   
        active_channel = int(input("\nSelect what channel to stop: "))
        CHANNELS[active_channel].fadeout(fadeout)
    
    if total_active_channels==1:
        CHANNELS[active_channel].fadeout(fadeout)
        
    
    

def stop_all():
    pg.mixer.stop()
        
        
        