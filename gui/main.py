import inputScreen, event, dice, turn
import logic.Game as Game

global currentScene, scenes, game

def setup():
    global currentScene, scenes
    
    # inputScreen.setup()
    # event.setup()
    # dice.setup()
    # turn.setup()
    
    currentScene = inputScreen
    #create a map for scenes and their names
    scenes = {
              "inputScreen": inputScreen,
              "event": event,
              "dice": dice,
              "turn": turn
              }
    
    for scene in scenes.values():
        scene.setup()
    
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
