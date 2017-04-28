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

player = pygame.midi.Output(2)
player.set_instrument(0)

playingTune = 0
caseVar = 0
mode = 1

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
            if mode==1:
                player.note_on(48, 127)
                time.sleep(2)
                player.note_off(48, 127)

        elif (caseVar == 3):
            print("entro 1+2")
            if mode ==1:
                player.note_on(53, 127)
                time.sleep(2)
                player.note_off(53, 127)

        elif (caseVar == 4):
            print("entro 3")
            if mode ==1:
                player.note_on(50, 127)
                time.sleep(2)
                player.note_off(50, 127)
            #pygame.mixer.music.load("Dit3/tetris.mp3")
            #pygame.mixer.music.play()

        elif (caseVar == 5):
            print("entro 1+3")
            if mode ==1:
                player.note_on(55, 127)
                time.sleep(2)
                player.note_off(55, 127)

        elif (caseVar == 6):
            print("entro 2+3")
            if mode ==1:
                player.note_on(59, 127)
                time.sleep(2)
                player.note_off(59, 127)

        elif (caseVar == 7):
            print("entro 1+2+3")

        elif (caseVar == 8):
            print("entro 4")
            if mode ==1:
                player.note_on(52, 127)
                time.sleep(2)
                player.note_off(52, 127)
            #pygame.mixer.music.load("Dit4/pokemon.mp3")
            #pygame.mixer.music.play()

        elif (caseVar == 9):
            print("entro 1+4")
            if mode ==1:
                player.note_on(57, 127)
                time.sleep(2)
                player.note_off(57, 127)

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
