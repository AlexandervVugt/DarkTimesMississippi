def setup():
    size(1280, 720, P3D)
    frameRate(10)
    
def draw():
    #create a matrix for the first cube
    pushMatrix()
    translate(width/2 - 125, height/2)
    box(150)
    popMatrix()
    
    #create a matrix for the second cube
    pushMatrix()
    translate(width/2 + 125, height/2)
    rotateX(frameCount%(2*PI))
    rotateY(frameCount%(2*PI))
    rotateZ(frameCount%(2*PI))
    box(150)
    popMatrix()
