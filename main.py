import explorerhat
import time
import pygame

#Trying if it works
pygame.mixer.init()
pygame.init()

quin=0;
while 1:
    if(explorerhat.input.one.read()==1):
        if(explorerhat.input.two.read()==1):
            print("entro 12")
            if(quin !=5):
                pygame.mixer.music.load("Dit12/tetris.mp3")
                pygame.mixer.music.play()
                quin=5
        else:
            print("entro 1")
            if quin!=1:
                pygame.mixer.music.load("Dit1/mario.mp3")
                pygame.mixer.music.play()
                quin=1
    else:
        if(explorerhat.input.two.read()==1):
            print("entro 2")
            if(quin!=2):
                pygame.mixer.music.load("Dit2/zelda.mp3")
                pygame.mixer.music.play()
                quin=2
        else:
            pygame.mixer.music.stop()
            quin=0
    time.sleep(0.2) # 3secs
