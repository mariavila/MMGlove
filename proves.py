import explorerhat
import time
from mingus.midi import fluidsynth


playingTune = 0
caseVar = 0

fluidsynth.set_instrument(1, 14)

while 1:
    playingTune = caseVar
    caseVar = explorerhat.input.one.read() + explorerhat.input.two.read() * 2 + explorerhat.input.three.read() * 4 + explorerhat.input.four.read() * 8

    if playingTune != caseVar:
        #if (caseVar == 0):
            #pygame.mixer.music.stop()


        if (caseVar == 1):
            print("entro 1")
            n = Note("C-5")
            n.channel = 5
            n.velocity = 50
            fluidsynth.play_Note(n)
            time.sleep(2)
            fluidsynth.stop_Note(n, 1)
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
