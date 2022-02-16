# All of the agent definitions
from vacuum import *
import random

global last_percept
global last_move


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
    return 'clean'

#run(20, 50000, random_agent)

print(many_runs(20, 50000, 10, reflex_agent))

print(many_runs(20, 50000, 10, random_agent))
