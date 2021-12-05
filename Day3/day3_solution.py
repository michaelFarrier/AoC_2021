# AOC 2021 - Day 3
# michaelFarrier
from collections import Counter


def reduce_matrix(matrix, flag):
    idx = 0
    while len(matrix) != 1:
        # Grab the current column and identify the most common elements
        column = list(zip(*matrix))        
        most_common_elements = Counter(column[idx]).most_common()
        
        # When the most common elements is just 1 we can move on to the next column
        if len(most_common_elements) == 1:
            idx += 1
            continue
            
        most_common = most_common_elements[0]
        least_common = most_common_elements[1]
        
        most_common_bit = most_common[0]
        least_common_bit = least_common[0]
        
        # Oxygen Case: If the counts are the same (i.e. they are both the most common)
        # Prefer bit 1 over bit 0
        if flag == 'oxygen':
            
            if most_common[1] == least_common[1]:
                if most_common_bit != 1:
                    most_common_bit = least_common_bit
                        
            # Filter out the matrix based on the most common bit
            matrix = [row for row in matrix if most_common_bit == row[idx]]
        
        # CO2 Case: Prefer bit 0 over bit 1
        elif flag == 'co2':
            
            if most_common[1] == least_common[1]:
                if least_common_bit != 0:
                    least_common_bit = most_common_bit    
            
            # Filter out the matrix based on the least common bit
            matrix = [row for row in matrix if least_common_bit == row[idx]]
            
        idx += 1
        
    # Convert the binary to decimal
    return int("".join(str(x) for x in matrix[0]), 2)

# Puzzle 2 follows a similar process to puzzle 1, but we must reduce the matrix
# each time we discover the most/least common bit until we are down to just 1 binary answer.
def puzzle_2(matrix):
    oxygen_rating = reduce_matrix(matrix, 'oxygen')
    co2_scrubber_rating = reduce_matrix(matrix, 'co2')
    
    return oxygen_rating * co2_scrubber_rating

# Puzzle 1 involves going down the columns and to find the least and most common bit
# gamma rate uses the most_common bit
# epsilon rate uses the least_common bit
def puzzle_1(matrix):
    
    most_common = []
    least_common = []
    
    # zip gives us all the columns in the matrix
    # Can use Counter to get the most & least common element in each of the columns in the matrix
    for col in zip(*matrix):
        most_common.append(Counter(col).most_common()[0][0])
        least_common.append(Counter(col).most_common()[-1][0])
    
    # convert to decimal from binary string
    gamma_rate = int("".join(str(x) for x in most_common), 2)
    epsilon_rate = int("".join(str(x) for x in least_common), 2)
    
    return gamma_rate * epsilon_rate
    

def main():
    
    input_matrix = []
    
    # File I/O
    with open('day3_input.txt', mode='r') as file:
        for line in file:
            input_matrix.append(list(map(int, line.strip())))
    
    # Puzzles
    print('Puzzle #1:', puzzle_1(input_matrix))
    print('Puzzle #2:', puzzle_2(input_matrix))
    
main()
