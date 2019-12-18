import main

def setup():
    global bg, buttonA, buttonB
    bg = loadImage("background.png")
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    
def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill(150, 0, 0)
    textSize(75)
    text('Manual & Rules', 400, 200)
    
    fill(0, 0, 0)
    rect(0, 0, 100, 50)
    fill(255, 255, 255)
    textSize(25)
    text('BACK', 20, 35)
    
def mousePressed():
    global buttonA, buttonB
    if mouseX in buttonA and mouseY in buttonB:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
    
