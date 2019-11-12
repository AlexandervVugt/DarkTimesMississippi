

def setup():
    global cardFront, cardBack, state, framePointer
    fullScreen()
    frameRate(60)
    cardFront = loadImage("card_front.png")
    cardBack = loadImage("card_back.png")
    state = "before"
    framePointer = 0
    
def draw():
    global cardFront, cardBack, state, framePointer
    background(0, 255, 0)
    translate(width/2, height/2)
    if state == "before":
        textAlign(CENTER)
        textSize(32)
        fill(255)
        text("Click anywhere to draw a card", 0, 0)
    if state == "animate":
        rotate(radians(((frameCount - framePointer)/frameRate)*360))
        scale((frameCount - framePointer)/(5*frameRate))
        image(cardBack, -(cardBack.width/2), -(cardBack.height/2))
        if frameCount >= 5*frameRate + framePointer:
            state = "done"
    if state == "done":
        image(cardFront, -(cardFront.width/2), -(cardBack.height/2))
        
def mousePressed():
    global state, framePointer
    if state == "before":
        framePointer = frameCount
        state = "animate"
