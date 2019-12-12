def setup():
    global one, two, three, four, five, six, step, before, min_duration, elapsed, xMap, yMap
    
    size(1280, 720, P3D)
    # frameRate(10)
    
    one = loadImage("one.png")
    two = loadImage("two.png")
    three = loadImage("three.png")
    four = loadImage("four.png")
    five = loadImage("five.png")
    six = loadImage("six.png")
    step = 0
    before = True
    min_duration = 12
    elapsed = 0
    xMap = {
                1: [3*PI/2, 3*PI/2],
                2: [0, PI],
                3: [0, PI],
                4: [0, PI],
                5: [PI, 0],
                6: [PI/2, PI/2]
            }
    yMap = {
            1: [-1, -1],
            2: [0, PI],
            3: [PI/2, 3*PI/2],
            4: [3*PI/2, PI/2],
            5: [0, PI],
            6: [-1, -1]
            }
    
def draw():
    global before, min_duration, elapsed, step, xMap, yMap, left_angle_x, left_angle_y, right_angle_x, right_angle_y
    
    if elapsed >= min_duration:
        elapsed = 0
        step = 0
        angle = (frameCount//10)%(2*PI)
        
    
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
        if before or step == 0: rect(width/2 - 225, 3*height/4 - 50, 450, 80, 10)
        fill(0)
        textAlign(CENTER)
        textSize(32)
        buttonText = "Click here to roll the dices" if before else "Click here to continue" if step == 0 else ""
        text(buttonText, width/2, 3*height/4)
        fill(255)
        if step == 1:
            elapsed += 1
    
def drawDice(lead = 0):
    global one, two, three, four, five, six, step
    
    rotateX(step*((frameCount//10)%(2*PI)+lead))
    rotateY(step*((frameCount//10)%(2*PI)+lead))
    rotateZ(step*((frameCount//10)%(2*PI)+lead))
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
    
def mousePressed():
    global before, step, left_angle_x, left_angle_y, right_angle_x, right_angle_y, xMap, yMap
    
    if mouseX in range(width/2 - 225, width/2 + 225) and mouseY in range(3*height/4 - 50, 3*height/4 + 30):
        if before:
            left = random(7)
            right = random(7)
            left_angle_x = xMap.get(left)
            left_angle_y = yMap.get(left)
            right_angle_x = xMap.get(right)
            right_angle_y = yMap.get(right)
            elapsed = 0
            step = 1
            before = False
        elif step == 0:
            setup()
            # main.gameController.getTurnInfo().setSteps(1)
            # main.currentScene.pop()

def keyPressed():
    return

def keyTyped():
    return
