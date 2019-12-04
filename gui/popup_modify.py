import main

global action

def setup():
    global title, userIn, num
    
    title = "Enter the amount to modify, then press the <ENTER> key to confirm."
    userIn = ''
    num = '-0123456789'
    action = None
    
def draw():
    global title
    
    background(0, 255, 0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(255)
    text(title, width/2, height/3)
    textSize(24)
    text(userIn, width/2, 2*height/3)
    
def keyTyped():
    global userIn, num
    
    if key == ENTER or key == RETURN or key == BACKSPACE:
        return
    if key in num:
        userIn += key
    
def keyPressed():
    global userIn
    
    if (key == ENTER or key == RETURN) and len(userIn) > 0:
        action(int(userIn))
        setup()
        main.currentScene.pop()
    elif key == BACKSPACE:
        userIn = userIn[:-1]
        
def mousePressed():
    return
