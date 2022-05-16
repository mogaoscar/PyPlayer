#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 12:16:30 2022

@author: Mogaoscar
"""

from setup import setup
import PyPlayer as pp


def main ():
      
    PATH, SUPPORTED_CODEC, opt, CHANNELS, SOUNDS, HEADER, MENU, fadeout = setup (app_path)
               
    while True:
        
        pp.clear_console()
        
        print (HEADER)
        print (MENU)
        print("1. Download Youtube audio\n2. Play stored audio file\n3. Stream Youtube audio\n4. Change Channel Volume\n5. Stop Channel\n6. Stop all\n7. Exit")
        
        selector = str(input ("\n\nSelect option number: "))       
        
        pp.clear_console()
        
        if selector == "1":
            if pp.select_options(opt,SUPPORTED_CODEC,PATH):
                pp.download_audio(opt)
            
        elif selector == "2":
            soundfile = pp.find_file(SUPPORTED_CODEC,PATH)
            if soundfile:
                if pp.play(soundfile,CHANNELS,SOUNDS):
                    input ('\nPress ENTER to return to the MENU')
            else:
                input ("No file containing that name was found in the audio folder... press ENTER to go back to the MENU")
                
        elif selector == "3":
            pp.stream_audio(opt,SUPPORTED_CODEC,PATH)
        
        elif selector == '4':
            pp.change_volume(CHANNELS, SOUNDS)
            
        elif selector == "5":
            pp.stop(CHANNELS, SOUNDS, fadeout)
        
        elif selector == "6":
            pp.stop_all()
            
        elif selector == "7":
            pp.clear_console
            print ("\n\nThank you for using PyPlayer!\n\nPlease send bug reports and feature requests at mogaoscar@gmail.com\nIf you want to help develop a frontend, also contact me at mogaoscar@gmail.com")
            break
    

if __name__ == "__main__":
    #!/usr/bin/python3
    import sys, os
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        app_path = os.path.dirname(sys.executable)
    else:
        app_path = os.path.dirname(os.path.abspath(__file__))
        
    main()