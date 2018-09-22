import json
from collections import defaultdict
import networkx as nx

class Player:
    def __init__(self, player_num):
        self.player_num = player_num
        self.name = "Player" + str(player_num)
        self.stance = "Invalid Stance"
        self.health = 20
        self.speed = 0
        self.movement_counter = 7
        self.location = 0
        self.destination = 0
        self.dead = False
        self.rock = 1
        self.paper = 1
        self.scissors = 1

graph = nx.DiGraph()

with open("meta.json") as file:
    js = json.load(file)
    for edge in js["Edges"]:
        adjacents = edge["Adjacents"]
        graph.add_edge(adjacents[0],adjacents[1])
        graph.add_edge(adjacents[1],adjacents[0])
    for monster in js["Monsters"]:
        graph.node[monster["Location"]]["Monster"] = monster
 
print(graph.nodes())
print(graph.edges())
