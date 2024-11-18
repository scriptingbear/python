#each location has a dictionary whose keys are one or more of the following E, W, N, S and Q (to quit)
# and whose values are the names of the locations in the house to which the mouse will move
#put the python in in a random location each time the game is played
#put mouse in a random location each time the game is played
#objective: mouse must make it to the front door without being eaten by the python

import random

#declare and populate moves dictionary
moves = {"Living Room" : {"E": "Bathroom", "W": "Kitchen", "S": "Basement", "N": "Front Door"},
            "Bathroom" : {"W": "Living Room", "S": "Bedroom", "N": "Front Door"},
            "Basement" : {"E": "Bedroom", "W": "Attic", "N": "Living Room"},
            "Kitchen" : {"E": "Living Room", "S": "Basement", "N": "Front Door"},
            "Bedroom" : {"W": "Basement", "N": "Bathroom"},
            "Attic" : {"E": "Basement", "N": "Kitchen"}
             
    } 

#determine python's location
#[NEW CODE: 01/29/2018] Instead of hard coding the locations, simply read them from the moves dictionary
locations = list(moves.keys())
py_loc = random.choice(locations)

#remove the snake's location to ensure that the mouse isn't assigned
#the same initial location as the python!
del locations[locations.index(py_loc)]
mouse_loc = random.choice(locations)

prompt = ''
welcome_msg = '''
Welcome to Pythonator™!

You're a mouse in a house
And you wanna get out
But there's a Python
That's lurking about

This is your mission
To escape is your quest
Cause that snake is wishing
That you'll be his lunch guest

This game can teach you
To become a Master Of Py
Just don't let that snake reach you
Or else you're gonna die!

© 2018 Adiv Abramson
'''


def getPrompt(loc):
    #get direction letters from sub dictionary inside moves{}
    sub_dict = moves.get(loc)
    return ",".join(sorted(sub_dict.keys()))


def getNextMove(direction):
    #[NEW CODE: 01/29/2018]if user enters invalid direction, return
    #current mouse location using get() method
    return moves[mouse_loc].get(direction,mouse_loc)



print(welcome_msg)

#loop until user enters "Q"
while True:
    #generate prompt
    prompt = getPrompt(mouse_loc)
    #[NEW CODE: 01/29/2018] convert input to upper case right from the start so that we don't have to
    # do that repeatedly later on
    option = input("You're in the {0}. Select direction ({1}) or press Q to quit ".format(mouse_loc, prompt)).upper()
    if option == "Q":
        print("Game over.")
        break
    elif option not in prompt:
        #[NEW CODE: 01/29/2018]instead of checking generically for any of the 4 valid directions, make validation
        #context sensitive by comparing option against the string contained in the prompt variable
        print("\"{}\" is not a valid selection. Try again.".format(option))
        continue
    
    mouse_loc = getNextMove(option)
    
    if mouse_loc == py_loc:
        print('''Oops! You've been eaten by The Pythonator!
        Thanks for coding!''')
        break
    elif mouse_loc == "Front Door":
        print('''Congratulations! You've escaped through the front door and will not be
        on the lunch menu...THIS TIME!  \\\o||o//''')
        break
    else:
        continue
