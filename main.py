import explorerhat
import time

#Trying if it works

while 1:
    #explorerhat.light.blue.off()
    #time.sleep(2) # 3secs
    
    if(explorerhat.input.one.read()==1):
        explorerhat.light.blue.on()
    else:
        explorerhat.light.blue.off()
    time.sleep(0.2) # 3secs
