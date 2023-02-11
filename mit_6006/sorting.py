import random 
import copy 
def selection_sort(array):
    n = len(array)
    for i in range(n-1, -1, -1):
        max_index = i 
        for j in range(i):
            if array[max_index] < array[j]:
                max_index = j 
        array[max_index], array[i] = array[i], array[max_index]
    

def merge_op(left, right):
    n, m = len(left), len(right)
    i, j = 0, 0
    final = []

    while i<n and j<m:
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
        
    if j < m:
        final += right[j:]
        
    if i < n:
        final += left[i:]

    return final


def merge_sort(array):
    
    n = len(array)
    
    if n <= 1: return array 
    else:
        left, right = merge_sort(array[:n//2]), merge_sort(array[n//2:])
        return merge_op(left, right)



def quick_sort(array, start=0, end=None):
    if end is None: end = len(array)
    if end-start <= 1: return array
    p = random.randint(start, end-1)

    array[p], array[start] = array[start], array[p]
    pivot = array[start]
    i, j = start+1, start+1
    while j < end:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1 
        j += 1
    
    i -= 1
    array[start], array[i] = array[i], array[start]
    
    quick_sort(array, start, i)
    
    i += 1
    while i < end and array[i] == pivot:
        i += 1
    
    quick_sort(array, i, end)

def count_sort(array, key=None):
    key = key or (lambda x: x)
    counts = [[] for _ in range(max(array, key=key) + 1)]
    for a in array:
        counts[key(a)].append(a)
    # print(counts)
    return [x for c in counts for x in c]
        
    
def radix_sort(array):
    num_digits = len(str(max(array))) + 1
    for n in range(1, num_digits):
        array = count_sort(array, key=lambda x: ((x%(10**n)) // (10 ** (n-1))))
        print(array, 'n=', n)
    return array 



def test():
    x = [random.randint(0, 1000) for i in range(20)]
    # x = [0, 1, 3, 2, 5]
    # x = [1, 1, 3, 3, 2, 5, 6,7, 6, 6, 5, 8]
    print('unsorted:', x)

    x_ = copy.deepcopy(x)
    selection_sort(x_)
    print('selection sorted:', x_)
    assert x_ == sorted(x)

    x_ = copy.deepcopy(x)
    x_ = merge_sort(x_)
    print('merge sorted:', x_)
    assert x_ == sorted(x)

    x_ = copy.deepcopy(x)
    quick_sort(x_)
    print('quick sorted:', x_)
    assert x_ == sorted(x)

    x_ = copy.deepcopy(x)
    x_ = count_sort(x_)
    print('count sorted:', x_)
    assert x_ == sorted(x)
    
    x_ = copy.deepcopy(x)
    x_ = radix_sort(x_)
    print('radix sorted:', x_)
    assert x_ == sorted(x)

test()


            

