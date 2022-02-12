#attractive multi colored starts

import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(10)
col=['yellow','blue','white','green','red']

c=0
for l in range(80):
    t.forward(l*10)
    t.right(144)
    t.color(col[c])
    if c==4:
        c=0
        
    else:
        c+=1
        
#let's see magic of python------>>>>>
