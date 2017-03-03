import pibrella
import time

#Trying if it works

while 1:
    pibrella.light.red.on();
    time.sleep(3); # 3secs
    pibrella.light.red.off();
    time.sleep(3); # 3secs
