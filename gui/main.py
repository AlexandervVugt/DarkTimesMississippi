import inputScreen, event, dice, turn, popup_modify, popup_confirm, victorious, eventScreen, startScreen, manual_rules, eventScreen, manual_rules2, manual_rules3, manual_rules4, settingsScreen
import logic.Game as Game
import logic.GameController as GameController

global currentScene, scenes, game, gameController

def setup():
    global currentScene, scenes, bg
    bg = loadImage("background.png")
    
    # currentScene is used like a stack
    # to nest a scene, use append(<scene you want to show>) to change the scene
    # to replace the current scene, use pop() and append(<scene you want to show>) to replace the scene
    # to go back to the previous scene, use pop()
    # to call the current scene, use currentScene[-1]
    currentScene = [startScreen]
    #create a map for scenes and their names
    scenes = {
              "startScreen": startScreen,
              "inputScreen": inputScreen,
              "event": event,
              "dice": dice,
              "turn": turn,
              "popup_modify": popup_modify,
              "popup_confirm": popup_confirm,
              "victorious": victorious,
              "manual_rules": manual_rules,
              "eventScreen": eventScreen,
              "manual_rules2": manual_rules2,
              "manual_rules3": manual_rules3,
              "manual_rules4": manual_rules4,
              "settingsScreen": settingsScreen
              }
    
    for scene in scenes.values():
        scene.setup()
    
def draw():
    image(bg, 0, 0)
    global currentScene
    
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
    
