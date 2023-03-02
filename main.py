FONT = ('Arial', 8, 'normal')
ALIGNMENT = 'center'
import turtle
from turtle import Turtle
import pandas as pd

writer = Turtle()
writer.hideturtle()
writer.penup()
game_is_on = True
df = pd.read_csv('50_states.csv')
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
guessed_states = []


while game_is_on:
    answer_state = (screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name?")).title()
    if answer_state == 'Exit':
        missed_states = []
        for state in df['state']:
            if state not in guessed_states:
                missed_states.append(state)
        missing_data = pd.DataFrame(missed_states)
        missing_data.to_csv('Missed_States.csv')
        break
    if len(guessed_states) >= 50:
        game_is_on = False
    if answer_state in df['state'].unique() and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        x = int(df[df.state==answer_state]['x'])
        y = int(df[df.state==answer_state]['y'])
        writer.goto(x,y)
        writer.write(answer_state,align=ALIGNMENT, font=FONT)



screen.exitonclick()