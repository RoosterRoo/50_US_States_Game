import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
states = pd.read_csv("50_states.csv")


def print_state(x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(answer_state)


while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States found", "What's another state name?")
    if not answer_state:
        break
    answer_state = answer_state.title()

    if answer_state in states['state'].values:
        guessed_states.append(answer_state)
        state = states[states['state'] == answer_state]
        print_state(float(state['x']), float(state['y']))


states_not_found = [state for _, state in states['state'].items() if state not in guessed_states]
pd.DataFrame(states_not_found).to_csv("states_not_found.csv")
