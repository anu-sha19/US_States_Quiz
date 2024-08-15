from turtle import Turtle, Screen
import pandas

#screen setup
screen = Screen()
turtle = Turtle()
screen.title("U.S. States Game")
screen.setup(height=491, width=725)

#you can add an image as a shape in a turtle
image = "blank_states_img.gif"
screen.addshape(image)  # need to add shape in Screen first to use it in turtle
turtle.shape(image)
screen.tracer(0)

#reading the csv file
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()  # NEED A LIST OF STATES
score = 0
user_answers = []

while score < 50:  #UNTIL YOU GET IT ALL RIGHT
    title = "Guess the state" if score == 0 else f"Score:{score}/50"
    answer = screen.textinput(title=f"{title}", prompt="What's another state's name? ")

    if answer == "exit":
        break

    if answer in user_answers:  #to make sure the user doesn't get points for repeated states
        continue

    user_answers.append(answer)
    if answer.title() in states:
        row_values = data[data.state == answer.title()]

        x = row_values.x.item()  #retrive the particular value without the index for ex: 0 145
        y = row_values.y.item()

        score += 1
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(answer.title(), False, "center", ("Arial", 7, "bold"))

#Finishing message
turtle.goto(150,0)
if score == 50:
    turtle.write("Well Done!!!", False, "center", ("Arial", 40, "bold"))
else:
    turtle.write("Unguessed state names in csv file: unguessed_states.csv", False, "right", ("Arial", 20, "bold"))
    for state in states:
            if state != user_answers:
                unguessed_state = state

                with open("unguessed_states.csv", mode='a') as file:
                    file.write(f"{unguessed_state}\n")

screen.exitonclick()