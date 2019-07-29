import turtle
import random #we will need this later

turtle.tracer(1,0) #this helps the turtle to move smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #curious? it is the turtle window size

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

#initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape('square')


#hide the turtle object (it is an arrow - we dont need to see it)
turtle.hideturtle()
#function to draw a part of the snake on the screan

def new_stamp():
    snake_pos = snake.pos() #get the snake's position
    #append the position tuple to pos_list
    pos_list.append(snake_pos)
    #snake.stamp() returns a stamp ID. save it in some variable
    stamp = snake.stamp()
    #append that stamp ID to stamp_list
    stamp_list.append(stamp)

#draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for loop in range():
    x_pos=snake.pos() #get x-position with snake.pos() [0]
    y_pos=snake.pos()

    #add SQUARE_SIZE to x_pos.where does x_pos point to now?
    # you are right
    x_pos+=

    snake.goto() #move snake to new (x,y)
    #now draw the new snake part on the screan (hint, you have a function to do this
    ()
