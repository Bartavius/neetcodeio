
def run_input():
    '''
    run the actual input file
    '''
    filepath = "./day2.txt"
    with open(filepath, "r") as file:
        lines = convert_to_pair(file.readline().split(","))
    return lines

def run_sample():
    '''
    use sample test case
    '''
    sample = convert_to_pair("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
    824824821-824824827,2121212118-2121212124".split(","))
    return sample

def convert_to_pair(arr_ranges):
    '''
    preps input to tuple (start, end) for each range
    '''
    return [tuple(rnge.split("-")) for rnge in arr_ranges]

def check_one_range(start, end):
    st = int(start)
    en = int(end)

    total = 0
    for num in range(st, en + 1):
        total += check_one_number(str(num), part)
    return total

def check_one_number_part1(num) -> int:
    # can only do even numbers
    if len(num) % 2 != 0:
        return 0
    
    midpoint = len(num) // 2
    first_half = num[:midpoint]
    second_half = num[midpoint:]

    # if the pattern repeats for the entire sequence
    if first_half == second_half:
        print("found pattern", first_half, "in number", num)
        return int(num)
    
    else:
        return 0
    
def check_one_number_part2(num) -> int:
    midpoint = len(num) // 2
    pattern = num[:midpoint]

    # naive solution
    while len(pattern) > 0:
        repetition = num.count(pattern)

        # if pattern repeats for the whole num
        if repetition * len(pattern) == len(num):
            print("found pattern", pattern, "in number", num)
            return int(num)
        
        else:
            midpoint -= 1
            pattern = num[:midpoint]
    
    return 0


  

def check_one_number(num, part) -> int:
    if part == 1:
        return check_one_number_part1(num)
    elif part == 2:
        return check_one_number_part2(num)


def part1(inp):
    total = 0
    for start, end in inp:
        total += check_one_range(start, end)

    return total

def test_for_sample(output, part):
    global test_sample
    sample_expected = 1227775554 if part == 1 else 4174379265

    print("\nOutput:", output)
    if test_sample:
        print("Expected sample:", output == sample_expected)
    print()
        

test_sample = False
part = 2

user = run_sample() if test_sample else run_input()
print("\nPart", part)
print("\nRunning on input:", user)
print()
print("-" * 40, "\n")

p1_output = part1(user)
test_for_sample(p1_output, part)

'''
pt1 answer logs:
54234399969
54234399924 <- correct

pt2 answer logs:
70187097315 <- correct
'''
