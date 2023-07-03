from turtle import *
#setting turtle
bgcolor("black")
setup(500,600)
title("Ironman")
color("orange")
speed(3)
#defining shape points
top=[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20),(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]
middle=[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210),(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]
bottom=[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250),(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]
#defining every part start
topStart=(0,120)
middleStart=(0,-30)
bottomStart=(0,-220)
#the draw method
def drawPart(part,partStart):
    #moving pen to starting location
    penup()
    goto(partStart)
    pendown()
    #drawing the part
    begin_fill()
    for i in range(len(part)):
        x,y=part[i]
        goto(x,y)
    end_fill()
#drawing parts
drawPart(top,topStart)
drawPart(middle,middleStart)
drawPart(bottom,bottomStart)    
#end drawing
hideturtle()
done()