import main

def setup():
    global cardFront, cardBack, state, framePointer, fading
    cardFront = loadImage("card_front.png")
    cardBack = loadImage("card_back.png")
    state = "before"
    framePointer = 0
    fading = 0
    
def draw():
    global cardFront, cardBack, state, framePointer, fading, cardText
    
    background(0, 255, 0)
    translate(width/2, height/2)
    if state == "before":
        textAlign(CENTER)
        textSize(32)
        fill(255)
        text("Click anywhere to draw a card", 0, 0)
    elif state == "animate":
        rotate(radians(((frameCount - framePointer)/frameRate)*360))
        scale((frameCount - framePointer)/(3*frameRate))
        image(cardBack, -(cardBack.width/2), -(cardBack.height/2))
        if frameCount >= 3*frameRate + framePointer:
            state = "fade"
    elif state == "fade":
        tint(255, 255 - fading)
        image(cardBack, -(cardBack.width/2), -(cardBack.height/2))
        tint(255, fading)
        image(cardFront, -(cardFront.width/2), -(cardBack.height/2))
        if fading >= 255:
            state = "done"
        fading += 255/60
    elif state == "done":
        image(cardFront, -(cardFront.width/2), -(cardBack.height/2))
        textAlign(CENTER)
        textSize(32)
        fill(0)
        # cardText = main.game.randEvent().toString()
        text(cardText, 0, 0)
        
def mousePressed():
    global state, framePointer, cardText
    
    if state == "before":
        framePointer = frameCount
        state = "animate"
    elif state == "animate" or state == "fade":
        cardText = main.game.randEvent().toString()
        state = "done"
    elif state == "done":
        setup()
        main.currentScene.pop()
        
def keyTyped():
    return

def keyPressed():
    return
