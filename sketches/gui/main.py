import inputScreen, event, dice

global currentScene, scenes

def setup():
    global currentScene
    
    inputScreen.vars()
    event.vars()
    dice.vars()
    
    currentScene = inputScreen
    #create a map for scenes and their names
    #scenes = 
    
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
