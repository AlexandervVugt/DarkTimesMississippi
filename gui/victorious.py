import main

def setup():
    global player, title, bg, font, bgs
    
    bg = loadImage("background.png")
    bgs = loadImage("woodtexture.png")
    player = None
    title = "{} has won the game!"
    font = loadFont('BanglaMN-48.vlw')
    bgs.resize(200, 200)
    
def draw():
    global player, title, font, bg, bgs
    
    # bg = loadImage("background.png")
    # cPlace = random(20)
    textSize(50)
    textAlign(CENTER, CENTER)
    fill(255, 255, 255)
    text(title.format(player.getName()), width/2, height/2)    
    
    i = 0
    
    while i < 20 and frameCount%5 == 0:
        fill(random(255), random(255), random(255))
        ellipse(random(width), random(height), 15, 15)
        i += 1
        
    fill(255, 255, 255)
    
    playerlist = main.game.getPlayers()
    index = 0
    lilen = len(playerlist)
    while index < lilen:
        xvalue = horizontalPosition(index, lilen)
        yvalue = 100
        image(bgs, xvalue, yvalue)
        textSize(18)
        textFont(font, 30)
        fill(217, 216, 114)
        text(playerlist[index].toString(), xvalue, yvalue, 200, 200)
        index += 1
    
def horizontalPosition(index, lilen):
    center = width/2
    if index == 0:
        if lilen == 2:
            return center - 225
        elif lilen == 3:
            return center - 350
        elif lilen == 4:
            return center - 525
    elif index == 1:
        return center + 25 - (125 * (lilen - 2))
        # if lilen == 2:
        #     return center + 25
        # elif lilen == 3:
        #     return center - 100
        # elif lilen == 4:
        #     return center - 225
    elif index == 2:
        if lilen == 3:
            return center + 150
        elif lilen == 4:
            return center + 25
    elif index == 3:
        return center + 275

def mousePressed():
    # print(mouseX)
    return

def keyPressed():
    return

def keyTyped():
    return
