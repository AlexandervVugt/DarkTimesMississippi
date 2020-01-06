add_library('sound')
import main


def setup():
    size(1440, 900) 
    main.setup()
    s = SoundFile(this, 'epicmusic.mp3')
    s.amp(0.50)
    #s.play()
    #s.loop()
    
def draw():
    main.draw()
    
def keyTyped():
    main.keyTyped()
    
def keyPressed():
    main.keyPressed()

def mousePressed():
    main.mousePressed()
