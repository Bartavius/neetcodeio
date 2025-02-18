def search(nums, target: int) -> int:
        
    def binSearch(l, r):
        mid = int((l + r) / 2)

        if l >= r and nums[mid] != target:
            return -1

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binSearch(mid + 1, r)
        else:
            return binSearch(l, mid - 1)

    l, r = 0, len(nums) - 1
    return binSearch(l, r)