import pibrella
import time

#Trying if it works

while 1:
    if(pirbella.input.e.read()==1):
        pibrella.light.red.on()
    else:
        pibrella.light.red.off()
    time.sleep(3) # 3secs
