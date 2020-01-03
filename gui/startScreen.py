import main

def setup():
    global bg, font, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH
    bg = loadImage("background.png")
    font = loadFont('BanglaMN-48.vlw')
    buttonA = range(450, 950)
    buttonB = range(350, 425)
    buttonC = range(450, 950)
    buttonD = range(450, 525)
    buttonE = range(450, 950)
    buttonF = range(550, 625)
    buttonG = range(450, 950)
    buttonH = range(650, 725)

def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    textAlign(LEFT, LEFT)
    
    fill (150, 0, 0)
    textSize(75)
    textFont(font, 75)
    text('DarkTimesMississippi', 300, 200)
    
    fill(0, 0, 0)
    rect(450, 350, 500, 75)
    fill(255, 255, 255)
    textSize(50)
    text('New Game', 555, 405)
    if ((mouseX in buttonA) and (mouseY in buttonB)):
        fill(100, 100, 100)
        rect(450, 350, 500, 75)
        fill(255, 255, 255)
        textSize(50)
        text('New Game', 555, 405)
    
    fill(0, 0, 0)
    rect(450, 450, 500, 75)
    fill(255, 255, 255)
    textSize(50)
    text('Manual & Rules', 490, 505)
    if ((mouseX in buttonC) and (mouseY in buttonD)):
        fill(100, 100, 100)
        rect(450, 450, 500, 75)
        fill(255, 255, 255)
        textSize(50)
        text('Manual & Rules', 490, 505)
    
    fill(0, 0, 0)
    rect(450, 550, 500, 75)
    fill(255, 255, 255)
    textSize(50)
    text('Event Cards', 530, 605)
    if ((mouseX in buttonE) and (mouseY in buttonF)):
        fill(100, 100, 100)
        rect(450, 550, 500, 75)
        fill(255, 255, 255)
        textSize(50)
        text('Event Cards', 530, 605)
        
    fill(0, 0, 0)
    rect(450, 650, 500, 75)
    fill(255, 255, 255)
    textSize(50)
    text('Settings', 585, 705)
    if ((mouseX in buttonG) and (mouseY in buttonH)):
        fill(100, 100, 100)
        rect(450, 650, 500, 75)
        fill(255, 255, 255)
        textSize(50)
        text('Settings', 585, 705)
        
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD)) or ((mouseX in buttonE) and (mouseY in buttonF)) or ((mouseX in buttonG) and (mouseY in buttonH))):
        cursor(HAND)
    else:
        cursor(ARROW)

def mousePressed():
    global buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH
    if mouseX in buttonA and mouseY in buttonB:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("inputScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules"))
    if mouseX in buttonE and mouseY in buttonF:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("eventScreen"))
    if mouseX in buttonG and mouseY in buttonH:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("settingsScreen"))

def keyPressed():
    return

def keyTyped():
    return
