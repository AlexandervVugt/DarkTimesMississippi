add_library('sound')
import main

def setup():
    global bg, volumeON, volumeOFF, s, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    bg = loadImage("background.png")
    volumeON = loadImage("volumeON.png")
    volumeON.resize(100, 100)
    volumeOFF = loadImage("volumeOFF.png")
    volumeOFF.resize(100, 100)
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(500, 600)
    buttonD = range(500, 600)
    buttonE = range(700, 800)
    buttonF = range(500, 600)
    
def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill(150, 0, 0)
    textSize(75)
    text('Settings', 525, 200)
    
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
        
    image(volumeON, 500, 500)
    image(volumeOFF, 700, 500)
    
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD)) or ((mouseX in buttonE) and (mouseY in buttonF))):
        cursor(HAND)
    else:
        cursor(ARROW)
        
def mousePressed():
    global s, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    if mouseX in buttonA and mouseY in buttonB:
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
    if mouseX in buttonC and mouseY in buttonD:
        gui.enable_sound()
    if mouseX in buttonE and mouseY in buttonF:
        gui.mute_sound()
