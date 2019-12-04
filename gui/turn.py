import main, popup_modify, popup_confirm, victorious

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
    rect(width-350, 0, 350, 310)
    textSize(25)
    fill(0, 0, 0)
    textAlign(TOP)
    text(player.toString(), width-350, 0, width, 500)
    buttons()
    
def mousePressed():
    global main, player
    
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
    elif mouseX in range(1300, 1345):
        if player.hasBoat():
            if mouseY in range(120, 140):
                # sell button mechanism
                popup_confirm.action = player.sellBoat
                main.currentScene.append(main.scenes.get("popup_confirm"))
            elif mouseY in range(195, 215):
                # load button
                popup_modify.action = player.getBoat().load
                main.currentScene.append(main.scenes.get("popup_modify"))
        if mouseY in range(45, 65):
            # gold button
            popup_modify.action = player.mutateGold
            main.currentScene.append(main.scenes.get("popup_modify"))
        elif mouseY in range(80, 100):
            # wheat button
            popup_modify.action = player.mutateWheat
            main.currentScene.append(main.scenes.get("popup_modify"))
    elif mouseX in range(1350, 1425) and mouseY in range(120, 140) and player.hasBoat():
        # delete boat button
        popup_confirm.action = player.destroyBoat
        main.currentScene.append(main.scenes.get("popup_confirm"))
    if not player.hasBoat() and mouseX in range(1300, 1365) and mouseY in range(120, 140):
        main.gameController.getPlayer().assignBoat()
        main.gameController.nextPlayer()
        main.gameController.startTurn(None)
        refresh()
    if player.getGold() >= 30 and mouseX in range(width-350, width) and mouseY in range(290, 310):
        main.currentScene.pop()
        victorious.player = player
        main.currentScene.append(main.scenes.get("victorious"))
            
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
    
def buttons():
    global player

    editButton(45.0)
    editButton(80.0)
    if player.hasBoat():
        editButton(195.0)
        
        fill(255, 255, 255)
        rect(1300, 120, 45, 20)
        textSize(15)
        fill(0, 0, 0)
        text('SELL', 1305, 120, 1340, 140)
        
        fill(255, 255, 255)
        rect(1350, 120, 75, 20)
        textSize(15)
        fill(0, 0, 0)
        text('DESTROY', 1355, 120, 1420, 140)
    else:
        fill(255, 255, 255)
        rect(1300, 120, 65, 20)
        textSize(15)
        fill(0, 0, 0)
        text('CREATE', 1305, 120, 1360, 140)
    if player.getGold() >= 30:
        fill(255, 255, 255)
        rect(width-350, 290, 350, 20)
        textSize(15)
        fill(0, 0, 0)
        text('Farm reached, VICTORIOUS!', width-275, 290, width, 310)
    
def editButton(y):
    fill(255, 255, 255)
    rect(1300, y, 45, 20)
    textSize(15)
    fill(0, 0, 0)
    text('EDIT', 1305, y, 1340, y+20)

def refresh():
    global player
    
    player = main.gameController.getPlayer()
