add_library('sound')
import main


def setup():
    global s
    
    size(1440, 900) 
    main.setup()
    s = SoundFile(this, 'epicmusic.mp3')
    s.amp(0.50)
    enable_sound()
    s.loop()
    
def mute_sound():
    s.stop()
    
def enable_sound():
    s.play()
    
def draw():
    main.draw()
    
def keyTyped():
    main.keyTyped()
    
def keyPressed():
    main.keyPressed()

def mousePressed():
    main.mousePressed()
