import inputScreen, event, dice, turn, popup_modify, popup_confirm, victorious
import logic.Game as Game
import logic.GameController as GameController

global currentScene, scenes, game, gameController

def setup():
    global currentScene, scenes
    
    # currentScene is used like a stack
    # to nest a scene, use append(<scene you want to show>) to change the scene
    # to replace the current scene, use pop() and append(<scene you want to show>) to replace the scene
    # to go back to the previous scene, use pop()
    # to call the current scene, use currentScene[-1]
    currentScene = [inputScreen]
    #create a map for scenes and their names
    scenes = {
              "inputScreen": inputScreen,
              "event": event,
              "dice": dice,
              "turn": turn,
              "popup_modify": popup_modify,
              "popup_confirm": popup_confirm,
              "victorious": victorious
              }
    
    for scene in scenes.values():
        scene.setup()
    
def draw():
    global currentScene
    
    if not currentScene[-1] == scenes.get("dice") or frameCount%5 == 0:
        background(0, 255, 0)
    currentScene[-1].draw()
    
def keyTyped():
    currentScene[-1].keyTyped()
    
def keyPressed():
    currentScene[-1].keyPressed()
    
def mousePressed():
    currentScene[-1].mousePressed()
    
def createGame(players):
    global game
    
    game = Game.Game(players)
    
def createController():
    global game, gameController
    
    gameController = GameController.GameController(game)
    
