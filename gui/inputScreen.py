import main, turn
import logic.Player as Player

def setup():
    global names, input, title, buttonText, buttonX, buttonY, buttonC, buttonD, alph, bg, planks, plankslight
    names = []
    input = ""
    title = "Please enter the names of the players who will play."
    buttonText = "Start game"
    buttonX = range(3*width/8, 3*width/8 + width/4)
    buttonY = range(3*height/4, 3*height/4 + 100)
    buttonA = range(0, 100)
    buttonB = range(0, 100)
    buttonC = range(0, 100)
    buttonD = range(0, 50)
    alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    bg = loadImage("background.png")
    planks = loadImage("woodenplanks.png")
    planks.resize(width/4, 100)
    plankslight = loadImage("woodenplankslight.png")
    plankslight.resize(width/4, 100)
    
def draw():
    global names, input, title, buttonText
    image(bg, 0, 0)
    
    fill(100 if ((mouseX in buttonC) and (mouseY in buttonD)) else 0)
    rect(0, 0, 100, 50)
    fill(255)
    textSize(25)
    text('BACK', 50, 25)
    
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
    fill(0, 0, 0)
    image(planks if mouseX in buttonX and mouseY in buttonY else plankslight, 3*width/8, 3*height/4, width/4, 100)
    fill(210, 180, 140)
    if mouseX in buttonX and mouseY in buttonY:
        fill(217, 216, 114)
    text(buttonText, 3*width/8, 3*height/4, width/4, 100)
    
    if (((mouseX in buttonX) and (mouseY in buttonY)) or ((mouseX in buttonC) and (mouseY in buttonD))):
        cursor(HAND)
    else:
        cursor(ARROW)
    
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
    global names, buttonX, buttonY, buttonC, buttonD, game
    if mouseX in buttonX and mouseY in buttonY and len(names) >= 2:
        players = []
        for name in names:
            players.append(Player.Player(name))
        main.createGame(players)
        main.createController()
        main.gameController.startTurn(None)
        main.currentScene.pop()
        turn.refresh()
        main.currentScene.append(main.scenes.get("turn"))
    if mouseX in buttonC and mouseY in buttonD:
        fill(0, 0, 0)
        rect(0, 0, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 50, 25)
        main.currentScene.pop()
        
    # if mouseX in buttonA and mouseY in buttonB:
