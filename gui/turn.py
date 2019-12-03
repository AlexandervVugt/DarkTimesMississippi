import main, popup_modify

def setup():
    global eventText, diceText, endText
    
    eventText = 'Click on the Blue button to draw event card'
    diceText = 'Click on the Red button to throw the dices'
    endText = 'END TURN'
    
def draw():
    global rolled, player
    
    textAlign(CENTER, CENTER)
    background(0, 255, 0)
    fill (150, 0, 0)
    textSize(50)
    text('DarkTimesMississippi',700,70)

    #Square Player 1
    square1 = square(1, 1, 200);
    #Square Player 2
    square2 = square(1, 210, 200);
    #Square Player 3
    square3 = square(1, 420, 200);
    #Square Player 4
    square4 = square(1, 630, 200);
    for i in range(4):
        #do something
        something = 'something'
    
    for i in range 1:
        if len(main.game.getPlayers()) == 2
        print (square1,square2)
        if len(main.game.getPlayers()) == 3
        print (square1,square2,square3)
        if len(main.game.getPlayers()) == 4
        print (square1,square2,square3,square4)
        
    
    
    
    textSize(24)
    rolled = main.gameController.getTurnInfo().getSteps() != -1
    if not rolled:
        diceButton()
    else:
        endTurnButton()
        eventButton()
        
    fill(255)
    square(width-100, height-100, 100)
    
    fill(211, 211, 211)
    rect(width-350, 0, 350, 310)
    textSize(25)
    fill(0, 0, 0)
    textAlign(TOP)
    text(player.toString(), width-350, 0, width, 500)
    fill(255, 255, 255)
    rect(1295, 42, 60, 20)
    textSize(15)
    fill(0, 0, 0)
    text('EDIT', 1309, 59)
    
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
        elif mouseY in range(460, 610) and rolled:
            main.currentScene.append(main.scenes.get("event"))
            # print('klikblauw')
    elif mouseX in range(width-100, width) and mouseY in range(height-100, height):
        popup_modify.action = main.gameController.getPlayer().mutateGold
        main.currentScene.append(main.scenes.get("popup_modify"))

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
    global player
    
    player = main.gameController.getPlayer()
