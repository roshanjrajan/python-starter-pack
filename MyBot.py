# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random

first_line = True # DO NOT REMOVE

# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]


def printLocations(arr, location):
    r = []
    for a in arr:
        r.append(len(game.shortest_paths(location, a.location)[0]))
    game.log(str(r))

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------

    # code in this block will be executed each turn of the game

    me = game.get_self()

    if me.location == me.destination: # check if we have moved this turn
        # get all living monsters closest to me
        monsters = game.nearest_monsters(me.location, 1)
        printLocations(monsters, me.location)

        # choose a monster to move to at random
        monster_to_move_to = monsters[0]

        # get the set of shortest paths to that monster
        paths = game.shortest_paths(me.location, monster_to_move_to.location)
        destination_node = paths[0][0]
    else:
        destination_node = me.destination

    if game.get_opponent().location == me.location:
        chosen_stance = stances[random.randint(0, 2)]
    elif game.has_monster(me.location) and not game.get_monster(me.location).dead:
        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]

    # get more health if we are low
    if (me.health < len(game.shortest_paths(me.location, 0)[0]) * 15):
        destination_node = game.shortest_paths(me.location, 0)[0][0]

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)
