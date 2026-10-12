import turtle as t
import math as m
import random as r
import time

s = t.Screen()
s.setup(600, 600)
s.bgcolor("black")
s.tracer(0)

N = 500
stars = []

for i in range(N):

    a = 2 * m.pi * (i / N)
    
    base_x = 16 * (m.sin(a)**3) * 11
    base_y = (13*m.cos(a) - 5*m.cos(2*a) - 2*m.cos(3*a) - m.cos(4*a)) * 11

    tx = base_x + r.uniform(-15, 15) 
    ty = base_y + r.uniform(-15, 15)

    sx, sy = r.randint(-320, 320), r.randint(-320, 320)
    size = r.uniform(1.5, 3.5)
    stars.append((sx, sy, tx, ty, size))

p = t.Turtle()
p.hideturtle()

def draw_star(x, y, size):
    p.pencolor("#a855f7") 
    p.width(1)
    for angle in (0, 45, 90, 135):
        rad = m.radians(angle)
        dx = size * m.cos(rad)
        dy = size * m.sin(rad)
        p.penup()
        p.goto(x - dx, y - dy)
        p.pendown()
        p.goto(x + dx, y + dy)

steps = 50

for frame in range(steps + 1):
    p.clear()
    progress = frame / steps
    eased = m.sin(progress * m.pi / 2)

    for sx, sy, tx, ty, size in stars:
        cx = sx + (tx - sx) * eased
        cy = sy + (ty - sy) * eased
        draw_star(cx, cy, size)

    s.update()
    time.sleep(0.02)

t.done()