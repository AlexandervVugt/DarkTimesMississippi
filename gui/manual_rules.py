import main

def setup():
    global x, bg, wood, planks, plankslight, font, li, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF
    x = 0
    bg = loadImage("background.png")
    wood = loadImage("woodtexture.png")
    wood.resize(600, 450)
    planks = loadImage("woodenplanks.png")
    planks.resize(100, 50)
    plankslight = loadImage("woodenplankslight.png")
    plankslight.resize(100, 50)
    font = loadFont('BanglaMN-48.vlw')
    li = [
          "The story behind this board game stems from the rural areas \nnext to the Mississippi river, near the city of New Orleans, \nLouisiana (USA). \nThe farmers in this area had a tradition to prove \ntheir manliness. \nThis tradition involved young men coming of age, \nwho would set sail for the city of New Orleans with goods \nto sell, on a self-made boat. \nWhile thee play this game for amusement, \nthe journey to New Orleans was never without dangers. \nAll sorts of threats were waiting for travellers, \nand more then once a sailer did not return from their journey. \nFor those who did return, awaited fortune \nand respect from the elderly. \nGo now, those brave enough, set sail for fortune, \nand glory shall await thou who returns before all others!",
          "The board features a one way river towards the market \nof New Orleans. To get back to thine farm, \nthou shall use either of two featured one way paths. \nAll players start the game with 10 units of wheat and 2 dollars. \nAt the start of every round, excluding the first round, \nall players receive 1 unit of wheat at their farm. \nTo win, thou shall acquire 30 dollars, and return to thine farm. \nEvery player has three recourse piles: \n- Thou shall store thine wheat at the farm. \n- Thou shall store thine money in the safe. \n- Thou shall store thine wheat for selling in the boat. \n\n- Thou shall not overload thine boat \n   with more than 10 units of wheat. \n- Thou shall skip one turn to build a new boat. \n- Thou shall stop moving upon reaching the market or farm, \n   discarding any leftover steps.",
          "- Thou shall pay 3 dollars for an improved boat, featuring: \n   - An extra capacity for 5 units of wheat; \n   - Leave the farm without skipping a turn; \n   - Use leftover steps from reaching the farm immediately. \n- Thou shall place an obstacle in the turn thee received it. \n- Thou will never lose acquired money, other than spending it. \n- Thou can buy the improved boat on any occasion. \n- Thou can wait turns only at the farm. \n- Thou shall load thee ship before throwing the dices. \n- The spots with a question mark are event spots. \n- Thou shall execute an event when landing on an event spot, \n  even if this is by being stopped by an obstacle. \n- There is no limit on the amount of wheat \n   that can be stored at the farm. \n- After throwing the dices, thou shall execute them."
    ]
    buttonA = range(0, 100)
    buttonB = range(0, 50)
    buttonC = range(1125, 1225)
    buttonD = range(450, 500)
    buttonE = range(150, 250)
    buttonF = range(450, 500)
    
def draw():
    image(bg, 0, 0)
    
    fill(150, 0, 0)
    textSize(75)
    textFont(font, 75)
    text('Manual & Rules', 375, 200)
    
    image(plankslight, 0, 0)
    fill(210, 180, 140)
    textSize(25)
    text('BACK', 10, 35)
    if ((mouseX in buttonA) and (mouseY in buttonB)):
        image(planks, 0, 0)
        fill(210, 180, 140)
        textSize(25)
        text('BACK', 10, 35)
    
    image(wood, 390, 250)
    
    fill(217, 216, 114)
    textSize(17)
    text(li[x], 395, 270)
    
    if x < 2:
        image(plankslight, 1125, 450)
        fill(255, 255, 255)
        textSize(25)
        text('NEXT', 1140, 485)
        if ((mouseX in buttonC) and (mouseY in buttonD)):
            image(planks, 1125, 450)
            fill(255, 255, 255)
            textSize(25)
            text('NEXT', 1140, 485)
    
    if x > 0:
        image(plankslight, 150, 450)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 160, 485)
        if ((mouseX in buttonE) and (mouseY in buttonF)):
            image(planks, 150, 450)
            fill(255, 255, 255)
            textSize(25)
            text('BACK', 160, 485)
    
    if (((mouseX in buttonA) and (mouseY in buttonB)) or ((mouseX in buttonC) and (mouseY in buttonD) and (x < 2)) or ((mouseX in buttonE) and (mouseY in buttonF) and (x > 0))):
        cursor(HAND)
    else:
        cursor(ARROW)

def mousePressed():
    global x, buttonA, buttonB, buttonC, buttonD
    if mouseX in buttonA and mouseY in buttonB:
        image(plankslight, 0, 0)
        fill(255, 255, 255)
        textSize(25)
        text('BACK', 10, 35)
        main.currentScene.pop()
        main.currentScene.append(main.scenes.get("startScreen"))
        x = 0
    if mouseX in buttonC and mouseY in buttonD:
        if x < 2:
            image(plankslight, 1125, 450)
            fill(255, 255, 255)
            textSize(25)
            text('NEXT', 1140, 485)
        x = x + 1
        if x == 3:
            x = 2
    if mouseX in buttonE and mouseY in buttonF:
        if x > 0:
            image(plankslight, 150, 450)
            fill(255, 255, 255)
            textSize(25)
            text('BACK', 160, 485)
        x = x - 1
        if x == -1:
            x = 0
