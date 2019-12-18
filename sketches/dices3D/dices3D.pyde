import random

def setup():
    global one, two, three, four, five, six, step, before, min_duration, elapsed, xMap, yMap, left_x_step, left_y_step, right_x_step, right_y_step, left_angle_x, left_angle_y, right_angle_x, right_angle_y
    
    size(1280, 720, P3D)
    # frameRate(10)
    
    one = loadImage("one.png")
    two = loadImage("two.png")
    three = loadImage("three.png")
    four = loadImage("four.png")
    five = loadImage("five.png")
    six = loadImage("six.png")
    step = False
    left_x_step = True
    left_y_step = True
    right_y_step = True
    right_x_step = True
    left_angle_x = 0
    left_angle_y = 0
    right_angle_x = 0
    right_angle_y = 0
    before = True
    min_duration = 12
    elapsed = 0
    xMap = {
                '1': [3*PI/2, 3*PI/2],
                '2': [0, PI],
                '3': [0, PI],
                '4': [0, PI],
                '5': [PI, 0],
                '6': [PI/2, PI/2]
            }
    yMap = {
    '1': [-1, -1],
    '2': [0, PI],
    '3': [PI/2, 3*PI/2],
    '4': [3*PI/2, PI/2],
    '5': [0, PI],
    '6': [-1, -1]
            }
    
def draw():
    global before, min_duration, elapsed, step, xMap, yMap, left_angle_x, left_angle_y, right_angle_x, right_angle_y
    
    if elapsed >= min_duration and frameCount%5 == 0:
        # elapsed = 0
        # step = 0
        angle = (frameCount//5)%(2*PI)
        if left_x_step:
            checkAngle(angle, left_angle_x, 'lx')
        if left_y_step:
            checkAngle(angle, left_angle_y, 'ly')
        if right_x_step:
            checkAngle(angle + PI, right_angle_x, 'rx')
        if right_y_step:
            checkAngle(angle + PI, right_angle_y, 'ry')
        if not left_x_step and not left_y_step and not right_x_step and not right_y_step:
            print()
            step = False
            elapsed = 0
        
    
    if frameCount%5 == 0:
        background(255)
        #create a matrix for the first cube
        pushMatrix()
        translate(width/2 - 125, height/2)
        drawDice(left_x_step, left_y_step, left_angle_x, left_angle_y, PI)
        popMatrix()
    
        #create a matrix for the second cube
        pushMatrix()
        translate(width/2 + 125, height/2)
        drawDice(right_x_step, right_y_step, right_angle_x, right_angle_y)
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
    
def drawDice(x_step, y_step, angle_x, angle_y, lead = 0):
    global one, two, three, four, five, six, step
    
    # rotateX(((frameCount//10)%(2*PI)+lead) if x_step and step else left_angle_x)
    # rotateY(((frameCount//10)%(2*PI)+lead) if y_step and step else left_angle_y)
    if step:
        if x_step:
            rotateX(((frameCount//5)%(2*PI)+lead))
        else:
            rotateX(angle_x)
        if y_step:
            rotateY(((frameCount//5)%(2*PI)+lead))
        else:
            rotateY(angle_y)
        rotateZ(((frameCount//5)%(2*PI)+lead))
    else:
        rotateX(angle_x)
        rotateY(angle_y)
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
    
def checkAngle(angle, coordinates, target):
    global left_x_step, left_y_step, right_x_step, right_y_step, left_angle_x, left_angle_y, right_angle_x, right_angle_y
    
    for coordinate in coordinates:
        leftbound = coordinate - (1.0/8.0*PI)
        rightbound = coordinate + (1.0/8.0*PI)
        if angle >= leftbound and angle <= rightbound:
            print("{} is near coordinate {}".format(angle, coordinate))
            if target == 'lx':
                left_x_step = False
                left_angle_x = angle
            elif target == 'ly':
                left_y_step = False
                left_angle_y = angle
            elif target == 'rx':
                right_x_step = False
                right_angle_x = angle
            elif target == 'ry':
                right_y_step = False
                right_angle_y = angle
        elif coordinate == -1:
            print("{} is near coordinate {}".format(angle, coordinate))
            if target == 'lx':
                left_x_step = False
                left_angle_x = angle
            elif target == 'ly':
                left_y_step = False
                left_angle_y = angle
            elif target == 'rx':
                right_x_step = False
                right_angle_x = angle
            elif target == 'ry':
                right_y_step = False
                right_angle_y = angle
        #else:
            #print("{} is not near coordinate {}".format(angle, coordinate))
    
def mousePressed():
    global before, step, left_angle_x, left_angle_y, right_angle_x, right_angle_y, xMap, yMap
    
    if mouseX in range(width/2 - 225, width/2 + 225) and mouseY in range(3*height/4 - 50, 3*height/4 + 30):
        if before:
            left = random.randrange(1, 7)
            right = random.randrange(1, 7)
            print(left)
            print(right)
            left_angle_x = xMap.get(str(left))
            left_angle_y = yMap.get(str(left))
            right_angle_x = xMap.get(str(right))
            right_angle_y = yMap.get(str(right))
            elapsed = 0
            step = True
            before = False
        elif step == 0:
            setup()
            # main.gameController.getTurnInfo().setSteps(1)
            # main.currentScene.pop()

def keyPressed():
    return

def keyTyped():
    return
