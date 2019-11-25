import inputScreen, event, dice
import logic.Game as Game

global currentScene, scenes#, game

def setup():
    global currentScene, scenes
    
    inputScreen.vars()
    event.vars()
    dice.vars()
    
    currentScene = inputScreen
    #create a map for scenes and their names
    scenes = {
              "inputScreen": inputScreen,
              "event": event,
              "dice": dice
              }
    
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
