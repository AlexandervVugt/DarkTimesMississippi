import main

def setup():
    global bg, wood, font, buttonA, buttonB, buttonC, buttonD
    bg = loadImage("background.png")
    wood = loadImage("woodtexture.png")
    wood.resize(600, 450)
    font = loadFont('BanglaMN-48.vlw')
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(890, 990)
    buttonD = range(650, 700)
    
def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill(150, 0, 0)
    textSize(75)
    textFont(font, 75)
    text('Manual & Rules', 375, 200)
    
    fill(0, 0, 0)
    rect(0, 0, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('BACK', 10, 35)
    if ((mouseX in buttonA) and (mouseY in buttonB)):
        fill(100, 100, 100)
        rect(0, 0, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 10, 35)
    
    image(wood, 390, 250)
    
    fill(217, 216, 114)
    textSize(17)
    text('The story behind this board game stems from the rural areas \nnext to the Mississippi river, near the city of New Orleans, \nLouisiana (USA). \nThe farmers in this area had a tradition to prove \ntheir manliness. \nThis tradition involved young men coming of age, \nwho would set sail for the city of New Orleans with goods \nto sell, on a self-made boat. \nWhile thee play this game for amusement, \nthe journey to New Orleans was never without dangers. \nAll sorts of threats were waiting for travellers, \nand more then once a sailer did not return from their journey. \nFor those who did return, awaited fortune and respect from the elderly. \nGo now, those brave enough, set sail for fortune, \nand glory shall await thou who returns before all others!', 395, 270)

    fill(0, 0, 0)
    rect(890, 650, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('NEXT', 905, 685)
    if ((mouseX in buttonC) and (mouseY in buttonD)):
        fill(100, 100, 100)
        rect(890, 650, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('NEXT', 905, 685)
    
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD))):
        cursor(HAND)
    else:
        cursor(ARROW)

def mousePressed():
    global buttonA, buttonB, buttonC, buttonD
    if mouseX in buttonA and mouseY in buttonB:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules2"))
