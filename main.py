import turtle

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()

screen.title("U.S States Game")
screen.addshape(IMAGE)
screen.setup(800, 600)
screen.bgcolor("black")
turtle.shape(IMAGE)

answer_states = screen.textinput(title="Guess a U.S States", prompt="Guess another U.S States ? ")


screen.exitonclick()