import main

def setup():
    global bg, buttonA, buttonB, buttonC, buttonD
    bg = loadImage("background.png")
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(390, 490)
    buttonD = range(650, 750)
    
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
    if ((mouseX in buttonA) and (mouseY in buttonB)):
        fill(100, 100, 100)
        rect(0, 0, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 20, 35)
    
    fill(255, 255, 255)
    rect(390, 250, 600, 450)
    
    fill(0, 0, 0)
    textSize(17)
    text('- Thou shall load thee ship before throwing the dices. \n- The spots with a question mark are event spots. \n- Thou shall execute an event when landing on an event spot, \n  even if this is by being stopped by an obstacle. \n- There is no limit on the amount of wheat that can be stored at the farm. \n- After throwing the dices, thou shall execute them.', 395, 270)
    
    fill(0, 0, 0)
    rect(390, 650, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('BACK', 410, 685)
    if ((mouseX in buttonC) and (buttonD)):
        fill(100, 100, 100)
        rect(390, 650, 100, 50)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 410, 685)
    
def mousePressed():
    if mouseX in buttonA and mouseY in buttonB:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("manual_rules3"))
