import main, inputScreen

def setup():
    global x, logo, bg, planks, planksdark, font, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH, buttonI, buttonJ
    x = inputScreen.x
    logo = loadImage("GameLogo.png")
    bg = loadImage("background.png")
    planks = loadImage("woodenplanks.png")
    planks.resize(500, 75)
    planksdark = loadImage("woodenplanksdark.png")
    planksdark.resize(500, 75)
    font = loadFont('BanglaMN-48.vlw')
    buttonA = range(440, 950)
    buttonB = range(350, 425)
    buttonC = range(440, 940)
    buttonD = range(450, 525)
    buttonE = range(440, 940)
    buttonF = range(550, 625)
    buttonG = range(440, 940)
    buttonH = range(650, 725)
    buttonI = range(440, 940)
    buttonJ = range(750, 825)

def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    textAlign(LEFT, LEFT)
    
    image(logo, 340, 50)
    
    textFont(font, 75)
    
    image(planks, 440, 350)
    fill(255, 225, 22)
    textSize(50)
    text('New Game', 545, 405)
    if ((mouseX in buttonA) and (mouseY in buttonB) and (x == 0)):
        image(planksdark, 440, 350)
        fill(237, 206, 0)
        textSize(50)
        text('New Game', 545, 405)
    
    if inputScreen.x == 1:
        image(planks, 440, 750)
        fill(255, 225, 22)
        textSize(50)
        text('Resume Game', 500, 805)
        if ((mouseX in buttonI) and (mouseY in buttonJ) and (inputScreen.x == 1)):
            image(planksdark, 440, 750)
            fill(237, 206, 0)
            textSize(50)
            text('Resume Game', 500, 805)
            
    image(planks, 440, 450)
    fill(255, 225, 22)
    textSize(50)
    text('Manual & Rules', 480, 505)
    if ((mouseX in buttonC) and (mouseY in buttonD)):
        image(planksdark, 440, 450)
        fill(237, 206, 0)
        textSize(50)
        text('Manual & Rules', 480, 505)
    
    image(planks, 440, 550)
    fill(255, 225, 22)
    textSize(50)
    text('Event Cards', 520, 605)
    if ((mouseX in buttonE) and (mouseY in buttonF)):
        image(planksdark, 440, 550)
        fill(237, 206, 0)
        textSize(50)
        text('Event Cards', 520, 605)
        
    image(planks, 440, 650)
    fill(255, 225, 22)
    textSize(50)
    text('Settings', 575, 705)
    if ((mouseX in buttonG) and (mouseY in buttonH)):
        image(planksdark, 440, 650)
        fill(237, 206, 0)
        textSize(50)
        text('Settings', 575, 705)
        
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD)) or ((mouseX in buttonE) and (mouseY in buttonF)) or ((mouseX in buttonG) and (mouseY in buttonH)) or ((mouseX in buttonI) and (mouseY in buttonJ) and (inputScreen.x == 1))):
        cursor(HAND)
    else:
        cursor(ARROW)

def mousePressed():
    global x, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH, buttonI, buttonJ
    if ((mouseX in buttonA and mouseY in buttonB)):
        image(planks, 440, 350)
        fill(255, 225, 22)
        textSize(50)
        text('New Game', 545, 405)
        main.currentScene.append(main.scenes.get("inputScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        image(planks, 440, 450)
        fill(255, 225, 22)
        textSize(50)
        text('Manual & Rules', 480, 505)
        main.currentScene.append(main.scenes.get("manual_rules"))
    if mouseX in buttonE and mouseY in buttonF:
        image(planks, 440, 550)
        fill(255, 225, 22)
        textSize(50)
        text('Event Cards', 520, 605)
        main.currentScene.append(main.scenes.get("eventScreen"))
    if mouseX in buttonG and mouseY in buttonH:
        image(planks, 440, 650)
        fill(255, 225, 22)
        textSize(50)
        text('Settings', 575, 705)
        main.currentScene.append(main.scenes.get("settingsScreen"))
    if ((mouseX in buttonI and mouseY in buttonJ) and (inputScreen.x == 1)):
        image(planks, 440, 750)
        fill(255, 225, 22)
        textSize(50)
        text('Resume Game', 500, 805)
        main.currentScene.pop()

def keyPressed():
    return

def keyTyped():
    return
