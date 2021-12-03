# AOC 2021 - Day 1 - Puzzle 1
# michaelFarrier

# Puzzle narrows down to identifying increasing/decreasing points in data
# When the data is increasing we want to increment a count and when decreasing don't increment the count
def puzzle_1(arr):
    count = 0

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            count += 1
            
    return count

def main():
    input_arr = [];
    
    # File I/O
    with open('puzzle1_input.txt', mode='r') as file:
        for line in file:
            input_arr.append(int(line))
            
    return puzzle_1(input_arr)
    
main()



