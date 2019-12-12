def setup():
    global one, two, three, four, five, six
    
    size(1280, 720, P3D)
    
    one = loadImage("one.png")
    two = loadImage("two.png")
    three = loadImage("three.png")
    four = loadImage("four.png")
    five = loadImage("five.png")
    six = loadImage("six.png")
    
def draw():
    if frameCount%10 == 0:
        background(255)
        #create a matrix for the first cube
        pushMatrix()
        translate(width/2 - 125, height/2)
        drawDice(PI)
        popMatrix()
    
        #create a matrix for the second cube
        pushMatrix()
        translate(width/2 + 125, height/2)
        drawDice()
        popMatrix()
    
def drawDice(lead = 0):
    global one, two, three, four, five, six
    
    rotateX((frameCount/10)%(2*PI)+lead)
    rotateY((frameCount/10)%(2*PI)+lead)
    rotateZ((frameCount/10)%(2*PI)+lead)
    # box(150)
    pushMatrix()
    translate(-75, -75, 75)
    image(two, 0, 0, 150, 150)
    translate(0, 0, -150)
    image(five, 0, 0, 150, 150)
    popMatrix()
    pushMatrix()
    translate(-75, -75, -75)
    rotateX(PI/2)
    image(six, 0, 0, 150, 150)
    translate(0, 0, -150)
    image(one, 0, 0, 150, 150)
    popMatrix()
    #3 links, 4 rechts
    pushMatrix()
    rotateY(PI/2)
    translate(-75, -75, 75)
    image(four, 0, 0, 150, 150)
    translate(0, 0, -150)
    image(three, 0, 0, 150, 150)
    popMatrix()
