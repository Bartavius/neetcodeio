'''
NEW PROBLEMS:
• #217 Contains Duplicate (Easy)
  Pattern: HashSet for O(1) lookup
• #242 Valid Anagram (Easy)
  Pattern: Frequency counting with HashMap
• #1 Two Sum (Easy)
  Pattern: Complement lookup in HashMap
• #49 Group Anagrams (Medium)
  Pattern: Sorted string or char count as key
'''

from typing import List


def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False

def valid_anagram(s, t):
    bucket = [0] * 26
    start = ord('a')

    # bucket sort count s
    for c in s:
        bucket[ord(c) - start] += 1
    
    # decrement chars from bucket
    for c in t:

        # exhausted that char
        if bucket[ord(c) - start] <= 0:
            return False
        else:
            bucket[ord(c) - start] -= 1
    
    return sum(bucket) == 0

def twoSum(self, nums: List[int], target: int) -> List[int]:

    arr = []
    for i, num in enumerate(nums):
        arr.append([num, i])
    arr.sort()

    print(arr)
    
    l, r = 0, len(arr) - 1

    while l < r:
        left = arr[l]
        right = arr[r]

        res = left[0] + right[0]

        if res == target:
            return [
                min(left[1], right[1]),
                max(left[1], right[1])
                ]
        elif res < target:
            l += 1
        else:
            r -= 1

    return []

def group_anagrams(strs):
    # need a dict (key -> list of strs)

    res = dict()
    start = ord("a")

    for word in strs:

        # count the letters in each word into a bucket (26 alphabet, lowercase)
        word_count = [0 for i in range(26)]

        for c in word:
            word_count[ord(c) - start] += 1
        
        # create new key
        key = tuple(word_count)
        if key in res:
            res[key].append(word)
        else:
            res[key] = [word]


    return list(res.values())