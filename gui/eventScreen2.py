import main, eventScreen3

def setup():
    global x, bg, card, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    x = 2
    bg = loadImage("background.png")
    card = loadImage("card_front.png")
    card.resize(800, 400)
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(1190, 1290)
    buttonD = range(475, 525)
    buttonE = range(150, 250)
    buttonF = range(475, 525)
    
def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill(150, 0, 0)
    textSize(75)
    text('Event Screen', 695, 200)
    
    fill(0, 0, 0)
    rect(0, 0, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('BACK', 50, 35)
    if ((mouseX in buttonA) and (mouseY in buttonB)):
        fill(100, 100, 100)
        rect(0, 0, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 50, 35)
        
    image(card, 295, 300)
    
    fill(0, 0, 0)
    textSize(20)
    textAlign(CENTER, LEFT)
    if x == 2:
        text("An amateurish bandit robbed thine farm whilst \nthee were adventuring! \nYou lose 1 wheat out of your farm stock.", 705, 475)
    if x == 3:
        text("A bandit robbed thine farm whilst thee were adventuring! \nYou lose 2 wheat out of your farm stock.", 705, 475)
    if x == 4:
        text("A plague roams the lands, the harvest doesn't look good. \nNot much wheat whill be left for thine journey. \nAt thine next journey to the market, \nthou shall carry no more than 8 wheat aboard.", 705, 475)
    if x == 5:
        text("The weather and barren circumstances \nstart to take a toll on thine health. \nThou hast gotten sick, and should take some rest. \nSkip thine next 2 turns.", 705, 475)
    if x == 6:
        text("Thine boat is rotting! \nLet's hope thou won't encounter obstacles on thine journey. \nWhen encountering an obstacle, thou will lose 2 wheat.", 705, 475)
    if x == 7:
        text("Bad weather has clogged the canals. \nThou cant take any shortcuts on this journey.", 705, 475)
    if x == 8:
        text("All these travels have exhausted thee. \nSkip thine next turn upon arriving at the market.", 705, 475)
    if x == 9:
        text("The river seems peaceful, \nthou cant feel a breeze. \nAt thine next turn, \nthou shall substract 2 from the amount thee rolled.", 705, 475)
    if x == 10:
        text("One man's trash is another man's treasure. \nThou hast stumbled upon a stranded ship, \nand it has wheat aboard! \nThou receives 2 wheat, provided your boat can carry more.", 705, 475)
    if x == 11:
        text("Drowning in sight, 12 o'clock! \nThe drowning man thou has saved, \nturns out to be the shipwright's son. \nHe will reward thee generously. \nThou whill receive an enhanced vessel for thine next journey, \nfree of charge.", 705, 475)
    if x == 12:
        text("In thine dreams, a vision about thine journey appeared. \nThere are no obstacles to be seen! \nThou may ignore any obstacles thee encounters on tis journey.", 705, 475)
    if x == 13:
        text("The fertilizer thee used has greatly increasd thine harvest. \nAt thine next 3 turns, \nthou will receive 2 wheat instead of 1.", 705, 475)
    if x == 14:
        text("Thine boat has gotten into a rapid! \nTake 3 extra steps.", 705, 475)
    if x == 15:
        text("Thou hast found a sea mine to leave behind for thine opponents. \nThou may place the sea mine obstacle on the board.", 705, 475)
    if x == 16:
        text("Thou hast found a bear trap to leave behind for thine opponents. \nThou may place the bear trap obstacle on the board.",705, 475)
    if x == 17:
        text("Thine boat has hit something! \nWater is leaking into the boat through a small hole. \nThou lost a quarter of thine load.", 705, 475)
    if x == 18:
        text("Thine boat has bumped into a small rock! \nWater is leaking into the boat rapidly. \nThou lost half thine load, \nand shall skip thine next turn \nto get rid of the water inside the boat.", 705, 475)
    if x == 19:
        text("Thine vessel has collided with a rock and sunk! \nThou lost thine boat and all load aboard.", 705, 475)
    if x == 20:
        text("An amateurish bandit attempted to mug you. \nThe poor fool. \nTake 3 extra steps and skip thine next turn.", 705, 475)
    if x == 21:
        text("Thou hast been mugged by a bandit! \nThou hast lost half thine load.", 705, 475)
    if x == 22:
        text("Thou hast been robbed by an ambitious bandit! \nThou hast lost thine ship and it's load.", 705, 475)
    if x == 23:
        text("An ambush! \nThine boat is stopped by a mob of savage bandits! \nThou hast jumped overboard and swum away \nto save thine dear life. \nThou hast lost thine ship and its load.", 705, 475)
    if x == 24:
        text("Thou are being extorted by a criminal! \nGive up all thine wheat aboard, \nor pay him off with 10 dollars. \nIn the latter case, \n the criminal will extort a player of thine choosing \nfor half their load or 5 dollars.", 705, 475)
    if x == 25:
        text("At the side of the river thou sees an old farmer \nwith an offer thou can't refuse. \nThe farmer offers you 2 wheat in exchange for 1 dollar, \nup to 10 wheat.", 705, 475)
    if x == 26:
        text("Whilst taking a break, \nthou has found a purse! \nThou receives 5 dollars.", 705, 475)
    if x == 27:
        text("It's raining heavily, and thine wheat has gotten wet. \nThou hast lost 1 wheat.", 705, 475)
    if x == 28:
        text("Thou sees a man drowning in the river. \nSave him: the man thanked thee with 3 dollars. \nSkip thine next turn. Keep going: pull another card.", 705, 475)
    
    fill(0, 0, 0)
    rect(1190, 475, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('NEXT', 1240, 510)
    if ((mouseX in buttonC) and (mouseY in buttonD)):
        fill(100, 100, 100)
        rect(1190, 475, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('NEXT', 1240, 510)
    
    fill(0, 0, 0)
    rect(150, 475, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('BACK', 200, 510)
    if ((mouseX in buttonE) and (mouseY in buttonF)):
        fill(100, 100, 100)
        rect(150, 475, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 200, 510)
    
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD)) or ((mouseX in buttonE) and (mouseY in buttonF))):
        cursor(HAND)
    else:
        cursor(ARROW)
        
def mousePressed():
    global x, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    if mouseX in buttonA and mouseY in buttonB:
        x = 2
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        x = x + 1
        if x > 28:
            main.currentScene.pop()
            main.currentScene.append(main.scenes.get("eventScreen3"))
            x = 28
    if mouseX in buttonE and mouseY in buttonF:
        x = x - 1
        if x < 2:
            main.currentScene.pop()
            main.currentScene.append(main.scenes.get("eventScreen"))
            x = 2
