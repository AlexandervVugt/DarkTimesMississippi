import main

global action

def setup():
    global title, confirm_text, cancel_text
    
    title = "Are you sure?"
    confirm_text = "CONFIRM"
    cancel_text = "CANCEL"
    
def draw():
    global title, confirm_text, cancel_text
    
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
            main.currentScene.pop()
        elif mouseX in range(width/2, 3*width/4):
            #cancel
            main.currentScene.pop()
