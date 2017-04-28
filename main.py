import explorerhat
import time
import pygame
import pygame.midi
def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %(i, interf, name, opened, in_out))

#Trying if it works
pygame.init()
#pygame.mixer.init()
pygame.midi.init()

player = pygame.midi.Output(0)
player.set_instrument(0,1)

playingTune = 0
caseVar = 0

print (pygame.midi.get_device_info(0))
print (pygame.midi.get_default_output_id())

_print_device_info()

while 1:
    playingTune = caseVar
    caseVar = explorerhat.input.one.read() + explorerhat.input.two.read() * 2 + explorerhat.input.three.read() * 4 + explorerhat.input.four.read() * 8

    if playingTune != caseVar:
        #if (caseVar == 0):
            #pygame.mixer.music.stop()


        if (caseVar == 1):
            print("entro 1")
            #pygame.mixer.music.load("Dit1/mario.mp3")
            #pygame.mixer.music.play()

        elif (caseVar == 2):
            print("entro 2")
            #pygame.mixer.music.load("Dit2/zelda.mp3")
            #pygame.mixer.music.play()

        elif (caseVar == 3):
            print("entro 1+2")


        elif (caseVar == 4):
            print("entro 3")
            #pygame.mixer.music.load("Dit3/tetris.mp3")
            #pygame.mixer.music.play()

        elif (caseVar == 5):
            print("entro 1+3")

        elif (caseVar == 6):
            print("entro 2+3")

        elif (caseVar == 7):
            print("entro 1+2+3")

        elif (caseVar == 8):
            print("entro 4")
            player.note_on(53, 127, 1)
            time.sleep(2)
            player.note_off(53, 127, 1)
            #pygame.mixer.music.load("Dit4/pokemon.mp3")
            #pygame.mixer.music.play()

        elif (caseVar == 9):
            print("entro 1+4")

        elif (caseVar == 10):
            print("entro 2+4")

        elif (caseVar == 11):
            print("entro 1+2+4")

        elif (caseVar == 12):
            print("entro 3+4")

        elif (caseVar == 13):
            print("entro 1+3+4")

        elif (caseVar == 14):
            print("entro 2+3+4")

        elif (caseVar == 15):
            print("entro 1+2+3+4")

    time.sleep(0.01) # 0.01secs
