

def setup():
    global players, input, title
    fullScreen()
    players = []
    input = ""
    title = "Please enter the names of the players who will play."
    
def draw():
    global players, input, title
    background(0, 255, 0)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(255)
    text(title, width/2, height/8)
    if len(players) < 4:
        rect(width/4, height/4 + len(players)*100, width/2, 100)
        fill(0)
        text(input, width/4, height/4 + len(players)*100, width/2, 100)
    for x in range(0, len(players)):
        fill(255)
        text(players[x], width/4, height/4 + x*100, width/2, 100)
        
def keyTyped():
    global input, players
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if len(players) == 4:
        return
    if key == ENTER or key == RETURN or key == BACKSPACE:
        return
    if key in alp:
        input += key
    
def keyPressed():
    global players, input, title
    if len(players) == 4:
        return
    if key == ENTER or key == RETURN:
        players.append(input)
        input = ""
        if len(players) == 4:
            title = "Players:"
    elif key == BACKSPACE:
        input = input[:-1]
