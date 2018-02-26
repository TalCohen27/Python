
def binarySearch(orderedList, num):

    left = 0
    right = len(orderedList) - 1
    mid = int((left + right) / 2)

    if orderedList[mid] == num:
        return True
    else:
        while left <= right:
            if num < orderedList[mid]:
                right = mid-1
            elif num > orderedList[mid]:
                left = mid+1
            elif num == orderedList[mid]:
                return True
            mid = int((left + right)/2)
    return False


a = [1, 3, 5, 30, 42, 43, 500]

print(str(binarySearch(a, -1)))

