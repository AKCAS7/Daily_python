import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title = " Guess the state ", prompt = " What is the states name ? ")
    
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[ data.state == answer_state ]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)







screen.exitonclick()

