def setup():
    global player, title, bg
    
    bg = loadImage("background.png")
    player = None
    title = "{} has won the game!"
    
def draw():
    global player, title
    
    bg = loadImage("background.png")
    textSize(50)
    textAlign(CENTER, CENTER)
    fill(255, 255, 255)
    text(title.format(player.getName()), width/2, height/2)
    
def mousePressed():
    return

def keyPressed():
    return

def keyTyped():
    return
