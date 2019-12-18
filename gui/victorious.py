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
    
    while i < 10:
        ellipse(random(width), random(height), 5, 5)
        i += 1
        
    fill(255, 255, 255)
    
    playerlist = main.game.getPlayers()
    for i in range(len(playerlist)+1):
        if i == 1:
            fill (211, 211, 211)
            image(bgs, 180, 100)
            # square(180, 100, 200);
            textSize(18)
            textFont(font, 30)
            fill (217, 216, 114)
            text(playerlist[i-1].toString(), 2, 100, 560, 200)
        if i == 2:
            fill (211, 211, 211)
            image(bgs, 480, 100)
            # square(480, 100, 200);
            textSize(18)
            textFont(font, 30)
            fill (217, 216, 114)
            text(playerlist[i-1].toString(), 2, 100, 1160, 200)
        if i == 3:
            fill (211, 211, 211)
            image(bgs, 780, 100)
            # square(780, 100, 200);
            textSize(18)
            textFont(font, 30)
            fill (217, 216, 114)
            text(playerlist[i-1].toString(), 2, 100, 1760, 200)
        if i == 4:
            fill (211, 211, 211)
            image(bgs, 1080, 100)
            # square(1080, 100, 200);
            textSize(18)
            textFont(font, 30)
            fill (217, 216, 114)
            text(playerlist[i-1].toString(), 2, 100, 2360, 200)
    
def mousePressed():
    return

def keyPressed():
    return

def keyTyped():
    return
