'''
import turtle
turtle.goto(0,0)

def up():
    print('you pressed the up key')

turtle.onkey(up, 'Up')
turtle.goto(0,0)
turtle.listen()
'''
import turtle
turtle.goto(0,0)

turtle.direction = None

def up():
    turtle.direction = 'Up'
    #print('you pressed the up key.')

turtle.onkey(up, 'Up')
turtle.listen()
def on_move( ):
    x,y= turtle.pos()
    if turtle.direction == 'Up':
        turtle.goto(x,y+10)
    
        
    
