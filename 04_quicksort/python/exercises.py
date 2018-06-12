def recursive_sum(arr):
    if (len(arr)) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])

def recursive_count(arr):
    if (len(arr) == 1):
        return 1
    else:
        return 1 + recursive_count(arr[1:])

def recursive_max(arr):
    if (len(arr) == 1):
        return arr[0]
    return max(arr[0], recursive_max(arr[1:]))

def recursive_binary_search(list, item, low=0, high=None):
    # low and high keep track of which part of the list you'll search in.
    # low = 0
    if high == None:
        high = len(list)-1

    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
      return mid

    if (guess > item):
        return recursive_binary_search(list, item, low, mid-1)
    else:
        return recursive_binary_search(list, item, mid+1, high)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(recursive_sum(arr))
# print(recursive_count(arr))
# print(recursive_max(arr))
print(recursive_binary_search(arr, 7))