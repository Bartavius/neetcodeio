'''
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.
'''

import heapq

def lastStoneWeight(stones) -> int:
    stone = [-i for i in stones]
    heapq.heapify(stone)

    while len(stone) > 1:
        first = heapq.heappop(stone)
        second = heapq.heappop(stone)
        if abs(first - second) != 0:
            heapq.heappush(stone, -(abs(first - second)))
    
    return -heapq.heappop(stone) if len(stone) == 1 else 0
