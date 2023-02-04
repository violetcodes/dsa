def find_peak(array):
    """return peak index if value is bigger or equal than neighbors"""

    if not array:
        return (-1, -1)
    n = len(array)
    if n == 1:
        return (0, array[0])
    if n == 2:
        return (0, array[0]) if array[0] >= array[1] else (1, array[1])
    else:
        n_2 = n//2 
        if array[(n_2 - 1)] <= array[n_2] >= array[n_2+1]:
            return n_2, array[n_2]
        if array[(n_2 - 1)] >= array[n_2]:
            return find_peak(array[:n_2+1])
        if array[(n_2 - 1)] <= array[n_2]:
            i, v = find_peak(array[n_2:])
            return i+n_2, v

# TODO: 2d peak finding

def naive_peak_finder(array):
    # if not array:
    #     return (-1, -1)
    # n = len(array)
    # if n == 1:
    #     return (0, array[0])
    # if n == 2:
    #     return (0, array[0]) if array[0] >= array[1] else (1, array[1])
    
    for i in range(1, len(array)-1):
        if array[i-1] <= array[i] >= array[i+1]:
            return (i, array[i])
    
    if array[0] >= array[1]:
        return (0, array[0])
    if array[-1] >= array[-2]:
        return (len(array)-1, array[-1])


def test_peak_finder():
    array = [0, 0, 0, 0, 0]
    assert find_peak(array) == (2, 0)
    array = []
    assert find_peak(array) == (-1, -1)
    array = [1, 1, 2, 3, 4, 5]
    assert find_peak(array) == (5, 5)
    array = [1, 0, 2]
    assert find_peak(array) == (0, 1)
    array = [2, 2, 3, 3, 5]
    assert find_peak(array) == (2, 3)

    # compare time with naive (is it fast?)
    import random, time 
    array = [_ for _ in range(10_000_000_0)]
    start_time = time.time()
    peak = find_peak(array)[0]
    print(f'peak binary search = {peak} in {time.time() - start_time} seconds')
    print(array[peak-2: peak+2])
    start_time = time.time()
    peak = naive_peak_finder(array)[0]
    print(f'peak naive = {peak} in {time.time() - start_time} seconds')
    print(array[peak-2: peak+2])
    

test_peak_finder()