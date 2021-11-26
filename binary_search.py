# Binary search algorithm working philosophy
# Will be proven that binary search is faster than naive search

# Naive search: scan entire list and ask if its equal to target
# if yes, return index
# if no, then return -1

from operator import le
import random
import time

def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


# Binary search : Divide and Conquer!
# Assuming that our list is SORTED

def binary_search(l,target, low=None, high=None):

    if low == None:
        low = 0

    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2 # Approximet
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint-1)
    else:
        return binary_search(l,target,midpoint+1,high)

if __name__ == "__main__" :
    
    # l = [1,3,5,10,14]
    # target = 10
    # print(naive_search(l,target))
    # print(binary_search(l,target))
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()
    print("Naive search time: ",(end-start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print("Binary search time: ",(end-start)/length, "seconds")

    # Naive search time:  0.0010932374477386475 seconds => 1.093237447739 ms
    # Binary search time:  3.671760559082031e-05 seconds => 0.0367 ms