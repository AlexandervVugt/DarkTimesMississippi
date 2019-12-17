def setup():
    global bg
    bg = loadImage("background.png")

def draw():
    size(1440, 900)
    image(bg, 0, 0)
    
    fill (150, 0, 0)
    textSize(75)
    text('DarkTimesMississippi', 300, 200)
    
    fill(0, 0, 0)
    rect(450, 350, 500, 75)
    fill(255, 255, 255)
    textSize(50)
    text('New Game', 575, 405)
    
    fill(0, 0, 0)
    rect(450, 450, 500, 75)
    fill(255, 255, 255)
    textSize(50)
    text('Manual & Rules', 520, 505)
    
    fill(0, 0, 0)
    rect(450, 550, 500, 75)
    fill(255, 255, 255)
    textSize(50)
    text('Event Cards', 550, 605)
    
