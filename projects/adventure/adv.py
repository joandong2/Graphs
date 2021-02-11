from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# movements and opposite direction
directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

# records opposite direction when moving
prev_path = []

# store visted rooms
visited = {}

# first visited = {0: [n,s,w,e]}
visited[player.current_room.id] = player.current_room.get_exits()

# print('current room id', player.current_room.id)
# print('length room graph', len(room_graph))
# print('length visited current room id', len(visited[player.current_room.id]))
# print('visited', visited)

# curr: 0 1 2

# visited = {
#   0: [n!, s, w, e],
#   1: [n!, s!]
#   2: [s!] call while

while len(visited) < len(room_graph) - 1:
    # print(player.current_room.id)
    if player.current_room.id not in visited:
        # n,s,w,e appending order from get_exits method
        visited[player.current_room.id] = player.current_room.get_exits()
        previous_direction = prev_path[-1]
        visited[player.current_room.id].remove(previous_direction)
        # print(visited)

    while len(visited[player.current_room.id]) < 1:
        prev_room = prev_path.pop()
        traversal_path.append(prev_room)
        player.travel(prev_room)

    room = visited[player.current_room.id].pop(0)  # n n
    traversal_path.append(room)  # n n
    prev_path.append(directions[room])  # s s
    player.travel(room)
    # print(visited)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

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
