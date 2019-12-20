import main

def setup():
    global bg, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    bg = loadImage("background.png")
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(890, 990)
    buttonD = range(650, 700)
    buttonE = range(390, 490)
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
    text('The board features a one way river towards the market \nof New Orleans. To get back to thine farm, \nthou shall use either of two featured one way paths. \nAll players start the game with 10 units of wheat and 2 dollars. \nAt the start of every round, excluding the first round, \nall players receive 1 unit of wheat at their farm. \nTo win, thou shall acquire 30 dollars, and return to thine farm. \nEvery player has three recourse piles: \n- Thou shall store thine wheat at the farm. \n- Thou shall store thine money in the safe. \n- Thou shall store thine wheat for selling in the boat.', 395, 270)
    
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
        main.currentScene.append(main.scenes.get("manual_rules3"))
    if mouseX in buttonE and mouseY in buttonF:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules"))
