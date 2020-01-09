add_library('sound')
import main


def setup():
    size(1440, 900, P3D)
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
