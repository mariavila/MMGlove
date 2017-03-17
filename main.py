import explorerhat
import time
import pygame

#Trying if it works
pygame.mixer.init()
pygame.init()

quin=0;
while 1:
    #quin=1
    if(explorerhat.input.one.read()==1):
        if quin!=1:
            pygame.mixer.music.load("mario.mp3")
            pygame.mixer.music.play()
            quin=1
    else:
        if(quin!=0):
            pygame.mixer.music.stop()
            quin=0
    time.sleep(0.2) # 3secs
