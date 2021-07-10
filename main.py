import turtle
import random #We'll need this later in the lab
import easygui
import pygame
import graphics
import player1_functions

graphics.bg_music()

turtle.title("Snake Game")

turtle.bgcolor('green')

graphics.border()

graphics.title_txt()


wn = turtle.Screen()
wn.bgpic("resources/grass_bg.gif")

score = 0
score2 = 0

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window
#size.
turtle.penup()

SQUARE_SIZE = 20 #Size of the squares that make up the snake
START_LENGTH = 4 #Initial size of the snake
TIME_STEP = 100

if score % 2 == 0:
    TIME_STEP -= 15

#Initialize lists
pos_list = []   #list of coordinates
stamp_list = [] #list of stamps that represent body of snake
food_pos = []   #list of coordinates of food
food_stamps = []#Initialize lists

pos_list2 = []   #list of coordinates
stamp_list2 = [] #list of stamps that represent body of snake

#Set up positions (x,y) of boxes that make up the snake
#Player 1
snake = turtle.clone()
snake.shape("circle")

#Player 2
snake2 = turtle.clone()
snake2.shape("square")

snake2.goto(-100,-60)

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


#Function to draw a part of the snake on the screen

# def new_stamp():
#     snake_pos = snake.pos() #Get snake’s position
#     #Append the position tuple to pos_list
#     pos_list.append(snake_pos)
#     #snake.stamp() returns a stamp ID. Save it in some variable
#     snake_stamp = snake.stamp()
#     #print(snake_stamp)
#     #append that stamp ID to stamp_list.
#     stamp_list.append(snake_stamp)

def new_stamp2():
    snake2_pos = snake2.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list2.append(snake2_pos)
    #snake.stamp() returns a stamp ID. Save it in some variable
    snake2_stamp = snake2.stamp()
    #print(snake_stamp)
    #append that stamp ID to stamp_list.
    stamp_list2.append(snake2_stamp)



# Draw a snake at the start of the game with a for loop
# for loop should use range() and count up to the number of pieces
# in the snake (i.e. START_LENGTH)
for snake_body in range(START_LENGTH):
    x_pos = snake.pos()[0]  # Get x-position with snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos += SQUARE_SIZE
    snake.goto(x_pos, y_pos)

    player1_functions.new_stamp(snake, pos_list, stamp_list)

#player 2
for snake2_body in range(START_LENGTH):
    x_pos2 = snake2.pos()[0]  # Get x-position with snake.pos()[0]
    y_pos2 = snake2.pos()[1]

    # Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
    # You're RIGHT!
    x_pos2 += SQUARE_SIZE
    snake.goto(x_pos2, y_pos2)  # Move snake to new (x,y)
    # Now draw the new snake part on the screen (hint, you have a
    # function to do this
    new_stamp2()


def remove_tail():
    old_stamp = stamp_list.pop(0) # remove last piece of tail
    snake.clearstamp(old_stamp)  # erase last piece of tail
    pos_list.pop(0)  # remove last piece of tail's position

def remove_tail2():
    old_stamp = stamp_list2.pop(0) # remove last piece of tail
    snake2.clearstamp(old_stamp)  # erase last piece of tail
    pos_list2.pop(0)  # remove last piece of tail's position

##################################################################
snake.direction = "Up"

snake2.direction = "Up"

UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300




def up():
    snake.direction = "Up"  # Change direction to up
    print("You pressed the up key!")


# 2. Make functions down(), left(), and right() that change snake.direction

snake.direction = "Down"

def down():
    snake.direction = "Down"  # Change direction to down
    print("You pressed the down key!")

snake.direction = "Left"

def left():
    snake.direction = "Left"  # Change direction to left
    print("You pressed the left key!")

snake.direction = "Right"

def right():
    snake.direction = "Right"  # Change direction to right
    print("You pressed the right key!")
#####################################################################

def up2():
    snake2.direction = "Up"  # Change direction to up
    print("You pressed the W key!")


# 2. Make functions down(), left(), and right() that change snake.direction

snake2.direction = "Down"

def down2():
    snake2.direction = "Down"  # Change direction to down
    print("You pressed the S key!")

snake2.direction = "Left"

def left2():
    snake2.direction = "Left"  # Change direction to left
    print("You pressed the A key!")

snake2.direction = "Right"

def right2():
    snake2.direction = "Right"  # Change direction to right
    print("You pressed the D key!")

#############################################################################


turtle.onkeypress(up, "Up")  # Create listener for up key

# 3. Do the same for the other arrow keys

turtle.onkeypress(down, "Down")

turtle.onkeypress(left, "Left")

turtle.onkeypress(right, "Right")


#########player2
turtle.onkeypress(up2, "w")  # Create listener for up key

# 3. Do the same for the other arrow keys

