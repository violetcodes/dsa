'''quick sort'''
from recursion4 import *
import random 

def partision(array, l, r):
    pivot = array[l]
    j = l + 1
    for i in range(l+1, r+1):
        if array[i] <= pivot:
            array[j], array[i] = array[i], array[j]; j += 1
    
    array[j-1], array[l] = array[l], array[j-1]
    return j-1

def partision3(array, l, r):
    '''2 way partision is takes n^2 time if elements are equal
    to remedy this 3 way partision is needed'''
    pivot = array[l]
    j = l + 1
    for i in range(l+1, r+1):
        if array[i] < pivot:
            array[j], array[i] = array[i], array[j]; j += 1
    
    array[j-1], array[l] = array[l], array[j-1]

    k = j-1
    for i in range(j-1, r+1):
        if array[i] == pivot:
            array[k], array[i] = array[i], array[k]; k += 1
       
    
    # array[j-1], array[l] = array[l], array[j-1]

    print(array[:j-1], array[j-1:k], array[k:])
    return max(j-2, l), min(k, r)

def quick_sort(array, l=None, r=None):
    l = l or 0; r = r or len(array)-1
    if l >= r or l < 0 or r >= len(array):
        return 

    # pv = random.randint(l, r)
    # array[l], array[pv] = array[pv], array[l]
    
    m, n = partision3(array, l, r)
    print(array, m, n, l, r)

    quick_sort(array, l, m)
    quick_sort(array, n, r)


if __name__ == '__main__':
    unsorted = [3, 2, 1, 0, 2, 3, 1, 7, 3, 3, 5,3, 9, 12, 7, 8, 6, 11]
    # unsorted = [0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 5, 7, 9, 12, 7, 8, 6, 11]
    # # unsorted = [6, 4, 2, 3, 9, 8, 9, 4, 7, 6, 1]
    # unsorted = [1, 2]
    
    cpy = unsorted[:]
    # selection_sort(cpy)

    # cpy2 = unsorted[:]
    # cpy2 = merge_sort(cpy2)
    # print(cpy2)

    print(partision3(cpy, 0, len(cpy)-1))
    quick_sort(cpy)
    print(cpy)