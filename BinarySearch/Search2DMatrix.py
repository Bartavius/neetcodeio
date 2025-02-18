
def searchMatrix(matrix, target: int) -> bool:

    def binSearchCol(l, r, arr):
        mid = int((l + r) / 2)
        if l >= r and arr[mid] != target:
            return False
        elif arr[mid] == target:
            return True
        elif arr[mid] < target:
            return binSearchCol(mid + 1, r, arr)
        else:
            return binSearchCol(l, mid - 1, arr)

    def binSearchRow(l, r, arr):
        mid = int((l + r) / 2)
        rowLength = len(arr[l]) - 1
        betweenCondition = arr[mid][0] <= target <= arr[mid][rowLength]
        
        if l >= r and not betweenCondition:
            return False
        if betweenCondition:
            return binSearchCol(0, rowLength, arr[mid])
        elif arr[mid][0] > target:
            return binSearchRow(l, mid - 1, arr)
        else:
            return binSearchRow(mid + 1, r, arr)

    return binSearchRow(0, len(matrix) - 1, matrix)
    
    