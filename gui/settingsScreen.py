add_library('sound')
import main

def setup():
    global bg, planks, woodsmall, woodsmalldark, volumeON, volumeONdark, volumeOFF, volumeOFFdark, s, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    bg = loadImage("background.png")
    planks = loadImage("woodenplanks.png")
    planks.resize(500, 75)
    woodsmall = loadImage("woodtexturesmall.png")
    woodsmall.resize(100, 50)
    woodsmalldark = loadImage("woodtexturesmalldark.png")
    woodsmalldark.resize(100, 50)
    volumeON = loadImage("volumeON.png")
    volumeON.resize(50, 50)
    volumeONdark = loadImage("volumeONdark.png")
    volumeONdark.resize(50, 50)
    volumeOFF = loadImage("volumeOFF.png")
    volumeOFF.resize(50, 50)
    volumeOFFdark = loadImage("volumeOFFdark.png")
    volumeOFFdark.resize(50, 50)
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(800, 850)
    buttonD = range(365, 415)
    buttonE = range(875, 925)
    buttonF = range(365, 415)
    
def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill(255, 225, 22)
    textSize(75)
    text('Settings', 525, 200)
    
    image(woodsmall, 0, 0)
    fill(255, 225, 22)
    textSize(25)
    text('BACK', 10, 35)
    if ((mouseX in buttonA) and (mouseY in buttonB)):
        image(woodsmalldark, 0, 0)
        fill(237, 206, 0)
        textSize(25)
        text('BACK', 10, 35)
    
    image(planks, 450, 350)
    textSize(50)
    text("Music:", 465, 405)
    
    image(volumeON, 800, 365)
    if ((mouseX in buttonC) and (mouseY in buttonD)):
        image(volumeONdark, 800, 365)
        
    image(volumeOFF, 875, 365)
    if ((mouseX in buttonE) and (mouseY in buttonF)):
        image(volumeOFFdark, 875, 365)
    
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD)) or ((mouseX in buttonE) and (mouseY in buttonF))):
        cursor(HAND)
    else:
        cursor(ARROW)
        
def mousePressed():
    global s, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    if mouseX in buttonA and mouseY in buttonB:
        image(woodsmall, 0, 0)
        fill(255, 225, 22)
        textSize(25)
        text('BACK', 10, 35)
        main.currentScene.pop()
    if mouseX in buttonC and mouseY in buttonD:
        main.enable_sound()
    if mouseX in buttonE and mouseY in buttonF:
        main.disable_sound()
        
def keyPressed():
    return

def keyTyped():
    return
