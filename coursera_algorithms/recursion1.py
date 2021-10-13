def tester_decorator(name_of_function, params=None):
    def dec(f):
        def fn(*args):
            print(f'testing {name_of_function} with follwoing parameters')
            for i, arg in (zip(params, args) if params is not None else enumerate(args)): 
                print(f'arg -> {i}: {arg}')
            result = f(*args)
            print(f'result obtained: {result}')
            print()
            return result
        return fn
    return dec 


'''Input: An array A with n elements.
A key k.
Output: An index, i, where A[i] = k.
If there is no such i, then
NOT_FOUND'''


# @tester_decorator("linear_search", ['array', 'key'])
def linear_search(array, key):
    if not array : return 'NOT FOUND'
    curr = 1
    if array[0] == key:
        return curr - 1
    
    else:
        r = linear_search(array[1:], key)
        if r == 'NOT FOUND':
            return r 
        else:
            return curr + r

'''Searching in a sorted array
Input: A sorted array A[low . . . high]
(∀low ≤ i < high : A[i] ≤ A[i + 1]).
A key k.
Output: An index, i, (low ≤ i ≤ high) where
A[i] = k.
Otherwise, the greatest index i,
where A[i] < k.
Otherwise (k < A[low]), the result is
low − 1.'''

def binary_search(s_array, key):
    high = len(s_array)
    low = 0

    if high == low: return 'NOT FOUND'
    mid = ( low + high ) // 2
    if s_array[mid] == key:
        return mid 
    
    elif s_array[mid] < key:
        s_array = s_array[mid+1:]
        r = binary_search(s_array, key)
        if r == 'NOT FOUND': return r 
        else: 
            r = mid+1 + r
            return r 
        
    elif s_array[mid] > key:
        s_array = s_array[:mid]
        r = binary_search(s_array, key)
        if r == 'NOT FOUND': return r
        else:
            return r
    
    


    
    



if __name__ == '__main__':

    w = [5, 12, 10, 17]
    key = 10
    print(linear_search(w, key))
    w.sort()
    print(w, key)
    print(binary_search(w, key))
