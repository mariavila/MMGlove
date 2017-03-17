import explorerhat
import time
import pygame

#Trying if it works
pygame.mixer.init()
s=pygame.mixer.Sound("mario.mp3")
while 1:
    #explorerhat.light.blue.off()
    #time.sleep(2) # 3secs

    if(explorerhat.input.one.read()==1):
        s.play()
        #explorerhat.light.blue.on()
    else:
        s.stop()
        #pygame.mixer.stop()
        explorerhat.light.blue.off()
    time.sleep(0.2) # 3secs
