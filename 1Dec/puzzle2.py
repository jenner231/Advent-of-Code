
with open('input.txt') as f:
    lines = f.readlines()


#create dict to translate spelled numbers to integers
numbers_dict = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7, 'eight':8, 'nine':9}
#get the first and last number in each line

def part2(lines):
    sum = 0
    for line in lines:
        numbers = []
        #get the first and last number in each line
        for i in range(len(line)):
            if line[i].isdigit():
                numbers.append(int(line[i]))
            else:
                for key in numbers_dict:
                    if line[i:i+len(key)] == key:
                        numbers.append(numbers_dict[key])
                        print(numbers_dict[key])
                        break
        print(numbers)
        sum += int(str(numbers[0]) + str(numbers[-1]))
    print(sum)
x = ["two1nine", "eighttwothree"]
part2(lines)