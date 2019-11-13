import inputScreen

def setup():
    global currentScene
    
    fullScreen()
    
    inputScreen.vars()
    
    currentScene = inputScreen
    
def draw():
    global currentScene
    
    background(0, 255, 0)
    currentScene.draw()
    
def keyTyped():
    currentScene.keyTyped()
    
def keyPressed():
    currentScene.keyPressed()
    
def mousePressed():
    currentScene.mousePressed()
