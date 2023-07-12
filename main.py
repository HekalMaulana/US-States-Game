import turtle
import pandas

IMAGE = "blank_states_img.gif"
screen = turtle.Screen()

screen.title("U.S States Game")
screen.addshape(IMAGE)
screen.setup(800, 600)
screen.bgcolor("black")
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
us_state = data["state"]
us_state_list = us_state.tolist()

correct_guess = []

while len(correct_guess) < 50:
    answer_states = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                                     prompt="Guess another U.S States ? ").title()

    if answer_states == "Exit":
        missing_state = [state for state in us_state_list if state not in correct_guess]
        states_to_learn = pandas.DataFrame(missing_state)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_states in us_state_list:
        correct_guess.append(answer_states)
        state = data[data["state"] == answer_states]
        x_state = state["x"].iloc[0]
        y_state = state["y"].iloc[0]

        text = turtle.Turtle()
        text.color("black")
        text.hideturtle()
        text.penup()
        text.goto(x_state, y_state)
        text.write(arg=f"{answer_states}")

screen.exitonclick()
