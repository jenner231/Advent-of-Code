#read input from file input.txt and make a loop to read each line
with open('input.txt') as f:
    lines = f.readlines()


sum = 0
#get the first and last number in each line
for line in lines:
    numbers_in_line = [int(s) for s in line if s.isdigit()]
    #cast the numbers to string and concatenate them, then convert back to int
    sum += int(str(numbers_in_line[0]) + str(numbers_in_line[-1]))

print(sum)
