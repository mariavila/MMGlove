import explorerhat
import time

#Trying if it works

while 1:
    if(explorerhat.input.one.read()==1):
        explorerhat.light.red.on()
    else:
        explorerhat.light.red.off()
    explorerhat.light.green.on();
    time.sleep(3) # 3secs
