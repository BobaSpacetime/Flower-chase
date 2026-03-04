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
def draw():
    screen.blit("background", (0,0))
    b.draw()
    f.draw()

def update():
    if keyboard.left: 
        b.x-=1
    if keyboard.right:
        b.x+=1
    if keyboard.up:
        b.y-=1
    if keyboard.down:
        b.y+=1
    if b.colliderect(f):
        f.x = random.randint(50, 400)
        f.y = random.randint(50, 400)

pgzrun.go()