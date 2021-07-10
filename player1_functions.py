import turtle

def new_stamp(snake, pos_list, stamp_list):
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos)
    #snake.stamp() returns a stamp ID. Save it in some variable
    snake_stamp = snake.stamp()
    #print(snake_stamp)
    #append that stamp ID to stamp_list.
    stamp_list.append(snake_stamp)