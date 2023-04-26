import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Games")
image = "Code_100/Day_25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(
    "Code_100/Day_25/us-states-game-start/50_states.csv")

guessed_state = []
all_states = data["state"].to_list()

game_is_on = True
while game_is_on or len(guessed_state) > 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state name? ").title()  # type: ignore

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        cor = data[data.state == answer_state]
        t.goto(int(cor.x), int(cor.y))  # type: ignore
        t.write(answer_state)
    print(guessed_state)
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("state_to_learn.csv")

        # or
        # missing_states = [state for state in all_states if state not in guessed_state]

        game_is_on = False

res = list(set(all_states) - set(guessed_state))

need_to_learn_list = {
    "state": res
}


new_data = pandas.DataFrame(need_to_learn_list)
# new_data.to_csv("Code_100/Day_25/us-states-game-start/state_to_learn.csv")
print(new_data)


screen.exitonclick()