turtle.onkeypress(down2, "s")

turtle.onkeypress(left2, "a")

turtle.onkeypress(right2, "d")

turtle.listen()

turtle.register_shape("resources/smol_apple.gif")
food = turtle.clone()
food.shape('resources/smol_apple.gif')
food.hideturtle()
food_pos = [(100, 100), (-100, 100), (-100, -100), (100, -100)]
food_stamps = []
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_id = food.stamp()
    food_stamps.append(food_id)


def make_food():
    # The screen positions go from -SIZE/2 to +SIZE/2
    # But we need to make food pieces only appear on game squares
    # So we cut up the game board into multiples of SQUARE_SIZE.
    min_x = -int(600 / 2 / SQUARE_SIZE) + 1
    max_x = int(600 / 2 / SQUARE_SIZE) - 1
    min_y = -int(600 / 2 / SQUARE_SIZE) + 1
    max_y = int(600 / 2 / SQUARE_SIZE) - 1

    # Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x, max_x) * SQUARE_SIZE  # Random x pos
    food_y = random.randint(min_y, max_y) * SQUARE_SIZE  # Random y pos

    ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
    ##                        position
    food.goto(food_x,food_y)
    ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append(food.pos())
    ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food_id = food.stamp()
    food_stamps.append(food_id)


def move_snake():
    global score
    global score2
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    # Grab position of snake

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]





    #player2
    my_pos2 = snake2.pos()
    x_pos2 = my_pos2[0]
    y_pos2 = my_pos2[1]
    # Grab position of snake

    new_pos2 = snake2.pos()
    new_x_pos2 = new_pos2[0]
    new_y_pos2 = new_pos2[1]

    # The next three lines check if the snake is hitting the
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    # You should write code to check for the left, top, and bottom edges.

    if new_x_pos <= LEFT_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    if new_y_pos >= UP_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    if new_y_pos <= DOWN_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    # If snake.direction is up, then we want the snake to change
    # it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)

    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)


    # 4. Write the conditions for RIGHT and LEFT on your own

    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)

    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)

    if len(food_stamps) <= 6:
        make_food()

    #player2
    if new_x_pos2 >= RIGHT_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    # You should write code to check for the left, top, and bottom edges.

    if new_x_pos2 <= LEFT_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    if new_y_pos2 >= UP_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    if new_y_pos2 <= DOWN_EDGE:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    # If snake.direction is up, then we want the snake to change
    # it’s y position by SQUARE_SIZE
    if snake2.direction == "Up":
        snake2.goto(x_pos2, y_pos2 + SQUARE_SIZE)

    elif snake2.direction == "Down":
        snake2.goto(x_pos2, y_pos2 - SQUARE_SIZE)


    # 4. Write the conditions for RIGHT and LEFT on your own

    elif snake2.direction == "Right":
        snake2.goto(x_pos2 + SQUARE_SIZE, y_pos2)

    elif snake2.direction == "Left":
        snake2.goto(x_pos2 - SQUARE_SIZE, y_pos2)

    if len(food_stamps) <= 6:
        make_food()


    player1_functions.new_stamp(snake, pos_list, stamp_list)

    new_stamp2()


    # Now, call the move_snake() function.  This starts moving the snake.  Once it starts
    # moving, it keeps moving by itself:


    # Make the snake stamp a new square on the screen
    # Hint - use a single function to do this


    ######## SPECIAL PLACE - Remember it for Part 5 ########
    if snake.pos() in food_pos:

        food_index = food_pos.index(snake.pos())  # What does this do?
        food.clearstamp(food_stamps[food_index])  # Remove eaten food stamp
        food_pos.pop(food_index)  # Remove eaten food position
        food_stamps.pop(food_index)  # Remove eaten food stamp
        print("You have eaten the food!")
        player1_functions.new_stamp(snake, pos_list, stamp_list)
        score += 1

    if snake2.pos() in food_pos:

        food_index = food_pos.index(snake2.pos())  # What does this do?
        food.clearstamp(food_stamps[food_index])  # Remove eaten food stamp
        food_pos.pop(food_index)  # Remove eaten food position
        food_stamps.pop(food_index)  # Remove eaten food stamp
        print("You have eaten the food!")
        new_stamp2()
        score2 += 1

    remove_tail()

    remove_tail2()

    if new_pos in pos_list[:-4]:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()

    if new_pos2 in pos_list[:-4]:
        pygame.mixer.music.fadeout(3000)
        easygui.msgbox("Player 1 ate " + str(score) + " apples!\nPlayer 2 ate " + str(score2) + " apples!", title="Game Over!")
        quit()
    turtle.ontimer(move_snake, TIME_STEP)  # <--- new line here
move_snake()
# remove the last piece of the snake (Hint Functions are FUN!)


turtle.mainloop()
