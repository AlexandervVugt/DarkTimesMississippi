import main, popup_modify, popup_confirm, victorious

def setup():
    global eventText, diceText, endText, bg, bgs, font, dicebttn, cardback, logo
    
    eventText = 'Click on the Blue button to draw event card'
    diceText = 'Click on the Red button to throw the dices'
    endText = 'END TURN'
    bg = loadImage("background.png")
    bgs = loadImage("woodtexture.png")
    bgs.resize(200, 200)
    font = loadFont('BanglaMN-48.vlw')
    dicebttn = loadImage("dicebttn.png")
    cardback = loadImage("card_back.png")
    logo = loadImage("GameLogo.png")
    
def draw():
    global rolled
    
    textAlign(CENTER, CENTER)
    image(bg, 0, 0)
    fill (150, 0, 0)
    textSize(50)
    image(logo, 350, 1, 700, 250)
    

    playerlist = main.game.getPlayers()
    for i in range(len(playerlist)+1):
        if i == 1:
            fill (211, 211, 211)
            image(bgs, 1, 1,)
            #square(1, 1, 200);
            textSize(18)
            textFont(font, 18)
            fill (255, 225, 22)
            text(playerlist[i-1].toString(), 2, 1, 200, 200)
        if i == 2:
            fill (211, 211, 211)
            image(bgs, 1, 210,)
            #square(1, 210, 200);
            textSize(18)
            textFont(font, 18)
            fill (255, 225, 22)
            text(playerlist[i-1].toString(), 2, 100, 200, 420)
        if i == 3:
            fill (211, 211, 211)
            image(bgs, 1, 420,)
            #square(1, 420, 200);
            textSize(18)
            textFont(font, 18)
            fill (255, 225, 22)
            text(playerlist[i-1].toString(), 2, 200, 200, 640)
        if i == 4:
            fill (211, 211, 211)
            image(bgs, 1, 630,)
            #square(1, 630, 200);
            textSize(18)
            textFont(font, 18)
            fill (255, 225, 22)
            text(playerlist[i-1].toString(), 2, 300, 200, 860)
        
        cursor(ARROW)

                
        
    textSize(24)
    rolled = main.gameController.getTurnInfo().getSteps() != -1
    if not rolled:
        diceButton()
    else:
        endTurnButton()
        eventButton()
    
    image(bgs, 1080, 1, 360, 320)
    textSize(28)
    fill(255, 225, 22)
    textAlign(TOP)
    text(player.toString(), width-340, 20, width, 320)
    buttons()
    
def mousePressed():
    global main
    
    print("x: " + str(mouseX))
    print("y: " + str(mouseY))
    if not rolled and mouseX in range(width/2 - 75, width/2 + 75) and mouseY in range(height/2 - 75, height/2 + 75):
        main.currentScene.append(main.scenes.get("dice"))
    elif mouseX in range(width/2-150, width/2+150):
        if mouseY in range(height/4+20, height/4+120):
            main.gameController.nextPlayer()
            main.gameController.startTurn(None)
            refresh()
        elif mouseY in range(height/2-81, height/2+81):
            main.currentScene.append(main.scenes.get("event"))
    if mouseX in range(1360, 1420):
        if player.hasBoat():
            if mouseY in range(140, 175):
                # sell button mechanism
                popup_confirm.action = player.sellBoat
                main.currentScene.append(main.scenes.get("popup_confirm"))
            elif mouseY in range(220, 255):
                # load button
                popup_modify.action = player.getBoat().load
                main.currentScene.append(main.scenes.get("popup_modify"))
        if mouseY in range(55, 90):
            # gold button
            popup_modify.action = player.mutateGold
            main.currentScene.append(main.scenes.get("popup_modify"))
        elif mouseY in range(95, 130):
            # wheat button
            popup_modify.action = player.mutateWheat
            main.currentScene.append(main.scenes.get("popup_modify"))
    elif mouseX in range(1250, 1350) and mouseY in range(140, 175) and player.hasBoat():
        # delete boat button 1250, 140, 100, 35
        popup_confirm.action = player.destroyBoat
        main.currentScene.append(main.scenes.get("popup_confirm"))
    if not player.hasBoat() and mouseX in range(1340, 1420) and mouseY in range(140, 175):
            player.assignBoat()
            main.gameController.nextPlayer()
            main.gameController.startTurn(None)
            refresh()
    if player.getGold() >= 30 and mouseX in range(width-340, width-20) and mouseY in range(295, 320):
        main.currentScene.pop()
        victorious.player = player
        main.currentScene.append(main.scenes.get("victorious"))
            
def keyPressed():
    return

def keyTyped():
    return

def diceButton():
    global diceText
    
    image(dicebttn, width/2 - 75, height/2 - 75, 150, 150)
    # fill (255, 0, 0)
    # text(diceText, 700, 150)
    # fill (255, 0, 0)
    # square(600, 190, 150)
    
def eventButton():
    global cardback
    
    pushMatrix()
    translate(width/2, height/2)
    image(cardback, -150, -81, 300, 162)
    popMatrix()
    
    # fill (0, 0, 255)
    # text(eventText, 700, 420)
    # fill (0, 0, 255)
    # square(600, 460, 150)
    
    
def endTurnButton():
    global endText
    
    fill (100 if mouseX in range(width/2-150, width/2+150) and mouseY in range(height/4+20, height/4+120) else 0)
    rect(width/2-150, height/4+20, 300, 100, 10)
    fill(255)
    text(endText, width/2-150, height/4+20, 300, 100)
    
def buttons():
    global player

    textAlign(CENTER, CENTER)
    editButton(55)
    editButton(95)
    if player.hasBoat():
        editButton(220)
        
        fill(100 if mouseX in range(1360, 1420) and mouseY in range(140, 175) else 0)
        rect(1360, 140, 60, 35)
        textSize(15)
        fill(255)
        text('SELL', 1365, 145, 50, 25)
        
        fill(100 if mouseX in range(1250, 1350) and mouseY in range(140, 175) else 0)
        rect(1250, 140, 100, 35)
        textSize(15)
        fill(255)
        text('DESTROY', 1255, 145, 90, 25)
    else:
        fill(100 if mouseX in range(1340, 1420) and mouseY in range(140, 175) else 0)
        rect(1340, 140, 80, 35)
        textSize(15)
        fill(255)
        text('CREATE', 1345, 145, 70, 25)
        
        fill(100 if mouseX in range(1250, 1330) and mouseY in range(140, 175) else 0)
        rect(1250, 140, 80, 35)
        textSize(15)
        fill(255)
        text('BUY', 1255, 145, 70, 25)
        
    if player.getGold() >= 30:
        fill(100 if mouseX in range(width-360, width) and mouseY in range(295, 320) else 0)
        rect(width-360, 295, 360, 25)
        textSize(15)
        fill(255)
        textAlign(TOP, CENTER)
        text('Farm reached, VICTORIOUS!', width-350, 300, 340, 20)
    
def editButton(y):
    fill(100 if mouseX in range(1360, 1420) and mouseY in range(y, y+35) else 0)
    rect(1360, y, 60, 35)
    textSize(15)
    fill(255)
    text('EDIT', 1365, y + 5, 50, 25)

def refresh():
    global player
    
    player = main.gameController.getPlayer()
