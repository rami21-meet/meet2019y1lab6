import turtle
import random #we will need this later

turtle.tracer(1,0) #this helps the turtle to move smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #curious? it is the turtle window size

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 100

#initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#set up positions (x,y) of boxes that make up the snakei
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
for loop in range(6):
    x_pos=snake.pos()[0] #get x-position with snake.pos() [0]
    y_pos=snake.pos()[1]

    #add SQUARE_SIZE to x_pos.where does x_pos point to now?
    # you are right
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #move snake to new (x,y)
    #now draw the new snake part on the screan (hint, you have a function to do this
    new_stamp()
 def remove_tail(): 
     old_stamp = stamp_list.pop(0) #last piece of tail
     snake.clearstamp(old_stamp) #erase last piece of the tail
     pos_list.pop(0) #remove last piece of tail's position

snake.direction = 'up'

def up():
    snake.direction='up' #change direction to up
    move_snake() #update the snake drawing
    print('you pressed the up key!')

#2. make function down(),left(), and right() that change the snake.direction

snake.direction = 'down'

def down():
    snake.direction]'down'
    move_snake()
    print('you pressed the down key!')

snake.direction = 'right'

def right():
    snake.direction='Right'
    move_snake()
    print('you pressed the right key!')

snake.direction = 'left'

def left():
    snake.direction='Left'
    move_snake()
    print('you pressed the left key!')

turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(left, 'Left')

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    #if snake.direction is up, then we want the snake to change its y position by square_size
    if snake.direction == 'up':
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print('you moved up')
    elif snake.direction=='down':
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print('you moved down!')

    #write the conditions for RIGHT and LEFT on your own
    if snake.direction=='right':
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('you moved right')
    elif snake.direction=='left':
        snake.goto(x_pos-SQUARE_SIZE, y_pos)
        print('you moved left')
    #make the snake stamp a new square on the screan hint-- use a single function
    new_stamp()
    
    ##### SPECIAL PLACE ITS FOR PART 5
    
    #remove the last piece of the snake
    remove_tail() 




































turtle.mainloop()

    
