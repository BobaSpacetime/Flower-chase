import pgzrun
import random

WIDTH= 450
HEIGHT= 450

b = Actor("bee")
b.pos = (225, 225)
f = Actor("flower")
f.x = random.randint(50,400)
f.y = random.randint(50, 400)
score = 0
gameover = False
def draw():
    screen.blit("background", (0,0))
    b.draw()
    f.draw()
    screen.draw.text("Score: " + str(score), (10,10), color = "#073A11")
    if gameover==True:
        screen.fill("#1E0A3A")
        screen.draw.text("TIME'S UP! Your score was: " + str(score) + " in 1 minute", center = (225, 225), color = "#B79CEB")
    if score>=30:
        screen.fill("#ECD030")
        screen.draw.text("YOU WIN!", center = (225, 225), color = "#FFFC39")

def update():
    global score
    if keyboard.left: 
        b.x-=1
    if keyboard.right:
        b.x+=1
    if keyboard.up:
        b.y-=1
    if keyboard.down:
        b.y+=1
    if b.colliderect(f):
        score +=1
        f.x = random.randint(50, 400)
        f.y = random.randint(50, 400)

def timesup():
    global gameover
    gameover = True 

clock.schedule(timesup, 60.0)
pgzrun.go()