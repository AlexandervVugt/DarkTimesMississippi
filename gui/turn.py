import main

def setup():
    global eventText, diceText, endText
    
    eventText = 'Click on the Blue button to draw event card'
    diceText = 'Click on the Red button to throw the dices'
    endText = 'END TURN'
    
def draw():
    global rolled
    
    textAlign(CENTER, CENTER)
    background(0, 255, 0)
    fill (150, 0, 0)
    textSize(50)
    text('DarkTimesMississippi',700,70)
    
    textSize(24)
    rolled = main.gameController.getTurnInfo().getSteps() != -1
    if not rolled:
        diceButton()
    else:
        endTurnButton()
        eventButton()
    
    fill(211, 211, 211)
    rect(1179, -1, 201, 301)
    textSize(16)
    fill(0, 0, 0)
    textAlign(LEFT, CENTER)
    text(currentPlayer, 1190, 20)
    
def mousePressed():
    global main
    
    # print("x: " + str(mouseX))
    # print("y: " + str(mouseY))
    if mouseX in range(600,750):
        if mouseY in range(190,340):
            if not rolled:
                main.currentScene.append(main.scenes.get("dice"))
                # print('klikrood')
            else:
                main.gameController.nextPlayer()
                main.gameController.startTurn(None)
                refresh()
        elif mouseY in range(460, 610):
            main.currentScene.append(main.scenes.get("event"))
            # print('klikblauw')

def keyPressed():
    return

def keyTyped():
    return

def diceButton():
    global diceText
    
    fill (255, 0, 0)
    text(diceText, 700, 150)
    fill (255, 0, 0)
    square(600, 190, 150)
    
def eventButton():
    global eventText
    
    fill (0, 0, 255)
    text(eventText, 700, 420)
    fill (0, 0, 255)
    square(600, 460, 150)
    
def endTurnButton():
    global endText
    
    fill(255, 0, 0)
    text(endText, 700, 150)
    fill (255, 0, 0)
    square(600, 190, 150)

def refresh():
    global currentPlayer
    
    player = main.gameController.getPlayer()
    currentPlayer = 'Current Player: \n{}'.format(player.getName())
    print('Refreshed for player: ' + player.getName())
