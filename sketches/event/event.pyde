

def setup():
    global card
    fullScreen()
    frameRate(60)
    card = loadImage("card_back.png")
    
def draw():
    global card
    background(0, 255, 0)
    #imageMode(CENTER)
    #pushMatrix()
    translate(width/2, height/2)
    #pushMatrix()
    if frameCount <= 5*frameRate:
        rotate(radians((frameCount/frameRate)*360))
        scale(frameCount/(5*frameRate))
    #popMatrix()
    image(card, -(card.width/2), -(card.height/2))
