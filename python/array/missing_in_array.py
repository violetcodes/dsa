def solve(array):
    sum_ = 0
    for i in array:
        sum_ += i
    l = len(array) + 1
    sum1 = (l *(l+1))//2
    return sum1 - sum_
# O(n)


def brute_force(array):
    rng = range(1, len(array)+2)
    print(rng)
    return [i for i in rng if i not in array][0]
# O(n) with hashing overhead

def simulate_examples():
    MAX_LEN = 10000

    import random 
    to_drop = random.randint(1, MAX_LEN)
    array = list(range(MAX_LEN)).remove(to_drop)
    return array 

if __name__ == "__main__":

    def prim_test():
        array = [1,2,3,5]
        print(solve(array), brute_force(array), 4)
    
    prim_test()

# Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.