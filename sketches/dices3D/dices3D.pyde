def setup():
    global six
    
    size(1280, 720, P3D)
    frameRate(10)
    
    one = loadImage("one.png")
    two = loadImage("two.png")
    three = loadImage("three.png")
    four = loadImage("four.png")
    five = loadImage("five.png")
    six = loadImage("six.png")
    
def draw():
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
    global six
    
    rotateX(frameCount%(2*PI)+lead)
    rotateY(frameCount%(2*PI)+lead)
    rotateZ(frameCount%(2*PI)+lead)
    box(150)
    pushMatrix()
    translate(-75, -75, 75)
    image(six, 0, 0, 150, 150)
    popMatrix()
