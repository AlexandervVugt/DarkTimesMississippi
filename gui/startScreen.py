import main, inputScreen

def setup():
    global x, logo, bg, wood, planks, planksdark, font, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH
    x = inputScreen.x
    logo = loadImage("GameLogo.png")
    bg = loadImage("background.png")
    wood = loadImage("woodtexture.png")
    wood.resize(500, 75)
    planks = loadImage("woodenplanks.png")
    planks.resize(500, 75)
    planksdark = loadImage("woodenplanksdark.png")
    planksdark.resize(500, 75)
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
    
    image(logo, 340, 50)
    
    textFont(font, 75)
    
    if x == 0:
        image(planks, 450, 350)
        fill(255, 225, 22)
        textSize(50)
        text('New Game', 555, 405)
        if ((mouseX in buttonA) and (mouseY in buttonB)):
            image(planksdark, 450, 350)
            fill(237, 206, 0)
            textSize(50)
            text('New Game', 555, 405)
    if x == 1:
        image(planks, 450, 350)
        fill(255, 225, 22)
        textSize(50)
        text('Resume Game', 510, 405)
        if ((mouseX in buttonA) and (mouseY in buttonB)):
            image(planksdark, 450, 350)
            fill(237, 206, 0)
            textSize(50)
            text('Resume Game', 510, 405)
            
    
    image(planks, 450, 450)
    fill(255, 225, 22)
    textSize(50)
    text('Manual & Rules', 490, 505)
    if ((mouseX in buttonC) and (mouseY in buttonD)):
        image(planksdark, 450, 450)
        fill(237, 206, 0)
        textSize(50)
        text('Manual & Rules', 490, 505)
    
    image(planks, 450, 550)
    fill(255, 225, 22)
    textSize(50)
    text('Event Cards', 530, 605)
    if ((mouseX in buttonE) and (mouseY in buttonF)):
        image(planksdark, 450, 550)
        fill(237, 206, 0)
        textSize(50)
        text('Event Cards', 530, 605)
        
    image(planks, 450, 650)
    fill(255, 225, 22)
    textSize(50)
    text('Settings', 585, 705)
    if ((mouseX in buttonG) and (mouseY in buttonH)):
        image(planksdark, 450, 650)
        fill(237, 206, 0)
        textSize(50)
        text('Settings', 585, 705)
        
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD)) or ((mouseX in buttonE) and (mouseY in buttonF)) or ((mouseX in buttonG) and (mouseY in buttonH))):
        cursor(HAND)
    else:
        cursor(ARROW)

def mousePressed():
    global x, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH
    if ((mouseX in buttonA and mouseY in buttonB) and (inputScreen.x == 0)):
        image(planks, 450, 350)
        fill(255, 225, 22)
        textSize(50)
        text('New Game', 555, 405)
        main.currentScene.append(main.scenes.get("inputScreen"))
    if ((mouseX in buttonA and mouseY in buttonB) and (inputScreen.x == 1)):
        image(planks, 450, 350)
        fill(255, 225, 22)
        textSize(50)
        text('Resume Game', 510, 405)
        main.currentScene.append(main.scenes.get("inputScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        image(planks, 450, 450)
        fill(255, 225, 22)
        textSize(50)
        text('Manual & Rules', 490, 505)
        main.currentScene.append(main.scenes.get("manual_rules"))
    if mouseX in buttonE and mouseY in buttonF:
        image(planks, 450, 550)
        fill(255, 225, 22)
        textSize(50)
        text('Event Cards', 530, 605)
        main.currentScene.append(main.scenes.get("eventScreen"))
    if mouseX in buttonG and mouseY in buttonH:
        image(planks, 450, 650)
        fill(255, 225, 22)
        textSize(50)
        text('Settings', 585, 705)
        main.currentScene.append(main.scenes.get("settingsScreen"))

def keyPressed():
    return

def keyTyped():
    return
