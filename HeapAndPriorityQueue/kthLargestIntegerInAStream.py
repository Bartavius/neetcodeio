import heapq


class KthLargest:

    def __init__(self, k: int, nums):

        self.minHeap = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]