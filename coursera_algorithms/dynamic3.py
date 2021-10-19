'''Knapsack with repetitions problem
Input: Weights w1, . . . , wn and values
v1, . . . , vn of n items; total
weight W (vi
’s, wi
’s, and W are
non-negative integers).
Output: The maximum value of items whose
weight does not exceed W . Each
item can be used any number of
times'''
from collections import Counter

def backtrack(opt_vals, weights, values):
    added = []
    W = len(opt_vals) - 1
    while W >= min(weights):
        for vj, wj in zip(values, weights):
            if opt_vals[W] == (opt_vals[W-wj] + vj) if W-wj >= 0 else 0:
                added.append((vj, wj))
                W -= wj  
                break 
                
    return Counter(added)
            




def optimized_knapsack(W, weights, values):
    l = len(weights)
    wgrid = [0] * (W+1)

    for i in range(1, W+1):
        for vj, wj in zip(values, weights):
            wgrid[i] = max(wgrid[i-wj]+vj if i-wj>=0 else 0, wgrid[i])

    print(wgrid)
    added = backtrack(wgrid, weights, values)
    print(added)

    return dict(val=wgrid[-1])           

'''Knapsack without repetitions problem
Input: Weights w1, . . . , wn and values
v1, . . . , vn of n items; total
weight W (vi
’s, wi
’s, and W are
non-negative integers).
Output: The maximum value of items whose
weight does not exceed W . Each
item can be used at most once'''

def non_repeat_knps(W, weights, values):
    '''idea: if ith item is taken then W-wi with (0..i-1) is optimized solution
    otherwise W is optimized solution with (0..i-1)'''

    grid = [[0]*(W+1) for _ in weights + ['']]
    for i in range(1, W+1):
        for j, (wj, vj) in enumerate(zip(weights, values), 1):
            if wj<=i:
                grid[j][i] = max(grid[j-1][i-wj]+vj, grid[j-1][i])
            grid[j][i] = max(grid[j][i], grid[j-1][i])

    items = backtrack2(grid, weights, values)
    print(items)

    for g in grid: print(' '.join([f"{g1:2}" for g1 in g]))
    return grid[-1][W]

def backtrack2(grid, weights, values):
    select_grid = []
    W = len(grid[0]) - 1
    for j, (wj, vj) in enumerate(list(zip(weights, values))[::-1], 1):
        if wj > W: continue
        if grid[-j-1][W-wj] + vj >= grid[-j-1][W]:
            select_grid.append(wj)
            W -= wj   

    return select_grid








if __name__ == '__main__':
    values = [30, 14, 16, 9]
    weights = [6, 3, 4, 2]
    W = 10

    print(optimized_knapsack(W, weights, values))
    print(non_repeat_knps(W, weights, values))


