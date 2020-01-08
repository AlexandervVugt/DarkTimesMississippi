import main

def setup():
    global bg, planks, plankslight, font, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH
    bg = loadImage("background.png")
    planks = loadImage("woodenplanks.png")
    planks.resize(500, 75)
    plankslight = loadImage("woodenplankslight.png")
    plankslight.resize(500, 75)
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
    image(bg, 0, 0)
    
    textAlign(LEFT, LEFT)
    
    fill (150, 0, 0)
    textSize(75)
    textFont(font, 75)
    text('DarkTimesMississippi', 275, 200)
    
    image(plankslight, 450, 350)
    fill(210, 180, 140)
    textSize(50)
    text('New Game', 555, 405)
    if ((mouseX in buttonA) and (mouseY in buttonB)):
        image(planks, 450, 350)
        fill(210, 180, 140)
        textSize(50)
        text('New Game', 555, 405)
    
    image(plankslight, 450, 450)
    fill(210, 180, 140)
    textSize(50)
    text('Manual & Rules', 490, 505)
    if ((mouseX in buttonC) and (mouseY in buttonD)):
        image(planks, 450, 450)
        fill(210, 180, 140)
        textSize(50)
        text('Manual & Rules', 490, 505)
    
    image(plankslight, 450, 550)
    fill(210, 180, 140)
    textSize(50)
    text('Event Cards', 530, 605)
    if ((mouseX in buttonE) and (mouseY in buttonF)):
        image(planks, 450, 550)
        fill(210, 180, 140)
        textSize(50)
        text('Event Cards', 530, 605)
        
    image(plankslight, 450, 650)
    fill(210, 180, 140)
    textSize(50)
    text('Settings', 585, 705)
    if ((mouseX in buttonG) and (mouseY in buttonH)):
        image(planks, 450, 650)
        fill(217, 216, 114)
        textSize(50)
        text('Settings', 585, 705)
        
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD)) or ((mouseX in buttonE) and (mouseY in buttonF)) or ((mouseX in buttonG) and (mouseY in buttonH))):
        cursor(HAND)
    else:
        cursor(ARROW)

def mousePressed():
    global buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH
    if mouseX in buttonA and mouseY in buttonB:
        image(plankslight, 450, 350)
        fill(217, 216, 114)
        textSize(50)
        text('New Game', 555, 405)
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("inputScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        image(plankslight, 450, 450)
        fill(217, 216, 114)
        textSize(50)
        text('Manual & Rules', 490, 505)
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules"))
    if mouseX in buttonE and mouseY in buttonF:
        image(plankslight, 450, 550)
        fill(217, 216, 114)
        textSize(50)
        text('Event Cards', 530, 605)
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("eventScreen"))
    if mouseX in buttonG and mouseY in buttonH:
        image(plankslight, 450, 650)
        fill(217, 216, 114)
        textSize(50)
        text('Settings', 585, 705)
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("settingsScreen"))

def keyPressed():
    return

def keyTyped():
    return
