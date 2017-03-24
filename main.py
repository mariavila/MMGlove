import explorerhat
import time
import pygame

#Trying if it works
pygame.mixer.init()
pygame.init()

playingTune=0
caseVar = 0

while 1:
    playingTune = caseVar
    caseVar = explorerhat.input.one.read() + explorerhat.input.two.read() * 2 + explorerhat.input.three.read() * 4 + explorerhat.input.four.read() * 8

    if playingTune != caseVar:
        if (caseVar == 0):
            pygame.mixer.music.stop()

        elif (caseVar == 1):
            print("entro 1")
            pygame.mixer.music.load("Dit1/mario.mp3")
            pygame.mixer.music.play()

        elif (caseVar == 2):
            print("entro 2")
            pygame.mixer.music.load("Dit2/zelda.mp3")
            pygame.mixer.music.play()

        elif (caseVar == 3):
            break


        elif (caseVar == 4):
            print("entro 3")
            pygame.mixer.music.load("Dit3/tetris.mp3")
            pygame.mixer.music.play()

        elif (caseVar == 5):
            break

        elif (caseVar == 6):
            break

        elif (caseVar == 7):
            break

        elif (caseVar == 8):
            print("entro 4")
            pygame.mixer.music.load("Dit4/pokemon.mp3")
            pygame.mixer.music.play()

        elif (caseVar == 9):
            break

        elif (caseVar == 10):
            break

        elif (caseVar == 11):
            break

        elif (caseVar == 12):
            break

        elif (caseVar == 13):
            break

        elif (caseVar == 14):
            break

        elif (caseVar == 15):
            break

    time.sleep(0.01) # 0.01secs
