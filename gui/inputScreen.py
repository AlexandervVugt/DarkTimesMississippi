import main
import logic.Game as Game
import logic.Player as Player

def setup():
    global names, input, title, buttonText, buttonX, buttonY, alph
    names = []
    input = ""
    title = "Please enter the players of the names who will play."
    buttonText = "Start game"
    buttonX = range(3*width/8, 3*width/8 + width/4)
    buttonY = range(3*height/4, 3*height/4 + 100)
    alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
def draw():
    global names, input, title, buttonText
    background(0, 255, 0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(255)
    text(title, width/2, height/8)
    if len(names) < 4:
        rect(width/4, height/4 + len(names)*100, width/2, 100, 10)
        fill(0)
        text(input, width/4, height/4 + len(names)*100, width/2, 100)
    for x in range(0, len(names)):
        fill(255)
        text(names[x], width/4, height/4 + x*100, width/2, 100)
    fill(0, 0, 255)
    rect(3*width/8, 3*height/4, width/4, 100, 10)
    fill(255)
    text(buttonText, 3*width/8, 3*height/4, width/4, 100)
        
def keyTyped():
    global input, names, alph
    if len(names) == 4:
        return
    if key == ENTER or key == RETURN or key == BACKSPACE:
        return
    if key in alph:
        input += key
    
def keyPressed():
    global names, input, title
    if len(names) == 4:
        return
    if (key == ENTER or key == RETURN) and len(input) > 0:
        names.append(input)
        input = ""
        if len(names) == 4:
            title = "Players:"
    elif key == BACKSPACE:
        input = input[:-1]
        
def mousePressed():
    global names, buttonX, buttonY, game
    if mouseX in buttonX and mouseY in buttonY and len(names) >= 2:
        # TODO: Create a game and start the game, switch to game screen.
        print(1)
        players = []
        print(2)
        for name in names:
            players.append(Player.Player(name))
        print(3)
        # not fully implemented
        # main.game = Game.Game(players)
        print(4)
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("turn"))
