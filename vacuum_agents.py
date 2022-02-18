# All of the agent definitions
from vacuum import *
import random


last_move = 'create'
location = [0,0]
i = 0

def reflex_agent(percept):
    if percept == True:

        return 'clean'
    else:
        return 'north'



def random_agent(percept):
    move = ['north', 'east', 'south','west']
    if percept == True:
        return 'clean'
    else:
        return random.choice(move)

def state_agent(percept):
    global i
    global last_move
    move = ['north', 'east', 'south','west']


    if percept == True:
        last_move = 'clean'
        return 'clean'
    else:
        if last_move != 'clean':
            last_move = random.choice(move)

            return last_move
        i += 1
        last_move = move[i % 4]

        return last_move


run(20, 50000, state_agent)

#print(many_runs(20, 50000, 10, reflex_agent))

print(many_runs(20, 50000, 10, random_agent))

print(many_runs(20, 50000, 10, state_agent))

