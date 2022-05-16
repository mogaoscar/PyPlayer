#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:32:28 2022

@author: Mogaoscar
"""

class options ():   
    def __init__ (self, codec):
        self.codec = codec
        self.video_url = ''
        self.path = ''
        self.filename = "{video_info['title']}.mp3"

def setup (app_path):
    
    import pygame as pg
    import os
    
    print ("printf '\e[8;50;100t'")
    
    pg.mixer.init()
    pg.mixer.stop()
    
    SOUNDS = []
    CHANNELS = []
    
    Channel0=pg.mixer.Channel(0)
    Channel1=pg.mixer.Channel(1)
    Channel2=pg.mixer.Channel(2)
    Channel3=pg.mixer.Channel(3)
    Channel4=pg.mixer.Channel(4)
    Channel5=pg.mixer.Channel(5)
    Channel6=pg.mixer.Channel(6)
    Channel7=pg.mixer.Channel(7) 
    
    
    Sound0=''
    Sound1=''
    Sound2=''
    Sound3=''
    Sound4=''
    Sound5=''
    Sound6=''
    Sound7=''   
    
    
    CHANNELS = [Channel0,Channel1,Channel2,Channel3,Channel4,Channel5,Channel6,Channel7]
    SOUNDS = [Sound0,Sound1,Sound2,Sound3,Sound4,Sound5,Sound6,Sound7]
    SUPPORTED_CODEC=['mp3','wav']
    
    pg.mixer.set_num_channels(len(CHANNELS))
    
    for i in range(len(CHANNELS)):
        CHANNELS[i].set_volume(0.05) #this is user volume 50%, absolute volume 5%
    
    opt = options('wav')
    fadeout=2000
    
    PATH = os.path.join((app_path),'audio')
    
    try:
        os.mkdir (PATH)
    except FileExistsError:
        pass
    
    HEADER='''
8888888b.           8888888b.  888                                    
888   Y88b          888   Y88b 888                                    
888    888          888    888 888                                    
888   d88P 888  888 888   d88P 888  8888b.  888  888  .d88b.  888d888 
8888888P"  888  888 8888888P"  888     "88b 888  888 d8P  Y8b 888P"   
888        888  888 888        888 .d888888 888  888 88888888 888     
888        Y88b 888 888        888 888  888 Y88b 888 Y8b.     888     
888         "Y88888 888        888 "Y888888  "Y88888  "Y8888  888     
                888                              888                  
           Y8b d88P                         Y8b d88P                  
            "Y88P"                           "Y88P"
            '''
            
    MENU='''
    
   _  _ ____ _  _ _  _ 
   |\/| |___ |\ | |  | 
   |  | |___ | \| |__|

 '''
    
    return PATH, SUPPORTED_CODEC, opt, CHANNELS, SOUNDS, HEADER, MENU, fadeout