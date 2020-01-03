import main

def setup():
    global x, bg, card, li, buttonA, buttonB, buttonC, buttonD
    x = 1
    bg = loadImage("background.png")
    card = loadImage("card_front.png")
    card.resize(800, 400)
    li = [
          "A violent storm sets, a tornado appears! \nShall thou risk travelling further? \nContinue (and lose 2 wheat) or skip thine next turn.",
          "An amateurish bandit robbed thine farm whilst \nthee were adventuring! \nYou lose 1 wheat out of your farm stock.",
          "A bandit robbed thine farm whilst thee were adventuring! \nYou lose 2 wheat out of your farm stock.",
          "A plague roams the lands, the harvest doesn't look good. \nNot much wheat whill be left for thine journey. \nAt thine next journey to the market, \nthou shall carry no more than 8 wheat aboard.",
          "The weather and barren circumstances \nstart to take a toll on thine health. \nThou hast gotten sick, and should take some rest. \nSkip thine next 2 turns.",
          "Thine boat is rotting! \nLet's hope thou won't encounter obstacles on thine journey. \nWhen encountering an obstacle, thou will lose 2 wheat.",
          "Bad weather has clogged the canals. \nThou cant take any shortcuts on this journey.",
          "All these travels have exhausted thee. \nSkip thine next turn upon arriving at the market.",
          "The river seems peaceful, \nthou cant feel a breeze. \nAt thine next turn, \nthou shall substract 2 from the amount thee rolled.",
          "One man's trash is another man's treasure. \nThou hast stumbled upon a stranded ship, \nand it has wheat aboard! \nThou receives 2 wheat, provided your boat can carry more.",
          "Drowning in sight, 12 o'clock! \nThe drowning man thou has saved, \nturns out to be the shipwright's son. \nHe will reward thee generously. \nThou whill receive an enhanced vessel for thine next journey, \nfree of charge.",
          "In thine dreams, a vision about thine journey appeared. \nThere are no obstacles to be seen! \nThou may ignore any obstacles thee encounters on tis journey.",
          "The fertilizer thee used has greatly increasd thine harvest. \nAt thine next 3 turns, \nthou will receive 2 wheat instead of 1.",
          "Thine boat has gotten into a rapid! \nTake 3 extra steps.",
          "Thou hast found a sea mine to leave behind for thine opponents. \nThou may place the sea mine obstacle on the board.",
          "Thou hast found a bear trap to leave behind for thine opponents. \nThou may place the bear trap obstacle on the board.",
          "Thine boat has hit something! \nWater is leaking into the boat through a small hole. \nThou lost a quarter of thine load.",
          "Thine boat has bumped into a small rock! \nWater is leaking into the boat rapidly. \nThou lost half thine load, \nand shall skip thine next turn \nto get rid of the water inside the boat.",
          "Thine vessel has collided with a rock and sunk! \nThou lost thine boat and all load aboard.",
          "An amateurish bandit attempted to mug you. \nThe poor fool. \nTake 3 extra steps and skip thine next turn.",
          "Thou hast been mugged by a bandit! \nThou hast lost half thine load.",
          "Thou hast been robbed by an ambitious bandit! \nThou hast lost thine ship and it's load.",
          "An ambush! \nThine boat is stopped by a mob of savage bandits! \nThou hast jumped overboard and swum away \nto save thine dear life. \nThou hast lost thine ship and its load.",
          "Thou are being extorted by a criminal! \nGive up all thine wheat aboard, \nor pay him off with 10 dollars. \nIn the latter case, \n the criminal will extort a player of thine choosing \nfor half their load or 5 dollars.",
          "At the side of the river thou sees an old farmer \nwith an offer thou can't refuse. \nThe farmer offers you 2 wheat in exchange for 1 dollar, \nup to 10 wheat.",
          "Whilst taking a break, \nthou hast found a purse! \nThou receives 5 dollars.",
          "It's raining heavily, and thine wheat has gotten wet. \nThou hast lost 1 wheat.",
          "Thou sees a man drowning in the river. \nSave him: the man thanked thee with 3 dollars. \nSkip thine next turn. \nKeep going: pull another card.",
          "A fire purged thine crops. \nFor the next 3 turns, thou shall not receive wheat at the farm."
    ]
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(1190, 1290)
    buttonD = range(475, 525)
    
def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill(150, 0, 0)
    textSize(75)
    text('Event Screen', 695, 200)
    
    fill(0, 0, 0)
    textSize(20)
    text(li[x] x, y, width, height)
    textAlign(CENTER, LEFT)
    
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
        x = x + 1
