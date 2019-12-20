import main

def setup():
    global bg, buttonA, buttonB, buttonC, buttonD
    bg = loadImage("background.png")
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(890, 990)
    buttonD = range(650, 700)
    
def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill(150, 0, 0)
    textSize(75)
    text('Manual & Rules', 415, 200)
    
    fill(0, 0, 0)
    rect(0, 0, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('BACK', 20, 35)
    
    fill(255, 255, 255)
    rect(390, 250, 600, 450)
    
    fill(0, 0, 0)
    textSize(17)
    text('The story behind this board game stems from the rural areas next \nto the Mississippi river, near the city of New Orleans, Louisiana (USA). \nThe farmers in this area had a tradition to prove their manliness. \nThis tradition involved young men coming of age, \nwho would set sail for the city of New Orleans with goods to sell, \non a self-made boat. While thee play this game for amusement, \nthe journey to New Orleans was never without dangers. \nAll sorts of threats were waiting for travellers, \nand more then once a sailer did not return from their journey. \nFor those who did return, awaited fortune and respect from the elderly. \nGo now, those brave enough, set sail for fortune, \nand glory shall await thou who returns before all others!', 395, 270)

    fill(0, 0, 0)
    rect(890, 650, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('NEXT', 910, 685)

def mousePressed():
    global buttonA, buttonB, buttonC, buttonD
    if mouseX in buttonA and mouseY in buttonB:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules2"))
