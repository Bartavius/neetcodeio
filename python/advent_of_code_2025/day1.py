"""
L90 means 'Left' 90 ints
bounded 0-99 (0 -> L1 = 99)

password is actually:
the number of times the dial is left pointing at 
0 after any rotation in the sequence.


"""

# read the input file -> pairs of (direction, distance)
with open("./day1.txt", 'r') as file:
    lines = [(line[0], int(line[1:].strip())) for line in file]

print((-11) % 5)

# start at dial 50
current = 50
zeros = 0

for direction, distance in lines:

    if direction == "R":
        current = (current + distance) % 100 # bounded

    elif direction == "L":
        current = (current - distance) % 100 # bounded


    # accumulate number of zeros
    if current == 0:
        zeros += 1

print(zeros) # 962