import turtle
import pygame

#music
def bg_music():
    pygame.mixer.init()
    pygame.mixer.music.load('resources/tetris_theme.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

turtle.title("Snake Game")

turtle.bgcolor('green')

#border turtle drawing
def border():
    border = turtle.Turtle()
    border.penup()
    border.goto(320,320)
    border.pendown()
    border.shape('circle')
    border.width(20)
    border.goto(320,-320)
    border.goto(-320,-320)
    border.goto(-320,320)
    border.goto(320,320)

#title text
def title_txt():
    t_title = turtle.Turtle()
    t_title.hideturtle()
    t_title.pu()
    t_title.setposition(-200,350)
    t_title.write("Snake Game", font=("Arial", 50, "bold"))

#background picture
wn = turtle.Screen()
wn.bgpic("resources/grass_bg.gif")