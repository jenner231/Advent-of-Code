
#Define max number of red, green and blue cubes:
max_red = 12
max_green = 13
max_blue = 14

with open('input.txt') as f:
    lines = f.readlines()
    #split lines into dict of pairs
    pairs = [line.split() for line in lines]
    print(lines)