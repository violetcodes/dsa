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

'''Change problem
Input: An integer money and positive
integers coin1, . . . , coind .
Output: The minimum number of coins with
denominations coin1, . . . , coind
that changes money'''
@tester_decorator('coin change', ['money', 'changes'])
def coin_change(m, changes):
    # changes.sort()
    min_changes = [0] * (m+1)
    for i in range(1, m+1):
        m1 = 100
        for c in changes:
            if c > i: break            
            m1 = min(m1, min_changes[i-c] + 1)
        min_changes[i] = m1
    return min_changes[m]


def coin_change2(m, changes, known=None):
    known = known or {}
    if m in known: return known[m]

    r = min([coin_change2(m-c, changes, known) + 1 for c in changes if c <=m], default=0)
    known[m] = r
    return r

if __name__ == '__main__':
    changes = [25, 20, 10, 5, 1]
    money = 40 

    # changes = [1, 5, 6]
    # money = 10

    changes.sort()
    coin_change(money, changes)

    tr = {}
    print(coin_change2(money, changes, tr))
    print(tr)
