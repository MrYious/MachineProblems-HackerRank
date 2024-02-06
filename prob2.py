import math
import random

def dynamicArray(n, queries):
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    # print(arr)
    for query in queries:
        num = int(query[0])
        x = int(query[1])
        y = int(query[2])
        idx = ((x ^ lastAnswer) % n)
        if num == 1:
            arr[idx].append(y)
        elif num == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            print(lastAnswer)

        # print(f'{arr}')

# Main code block
if __name__ == "__main__":
    n = 2
    queries = [
        [1, 0, 50],
        [1, 1, 70],
        [1, 0, 30],
        [2, 1, 0],
        [2, 1, 1]
    ]

    result = dynamicArray(n, queries)
