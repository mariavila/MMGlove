from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import explorerhat
import time
import pygame
import pygame.midi

def runFunc():
    socketio.run(app, host='0.0.0.0')

app = Flask(__name__)
socketio = SocketIO(app)
thread = threading.Thread(None, runFunc)

@app.route('/')
def hello_func():
    #print ('ohayo')
    return render_template('hello.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    socketio.emit('ping event', {'data': 42})

pygame.init()
#pygame.mixer.init()
pygame.midi.init()

player = pygame.midi.Output(2)
player.set_instrument(0)

playingTune = 0
caseVar = 0
mode = 0
notes =[]

if __name__ == '__main__':
    thread.start()
    while 1:
        playingTune = caseVar
        caseVar = explorerhat.input.one.read() + explorerhat.input.two.read() * 2 + explorerhat.input.three.read() * 4 + explorerhat.input.four.read() * 8

        if playingTune != caseVar:
            #if (caseVar == 0):
                #pygame.mixer.music.stop()


            if (caseVar == 1):
                print("entro 1")
                socketio.emit('finger1')
                #pygame.mixer.music.load("Dit1/mario.mp3")
                #pygame.mixer.music.play()
                if mode==0:
                    player.set_instrument(0)
                    mode+=1
                    playingTune=20
                elif mode==1:
                    mode+=1
                    playingTune=20
                elif mode==2:
                    file= open("music.txt", 'w')
                    ini=0
                    for aux in notes:
                        if aux==48:
                            if ini=0
                                file.write("DO")
                            else
                                file.write(", DO")
                        elif aux==50:
                            if ini=0
                                file.write("RE")
                            else
                                file.write(", RE")
                        elif aux==52:
                            if ini=0
                                file.write("MI")
                            else
                                file.write(", MI")
                        elif aux==53:
                            if ini=0
                                file.write("FA")
                            else
                                file.write(", FA")
                        elif aux==55:
                            if ini=0
                                file.write("SOL")
                            else
                                file.write(", SOL")
                        elif aux==57:
                            if ini=0
                                file.write("LA")
                            else
                                file.write(", LA")
                        elif aux==59:
                            if ini=0
                                file.write("SI")
                            else
                                file.write(", SI")
                        elif aux==60:
                            if ini=0
                                file.write("DO4")
                            else
                                file.write(", DO4")
                    file.close()
                    mode = 0
                    playingTune=20

            elif (caseVar == 2):
                print("entro 2")
                #pygame.mixer.music.load("Dit2/zelda.mp3")
                #pygame.mixer.music.play()
                if mode==0:
                    socketio.emit('finger2')
                    player.set_instrument(24)
                    mode+=1
                    playingTune=20
                elif mode==1:
                    player.note_on(48, 127)
                    time.sleep(0.5)
                    player.note_off(48, 127)
                    notes= notes + [48]
                elif mode==2:
                    socketio.emit('finger2')
                    notes=notes[:-1]

            elif (caseVar == 3):
                print("entro 1+2")
                if mode ==1:
                    player.note_on(53, 127)
                    time.sleep(0.5)
                    player.note_off(53, 127)
                    notes= notes + [53]

            elif (caseVar == 4):
                print("entro 3")
                if mode==0:
                    socketio.emit('finger3')
                    player.set_instrument(40)
                    mode+=1
                    playingTune=20
                elif mode ==1:
                    player.note_on(50, 127)
                    time.sleep(0.5)
                    player.note_off(50, 127)
                    notes= notes + [50]
                elif mode==2:
                    socketio.emit('finger3')
                    aux=0
                    for aux in notes:
                        player.note_on(aux, 127)
                        time.sleep(0.5)
                        player.note_off(aux, 127)

            elif (caseVar == 5):
                print("entro 1+3")
                if mode ==1:
                    player.note_on(55, 127)
                    time.sleep(0.5)
                    player.note_off(55, 127)
                    notes= notes + [55]

            elif (caseVar == 6):
                print("entro 2+3")
                if mode ==1:
                    player.note_on(59, 127)
                    time.sleep(0.5)
                    player.note_off(59, 127)
                    notes= notes + [59]

            elif (caseVar == 7):
                print("entro 1+2+3")

            elif (caseVar == 8):
                print("entro 4")
                if mode==0:
                    socketio.emit('finger4')
                    player.set_instrument(65)
                    mode+=1
                    playingTune=20
                elif mode ==1:
                    player.note_on(52, 127)
                    time.sleep(0.5)
                    player.note_off(52, 127)
                    notes= notes + [52]
                elif mode==2:
                    socketio.emit('finger4')
                    mode = 1
                    playingTune=20
                #pygame.mixer.music.load("Dit4/pokemon.mp3")
                #pygame.mixer.music.play()

            elif (caseVar == 9):
                print("entro 1+4")
                if mode ==1:
                    player.note_on(57, 127)
                    time.sleep(0.5)
                    player.note_off(57, 127)
                    notes= notes + [57]

            elif (caseVar == 10):
                print("entro 2+4")

            elif (caseVar == 11):
                print("entro 1+2+4")

            elif (caseVar == 12):
                print("entro 3+4")
                if mode ==1:
                    player.note_on(60, 127)
                    time.sleep(0.5)
                    player.note_off(60, 127)
                    notes= notes + [60]

            elif (caseVar == 13):
                print("entro 1+3+4")

            elif (caseVar == 14):
                print("entro 2+3+4")

            elif (caseVar == 15):
                print("entro 1+2+3+4")

        time.sleep(0.05) # 0.05secs
