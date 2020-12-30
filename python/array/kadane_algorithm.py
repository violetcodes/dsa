def solve(array):
    start = 0
    stop = 0
    sofar_max = -100000
    cum_sum = 0
    for i, val in enumerate(array):
        cum_sum += val
        if sofar_max <= cum_sum:
            sofar_max = cum_sum
            stop = i
        sofar_max = max(sofar_max, cum_sum)
        if cum_sum < 0:
            start = i
            cum_sum = 0
        
    return start, stop, sofar_max

def brute_force(array):
    cum_sum = -10000
    for i in range(len(array)):
        for j in range(i, len(array)):
            cum_sum = max(cum_sum, sum(array[i:j+1]))
    return cum_sum

if __name__ == "__main__":
    def prim_test():
        array = [1, 2, 3, -2, -5, 6, 5]
        print('array:', array)
        start, stop, sofar_max = solve(array)
        print(f'start {start}, stop {stop}, max {sofar_max}')
        print(f'bruteforce: {brute_force(array)}')

        array = [-1,-2,-3,-4]
        print('array:', array)
        start, stop, sofar_max = solve(array)
        print(f'start {start}, stop {stop}, max {sofar_max}')
        print(f'bruteforce: {brute_force(array)}')

    prim_test()     



# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

