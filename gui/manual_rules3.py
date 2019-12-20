import main

def setup():
    global bg, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    bg = loadImage("background.png")
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(390, 490)
    buttonD = range(650, 750)
    buttonE = range(890, 990)
    buttonF = range(650, 700)
    
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
    text('- Thou shall not overload thine boat with more than 10 units of wheat. \n- Thou shall skip one turn to build a new boat. \n- Thou shall stop moving upon reaching the market or farm, \n   discarding any leftover steps. \n- Thou shall pay 3 dollars for an improved boat, featuring: \n   - An extra capacity for 5 units of wheat; \n   - Leave the farm without skipping a turn; \n   - Use leftover steps from reaching the farm immediately. \n- Thou shall place an obstacle in the turn thee received it. \n- Thou will never lose acquired money, other than spending it. \n- Thou can buy the improved boat on any occasion. \n- Thou can wait turns only at the farm.', 395, 270)
    
    fill(0, 0, 0)
    rect(890, 650, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('NEXT', 910, 685)
    
    fill(0, 0, 0)
    rect(390, 650, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('BACK', 410, 685)
    
def mousePressed():
    global buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    if mouseX in buttonA and mouseY in buttonB:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules2"))
    if mouseX in buttonE and mouseY in buttonF:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules4"))
    
