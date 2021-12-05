# AOC 2021 - Day 1
# michaelFarrier

# This puzzle requires us to perform a sliding window technique to pass in modified input for puzzle_1
# Sliding Window restriction is K = 3
def puzzle_2(arr, k):
    new_arr = []
    window_start = 0 
    curr_sum = 0
    
    for window_end in range(len(arr)):
        
        curr_sum += arr[window_end]
        
        # Add the sum to our new arr and slide the window
        if window_end >= k-1:
            new_arr.append(curr_sum)
            curr_sum -= arr[window_start]
            window_start += 1
    
    return puzzle_1(new_arr)
    
# Puzzle narrows down to identifying increasing/decreasing points in data
# When the data is increasing we want to increment a count and when decreasing don't increment the count   
def puzzle_1(arr):
    count = 0

    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            count += 1
            
    return count

def main():
    
    # File I/O
    input_arr = [];
    
    with open('day1_input.txt', mode='r') as file:
        for line in file:
            input_arr.append(int(line))
    
    # Puzzles
    print('Puzzle #1:', puzzle_1(input_arr))
    print('Puzzle #2:', puzzle_2(input_arr, 3))
    
main()



