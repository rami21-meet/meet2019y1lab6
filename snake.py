import turtle
import random #we will need this later
turtle.color('blue')
turtle.bgcolor('black')
turtle.tracer(1,0) #this helps the turtle to move smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #curious? it is the turtle window size

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 75

#initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape('circle')

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
for loop in range(START_LENGTH):
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
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction='up' #change direction to up
     #update the snake drawing
    print('you pressed the up key!')

#2. make function down(),left(), and right() that change the snake.direction

#snake.direction = 'down'

def down():
    snake.direction='down'
    print('you pressed the down key!')

#snake.direction = 'right'

def right():
    snake.direction='Right'
    print('you pressed the right key!')

#snake.direction = 'left'

def left():
    snake.direction='Left'
    print('you pressed the left key!')

turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(left, 'Left')

turtle.listen()
food=turtle.clone()
food.hideturtle()
def make_food():
    #the screen positions from-SIZE/2 but we need the make food pieces only apper on game squares so we cut up the game board into multiplies of SQUARE_SIZE
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    #pick a position that is random multiply of square size
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())
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
    if snake.direction=='Right':
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('you moved right')
    elif snake.direction=='Left':
        snake.goto(x_pos-SQUARE_SIZE, y_pos)
        print('you moved left') 
  
    

    if snake.pos() in pos_list[:-1]:
        print(pos_list, snake.pos())
        quit()

    #make the snake stamp a new square on the screan hint-- use a single function
    new_stamp()
    
    ##### SPECIAL PLACE ITS FOR PART 5
    

    #if snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #what does this do?
        food.clearstamp(food_stamps[food_index]) #remove eaten food stamps
        food_pos.pop(food_index) #remove eaten food positions
        food_stamps.pop(food_index) #remove eaten food stamps
        print('you have eaten the food!')
        new_stamp()
    #HINT: this if statemint may be useful for part 8
            
    
    #remove the last piece of the snake
    remove_tail()

    #add new lines to the end of the function, grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    #the next three line check if the snake is hitting the right edge
    if new_x_pos >=RIGHT_EDGE:
        print('you hit the right edge! game over!')
        quit()
    if new_x_pos <=LEFT_EDGE:
        print('you hit the left edge! game over!')
        quit()
    if new_y_pos >=UP_EDGE:
        print('you hit the up edge! game over!')
        quit()
    if new_y_pos <=DOWN_EDGE:
        print('you hit the down edge! game over!')
        quit()
    
    if len(food_stamps) <= 6 :
        make_food()

    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

turtle.listen()

turtle.register_shape('trash.gif')

food = turtle.clone()
food.shape('trash.gif')

    
 

    





































turtle.mainloop()

    
