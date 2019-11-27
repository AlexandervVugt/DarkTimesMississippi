import main

def setup():
    global blueText, redText
    
    blueText = 'Click on the Blue button to draw event card'
    redText = 'Click on the red button to throw the dices'
    
def draw():
    global blueText, redText
    
    background(0, 255, 0)
    textSize(24)
    fill (178, 57, 91)
    text(redText, 700, 150)
    fill (255, 0, 0)
    square(600, 190, 150)
    fill (0, 0, 255)
    text(blueText, 700, 420)
    fill (0, 0, 255)
    square(600, 460, 150)
    fill (150, 0, 0)
    textSize(50)
    text('DarkTimesMisissipi',700,70)
    
def mousePressed():
    global main
    
    # print("x: " + str(mouseX))
    # print("y: " + str(mouseY))
    if mouseX in range(600,750):
        if mouseY in range(190,340):
            main.currentScene.append(main.scenes.get("dice"))
            # print('klikrood')
        elif mouseY in range(460, 610):
            main.currentScene.append(main.scenes.get("event"))
            # print('klikblauw')

def keyPressed():
    return

def keyTyped():
    return
