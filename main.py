import explorerhat
import time
import pygame

#Trying if it works
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("mario.mp3")
while 1:
    #explorerhat.light.blue.off()
    #time.sleep(2) # 3secs

    if(explorerhat.input.one.read()==1):
        pygame.mixer.music.play()
        #explorerhat.light.blue.on()
    else:
        pygame.mixer.music.stop()
        #pygame.mixer.stop()
        explorerhat.light.blue.off()
    time.sleep(0.2) # 3secs
