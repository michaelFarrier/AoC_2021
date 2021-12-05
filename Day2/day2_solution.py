# AOC 2021 - Day 2
# michaelFarrier


# Modified version of puzzle_1, we now need to track a 3rd variable called aim.
# Depth is scaled by aim.
def puzzle_2():
    horizontal_position = 0
    depth = 0
    aim = 0
    
    # File I/O
    with open('day2_input.txt', mode='r') as file:
        for line in file:
            # for each instruction grab the direction & distance
            instruction = line.strip().split(' ')
            
            direction = instruction[0]
            units = int(instruction[1])
            
            # forward adds distance to the horizontal position
            # forward also adds depth based on aim
            # up subtracts aim 
            # down adds aim
            if direction == 'forward':
                horizontal_position += units
                if aim > 0:
                    depth += aim * units
                     
            elif direction == 'up':
                aim -= units
            elif direction == 'down':
                aim += units
            else:
                print('Unknown Direction!')
                
    return horizontal_position * depth


# This puzzle involves reading instructions from a text file and 
# manipulating 2 variables: depth and horizontal_position based on the instruction.
def puzzle_1():
    horizontal_position = 0
    depth = 0
    
    # File I/O
    with open('day2_input.txt', mode='r') as file:
        for line in file:
            # for each instruction grab the direction & distance
            instruction = line.strip().split(' ')
            
            direction = instruction[0]
            distance = int(instruction[1])
            
            # forward adds distance to the horizontal position
            # up subtracts depth 
            # down adds depth
            if direction == 'forward':
                horizontal_position += distance
            elif direction == 'up':
                depth -= distance
            elif direction == 'down':
                depth += distance
            else:
                print('Unknown Direction!')
    
    return horizontal_position * depth

def main():
    
    # Puzzles
    print('Puzzle #1:', puzzle_1())
    print('Puzzle #2:', puzzle_2())
    
main()
