add_library('sound')
import main


def setup():
    global s
    
    size(1440, 900) 
    main.setup()
    sound = SoundFile(this, 'epicmusic.mp3')
    main.setup_sound(sound)
    
def draw():
    main.draw()
    
def keyTyped():
    main.keyTyped()
    
def keyPressed():
    main.keyPressed()

def mousePressed():
    main.mousePressed()
