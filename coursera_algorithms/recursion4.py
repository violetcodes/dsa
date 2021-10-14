'''sorting algorithm'''
def tester_decorator(name_of_function, params=None):
    def dec(f):
        def fn(*args):
            print(f'testing {name_of_function} with follwoing parameters')
            for i, arg in (zip(params, args) if params is not None else enumerate(args)): 
                print(f'arg -> {i}: {arg}')
            result = f(*args)
            print(f'result obtained: {result}')
            print()
        return fn
    return dec 

@tester_decorator('selection sort')
def selection_sort(u_array):
    '''selection sort'''

    for i, _ in enumerate(u_array):
        for j, _ in enumerate(u_array[i:]):
            if u_array[i] > u_array[i+j]:
                u_array[i], u_array[i+j] = u_array[j+i], u_array[i]
    
    return u_array

def merge_op(p1, p2):
    '''merging two sorted array'''
    r = [0] * (len(p1)+len(p2))
    i = j = c = 0

    while i < len(p1) and j < len(p2):
        if p1[i] <= p2[j]:
            r[c] = p1[i]
            c += 1; i += 1
        else:
            r[c] = p2[j]
            c += 1; j += 1

    r[c:] = p2[j:] if j < len(p2) else p1[i:]
    return r 

def merge_sort(u_array):
    '''merge sort'''
    if len(u_array) <= 1: return u_array
    l = len(u_array)
    p1, p2 = u_array[:l//2], u_array[l//2:]
    p1 = merge_sort(p1)
    p2 = merge_sort(p2)

    u_array = merge_op(p1, p2)
    return u_array


if __name__ == '__main__':
    unsorted = [3, 2, 1, 0, 2, 3, 1, 7, 9, 12, 7, 8, 6, 11]
    cpy = unsorted[:]
    selection_sort(cpy)

    cpy2 = unsorted[:]
    cpy2 = merge_sort(cpy2)
    print(cpy2)

