import pandas
from turtle import Screen
from writer import Writer

screen = Screen()
screen.title("India States Quiz")
screen.bgpic("India.gif")

states = pandas.read_csv("states_of_india.csv")
printer = Writer()

quiz_is_on = True
states_found = []

while quiz_is_on:
    user_guess = screen.textinput(title=f"{len(states_found)}/30 found",
                                  prompt="Enter the name of any other state\nEnter Quit to Quit the Game")
    user_guess = user_guess.title()
    if user_guess == "Quit":
        quiz_is_on = False
        all_states = states.States.to_list()
        states_to_know = [state for state in all_states if state not in states_found]
        new_data = pandas.DataFrame(states_to_know)
        new_data.to_csv("States_to_learn.csv")
    for row_number in range(30):
        if states.at[row_number, "States"] == user_guess:
            printer.writer(states.at[row_number, "x"], states.at[row_number, "y"],
                           states.at[row_number, "States"])
            if user_guess not in states_found:
                states_found.append(user_guess)
    if len(states_found) == 30:
        quiz_is_on = False
