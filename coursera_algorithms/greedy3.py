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

'''Fractional knapsack
Input: Weights w1, . . . , wn and values
v1, . . . , vn of n items; capacity W .
Output: The maximum total value of
fractions of items that at into a
bag of capacity W '''
@tester_decorator("max_frac_value", ['w', 'v', 'C'])
def max_frac_value(w, v, C):
    val_per_weight = [(w1, v1, v1/w1) for v1, w1 in zip(v, w)]
    val_per_weight = sorted(val_per_weight, key=lambda x: -x[-1])

    total_val, i = 0, 0
    for w1, v1, ratio in val_per_weight:
        w_add = min(C, w1)
        total_val += w_add * ratio
        C -= w_add 
        if C == 0:
            return total_val
    
    return total_val

if __name__ == '__main__':

    w = [5, 12, 10, 17]
    v = [13, 10, 15, 11]
    C = 15

    max_frac_value(w, v, C)


def add_fn(a1, b1):
    a2, b2 = (a1, b1) if len(a1) >= len(b1) else (b1, a1) 

    added = [0] * len(a2)
    for i, d in enumerate(a2):
        added[i] += d 
    
    for i, d in enumerate(b2):
        added[-(i+1)] += d 

    return added