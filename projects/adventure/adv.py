from room import Room
from player import Player
from world import World

import random
from random import choice
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

rooms = set()
# rooms that are visited
player.current_room = world.starting_room
rooms.add(player.current_room.id)
last_move = ''
next_move = ''
fourways = dict()
# to help with 4way intersections

next_move = 'e'  # setting first move
traversal_path.append(next_move)

while len(rooms) < 500:  # continues till all rooms traversed
    player.travel(next_move)
    rooms.add(player.current_room.id)
    last_move = next_move
     # if 4 way intersection, prevents loop from happening
    if len(player.current_room.get_exits()) == 4:
        current = player.current_room.id
        if current not in fourways:
            fourways[current] = []
        if next_move not in fourways[current]:
            fourways[current].append(next_move)
        elif len(fourways[current]) < 4:
            next_move = choice([i for i in ['n', 's', 'e', 'w'] if i not in fourways[current]])
            fourways[current].append(next_move)
        else:
            # choice([i for i in ['n', 's', 'e', 'w']])
            next_move = fourways[current][len(fourways[current]) % 4]
            fourways[current].append(next_move)

    if last_move == 'e':
        if 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        else:
            next_move = 'w'
    elif last_move == 'n':
        if 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        else:
            next_move = 's'
    elif last_move == 'w':
        if 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        else:
            next_move = 'e'
    elif last_move == 's':
        if 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        else:
            next_move = 'n'
    traversal_path.append(next_move)

    if len(traversal_path) > 2000:
        break


print('Total Rooms traversed:', len(rooms))
print('Length of Traversal:', len(traversal_path))


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    print(player.current_room.id, player.current_room.get_exits())

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
