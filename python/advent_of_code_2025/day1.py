"""
L90 means 'Left' 90 ints
bounded 0-99 (0 -> L1 = 99)

password is actually:
the number of times the dial is left pointing at 
0 after any rotation in the sequence.


"""

def part1(lines):

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

    return zeros # 962

def part2(lines):

    # start at dial 50
    current = 50
    zeros = 0

    for direction, distance in lines:

        full_rotations = distance // 100
        remainder = distance % 100

        if remainder == 0:
            zeros += full_rotations
            continue
        
        temp = current + (remainder if direction == "R" else -remainder)
        
        zeros += full_rotations + (1 if (temp >= 100 or temp <= 0) and current != 0 else 0)
        current = temp
        current %= 100

    return zeros

def part2test():

     # start at dial 50
    current = 50
    zeros = 0
    
    while True:
        user = input()
        action = (user[0], int(user[1:].strip()))


        full_rotations = action[1] // 100
        remainder = action[1] % 100

        if remainder == 0:
            zeros += full_rotations
            print("current:", current)
            print("zero:", zeros)

            continue
        
        temp = current + (remainder if action[0] == "R" else -remainder)
        
        a = (1 if (temp >= 100 or temp <= 0) and current != 0 else 0)
        zeros += full_rotations + a
        current = temp
        current %= 100

        print("full rotations:", full_rotations)
        print("temp:", temp)
        print("a:", a)
        print("current:", current)
        print("zero:", zeros)
        print()

# read the input file -> pairs of (direction, distance)
with open("./day1.txt", 'r') as file:
    lines = [(line[0], int(line[1:].strip())) for line in file]

def test():
    # 1 full rotation from 50
    print(part2([('R', 100)]) == 1)

    # 100 full rotation from 50
    print(part2([('R', 10000)]) == 100)

    # 3 full rotation from 0
    print(part2([('L', 50), ('R', 300)]) == 4)

    # overflow L
    print(part2([('L', 1), ('L', 50)]) == 1)

    # overflow R
    print(part2([('R', 1), ('R', 50)]) == 1)
    
    # going from 0 to 0
    print(part2([
        ('R', 50),
        ('R', 100),
        ('L', 100),
        ]) == 3)



test()
print("Part 1:", part1(lines))
print("Part 2:", part2(lines))

part2test()