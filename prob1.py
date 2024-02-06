import math
import random

# Function definitions
def hourglassSum(arr):
    maxNum = -100
    sum = 0
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            # CALCULATE SUM
            sum = getSum(i,j, arr)
            maxNum = max(maxNum,sum)
            print(f"i: {i} j: {j} | {sum} {maxNum}")
            j += 1
        i += 1

    return maxNum

def getSum(i,j, arr):
    sum = 0
    sum += arr[i][j]        #1
    sum += arr[i][j+1]      #2
    sum += arr[i][j+2]      #3
    sum += arr[i+1][j+1]    #4
    sum += arr[i+2][j]      #5
    sum += arr[i+2][j+1]    #6
    sum += arr[i+2][j+2]    #7
    return sum

# Main code block
if __name__ == "__main__":
    # Code that should only run when the script is executed directly
    # This could include function calls, variable initializations, etc.
    arr = [
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5]
    ]
    result = hourglassSum(arr)
    print(result)
