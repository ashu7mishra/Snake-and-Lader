snakes = int(input("Enter number of snakes in the game: "))
snake_position = []
print("Specificy snake tail and head in following manner for all snakes: (tail head) \n")
for snake in range(snakes):
    pos = input(f"Enter snake {snake+1} tail and head: ")
    pos = pos.split()
    snake_position.append([int(pos[0]), int(pos[1])])
print(snake_position)

ladders = int(input("Enter number of ladders in the game: "))
ladder_position = []
print("Specificy ladders start and end positions in following manner for all ladders: (start end) \n")
for ladder in range(ladders):
    pos = input(f"Enter ladder {ladder+1} start and end: ")
    pos = pos.split()
    ladder_position.append([int(pos[0]), int(pos[1])])
print(ladder_position)