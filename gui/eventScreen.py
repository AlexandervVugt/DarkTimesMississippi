import main

def setup():
    global bg, card, buttonA, buttonB, buttonC, buttonD
    bg = loadImage("background.png")
    card = loadImage("card_front.png")
    card.resize(800, 400)
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
    
    text("A violent storm sets, a tornado appears! \nShall thou risk travelling further? \nContinue (and lose 2 wheat) or skip thine next turn.", 705, 475)
    
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
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("eventScreen2"))
