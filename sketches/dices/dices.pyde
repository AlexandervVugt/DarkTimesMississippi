def setup():
    fullScreen()
    global one, two, three, four, five, six, dice1, dice2
    one = loadImage("one.png")
    two = loadImage("two.png")
    three = loadImage("three.png")
    four = loadImage("four.png")
    five = loadImage("five.png")
    six = loadImage("six.png")
    dice1 = six
    dice2 = six
    
def draw():
    global dice1, dice2
    background(0, 255, 0)
    square(width/2 - 200, height/2 - 75, 150)
    square(width/2 + 50, height/2 - 75, 150)
    image(dice1, width/2 - 200, height/2 - 75, 150, 150)
    image(dice2, width/2 + 50, height/2 - 75, 150, 150)
    
def roll():
    global dice1, dice2, one, two, three, four, five, six
    
