def topKFrequent(nums, k: int):

    # 1. count frequency 
    # 2. put in hashset,

    # sort the numbers into: 
    #     key: frequency, elem: all the nums that has that frequency

    frequencies = [[] for i in range(len(nums))]
    count = {}

    # counting the frequency
    for n in nums:
        if str(n) not in count:
            count[str(n)] = 0
        count[str(n)] += 1
    
    # bucket sorting
    for key in count.keys():
        frequencies[count[key] - 1].append(int(key))

    length = len(frequencies)

    # getting output
    res = []
    i = length - 1
    while len(res) < k:
        if not frequencies[i]:
            i -= 1
            continue
        res.append(frequencies[i].pop())
    
    return res