import main

global action

def setup():
    global title, confirm_text, cancel_text, bg
    
    title = "Are you sure?"
    confirm_text = "CONFIRM"
    cancel_text = "CANCEL"
    action = None
    bg = loadImage("background.png")
    
def draw():
    global title, confirm_text, cancel_text
    
    image(bg, 0, 0)
    textAlign(CENTER, CENTER)
    textSize(50)
    fill(255)
    text(title, width/2, height/3)
    
    textSize(24)
    text(confirm_text, width/4, 2*height/3, width/2, 5*height/6)
    text(cancel_text, width/2, 2*height/3, 3*width/4, 5*height/6)
    
    fill(0, 153, 0)
    rect(width/4, 2*height/3, width/4, height/6)
    fill(204, 0, 0)
    rect(width/2, 2*height/3, width/4, height/6)
    
def keyPressed():
    return

def keyTyped():
    return

def mousePressed():
    if mouseY in range(2*height/3, 5*height/6):
        if mouseX in range(width/4, width/2):
            #confirm
            action()
            setup()
            main.currentScene.pop()
        elif mouseX in range(width/2, 3*width/4):
            #cancel
            setup()
            main.currentScene.pop()
