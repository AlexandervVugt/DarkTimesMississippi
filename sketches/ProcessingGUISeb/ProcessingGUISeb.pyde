#import main

def setup():
    size(900,800)
    
def draw():
    background(0, 255, 0)
    textSize(24)
    fill (178, 57, 91)
    text('Click on the red button to throw the dices',230,130)
    fill (255, 0, 0)
    square(380, 170, 150)
    fill (0, 0, 255)
    text('Click on the Blue button to draw event card',230,390)
    fill (0, 0, 255)
    square(380, 430, 150)
    fill (150, 0, 0)
    textSize(50)
    text('DarkTimesMisissipi',230,70)
    
def mousePressed():
    # print("x: " + str(mouseX))
    # print("y: " + str(mouseY))
    if mouseX in range(380,530):
        if mouseY in range(150,300):
            #main.currentScene
            print('klikrood')
        elif mouseY in range(430, 580):
            print('klikblauw')
        
    
    

    
    

    
