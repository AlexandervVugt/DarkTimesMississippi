import random

def setup():
    fullScreen()
    global dice1, dice2, cube
    one = loadImage("one.png")
    two = loadImage("two.png")
    three = loadImage("three.png")
    four = loadImage("four.png")
    five = loadImage("five.png")
    six = loadImage("six.png")
    dice1 = six
    dice2 = six
    cube = [one, two, three, four, five, six]
    
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
    buttonText = "Click here to roll the dices"
    text(buttonText, width/2, 3*height/4)
    fill(255)
    
def roll():
    global dice1, dice2, cube
    dice1 = cube[random.randrange(0, len(cube))]
    dice2 = cube[random.randrange(0, len(cube))]
    
def mousePressed():
    if mouseX in range(width/2 - 225, width/2 + 225) and mouseY in range(3*height/4 - 50, 3*height/4 + 30):
        roll()
