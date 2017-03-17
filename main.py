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
            if(quin !=5):
                pygame.mixer.music.load("/Dit12/*.mp3")
                pygame.mixer.music.play()
                quin=5
        else:
            if quin!=1:
                pygame.mixer.music.load("/Dit1/*.mp3")
                pygame.mixer.music.play()
                quin=1
    else:
        if(explorerhat.input.two.read()==1):
            if(quin!=2):
                pygame.mixer.music.load("/Dit2/*.mp3")
                pygame.mixer.music.play()
                quin=2
        else:
            pygame.mixer.music.stop()
            quin=2
    time.sleep(0.2) # 3secs
