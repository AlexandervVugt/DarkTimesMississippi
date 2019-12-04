import main

def setup():
    global dice1, dice2, cube, active
    
    one = loadImage("one.png")
    two = loadImage("two.png")
    three = loadImage("three.png")
    four = loadImage("four.png")
    five = loadImage("five.png")
    six = loadImage("six.png")
    dice1 = six
    dice2 = six
    cube = [one, two, three, four, five, six]
    active = True
    
def draw():
    global dice1, dice2
    
    background(0, 255, 0)
    square(width/2 - 200, height/2 - 75, 150)
    square(width/2 + 50, height/2 - 75, 150)
    rect(width/2 - 225, 3*height/4 - 50, 450, 80, 10)
    fill(0)
    image(dice1, width/2 - 200, height/2 - 75, 150, 150)
    image(dice2, width/2 + 50, height/2 - 75, 150, 150)
    textAlign(CENTER)
    textSize(32)
    buttonText = "Click here to roll the dices" if active else "Click here to continue"
    text(buttonText, width/2, 3*height/4)
    fill(255)
    
def roll():
    global dice1, dice2, cube, active, result
    
    active = False
    res1 = int(random(len(cube) + 1))
    res2 = int(random(len(cube) + 1))
    dice1 = cube[res1 - 1]
    dice2 = cube[res2 - 1]
    result = res1 + res2
    
def mousePressed():
    if mouseX in range(width/2 - 225, width/2 + 225) and mouseY in range(3*height/4 - 50, 3*height/4 + 30):
        if active:
            roll()
        else:
            setup()
            main.gameController.getTurnInfo().setSteps(result)
            main.currentScene.pop()
        
def keyTyped():
    return

def keyPressed():
    return
