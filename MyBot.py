# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random
import networkx as nx

graph_des = {

	"Edges" : [
		{"Name": "Edge_0_1", "Adjacents": [0, 1]},
		{"Name": "Edge_0_6", "Adjacents": [0, 6]},
		{"Name": "Edge_0_10", "Adjacents": [0, 10]},
		{"Name": "Edge_1_2", "Adjacents": [1, 2]},
		{"Name": "Edge_1_3", "Adjacents": [1, 3]},
		{"Name": "Edge_2_3", "Adjacents": [2, 3]},
		{"Name": "Edge_2_4", "Adjacents": [2, 4]},
		{"Name": "Edge_4_5", "Adjacents": [4, 5]},
		{"Name": "Edge_4_13", "Adjacents": [4, 13]},
		{"Name": "Edge_5_6", "Adjacents": [5, 6]},
		{"Name": "Edge_6_7", "Adjacents": [6, 7]},
		{"Name": "Edge_7_8", "Adjacents": [7, 8]},
		{"Name": "Edge_8_9", "Adjacents": [8, 9]},
		{"Name": "Edge_8_14", "Adjacents": [8, 14]},
		{"Name": "Edge_9_10", "Adjacents": [9, 10]},
		{"Name": "Edge_10_11", "Adjacents": [10, 11]},
		{"Name": "Edge_10_16", "Adjacents": [10, 16]},
		{"Name": "Edge_11_12", "Adjacents": [11, 12]},
		{"Name": "Edge_12_13", "Adjacents": [12, 13]},
		{"Name": "Edge_12_16", "Adjacents": [12, 16]},
		{"Name": "Edge_12_22", "Adjacents": [12, 22]},
		{"Name": "Edge_13_14", "Adjacents": [13, 14]},
		{"Name": "Edge_13_20", "Adjacents": [13, 20]},
		{"Name": "Edge_14_19", "Adjacents": [14, 19]},
		{"Name": "Edge_15_16", "Adjacents": [15, 16]},
		{"Name": "Edge_15_18", "Adjacents": [15, 18]},
		{"Name": "Edge_16_17", "Adjacents": [16, 17]},
		{"Name": "Edge_17_18", "Adjacents": [17, 18]},
		{"Name": "Edge_19_20", "Adjacents": [19, 20]},
		{"Name": "Edge_19_22", "Adjacents": [19, 22]},
		{"Name": "Edge_19_23", "Adjacents": [19, 23]},
		{"Name": "Edge_20_21", "Adjacents": [20, 21]},
		{"Name": "Edge_20_21", "Adjacents": [20, 21]},
		{"Name": "Edge_21_22", "Adjacents": [20, 21]},
		{"Name": "Edge_23_24", "Adjacents": [23, 24]}
		
	],
	"Monsters" : [
		{"Name": "Health 0", "Health": 4, "Stance": "Rock", "Speed": -33, "Location": 0, "Attack": 0, "Death Effects":
			{"Rock": 0, "Paper": 0, "Scissors": 0, "Speed": 0, "Health": 20}} ,
		{"Name": "Rock 1", "Health": 4, "Stance": "Rock", "Speed": -7, "Location": 1, "Attack": 1, "Death Effects":
				{"Rock": 0, "Paper": 1, "Scissors": 0, "Speed": 0, "Health": 0}}, 
		{"Name": "Paper 3", "Health": 8, "Stance": "Paper", "Speed": -53, "Location": 3, "Attack": 2, "Death Effects":
			{"Rock": 0, "Paper": 0, "Scissors": 0, "Speed": 1, "Health": 0}},
		{"Name": "Rock 4", "Health": 16, "Stance": "Rock", "Speed": -21, "Location": 4, "Attack": 4, "Death Effects":
			{"Rock": 0, "Paper": 4, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Paper 6", "Health": 4, "Stance": "Paper", "Speed": -7, "Location": 6, "Attack": 1, "Death Effects":
			{"Rock": 0, "Paper": 0, "Scissors": 1, "Speed": 0, "Health": 0}},
		{"Name": "Scissors 8", "Health": 16, "Stance": "Scissors", "Speed": -33, "Location": 8, "Attack": 4, "Death Effects":
			{"Rock": 0, "Paper": 0, "Scissors": 4, "Speed": 0, "Health": 0}},
		{"Name": "Scissors 10", "Health": 4, "Stance": "Scissors", "Speed": -7, "Location": 10, "Attack": 1, "Death Effects":
			{"Rock": 1, "Paper": 0, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Rock 11", "Health": 16, "Stance": "Rock", "Speed": -53, "Location": 11, "Attack": 4, "Death Effects":
			{"Rock": 0, "Paper": 4, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Rock 13", "Health": 8, "Stance": "Rock", "Speed": -21, "Location": 13, "Attack": 2, "Death Effects":
			{"Rock": 2, "Paper": 0, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Rock 15", "Health": 16, "Stance": "Rock", "Speed": -33, "Location": 15, "Attack": 4, "Death Effects":
			{"Rock": 0, "Paper": 0, "Scissors": 4, "Speed": 0, "Health": 0}},
		{"Name": "Rock 16", "Health": 8, "Stance": "Rock", "Speed": -21, "Location": 16, "Attack": 2, "Death Effects":
			{"Rock": 2, "Paper": 0, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Scissors 17", "Health": 16, "Stance": "Scissors", "Speed": -33, "Location": 17, "Attack": 4, "Death Effects":
			{"Rock": 4, "Paper": 0, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Paper 18", "Health": 8, "Stance": "Paper", "Speed": -21, "Location": 18, "Attack": 2, "Death Effects":
			{"Rock": 0, "Paper": 2, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Paper 20", "Health": 8, "Stance": "Paper", "Speed": -21, "Location": 20, "Attack": 2, "Death Effects":
			{"Rock": 0, "Paper": 0, "Scissors": 2, "Speed": 0, "Health": 0}},
		{"Name": "Scissors 21", "Health": 16, "Stance": "Scissors", "Speed": -53, "Location": 21, "Attack": 4, "Death Effects":
			{"Rock": 0, "Paper": 0, "Scissors": 0, "Speed": 2, "Health": 0}},
		{"Name": "Scissors 22", "Health": 8, "Stance": "Scissors", "Speed": -21, "Location": 22, "Attack": 2, "Death Effects":
			{"Rock": 0, "Paper": 2, "Scissors": 0, "Speed": 0, "Health": 0}},
		{"Name": "Scissors 23", "Health": 12, "Stance": "Scissors", "Speed": -33, "Location": 23, "Attack": 3, "Death Effects":
			{"Rock": 1, "Paper": 0, "Scissors": 2, "Speed": 0, "Health": 0}},
		{"Name": "Paper 24", "Health": 30, "Stance": "Paper", "Speed": -73, "Location": 24, "Attack": 5, "Death Effects":
			{"Rock": 3, "Paper": 3, "Scissors": 3, "Speed": 0, "Health": 0}}
	
	]
}


first_line = True # DO NOT REMOVE

# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]

# Create the graph
graph = nx.DiGraph()
for edge in graph_des["Edges"]:
    adjacents = edge["Adjacents"]
    graph.add_edge(adjacents[0],adjacents[1])
    graph.add_edge(adjacents[1],adjacents[0])
for monster in graph_des["Monsters"]:
    graph.node[monster["Location"]]["Monster"] = monster

def printLocations(arr, location):
    r = []
    for a in arr:
        r.append(len(game.shortest_paths(location, a.location)[0]))
    game.log(str(r))

def log(message):
    game.log(str(message))

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
 
    #log(graph.nodes())
    game.log(str(graph.nodes()))
    game.log(str(graph.edges()))


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
