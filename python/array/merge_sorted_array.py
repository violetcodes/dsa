# Expected Time Complexity:  O((n+m) log(n+m))
# Expected Auxilliary Space: O(1)
import time, random
from tqdm import tqdm 

def solve(a1, a2):
    m, n = len(a1), len(a2)
    result = [0] * (m + n)
    i, j, k = 0, 0, 0
    while (i < m+n):
        while (j < m and k < n):
            if a1[j] > a2[k]:
                result[i] = a2[k]
                k += 1

            else:
                result[i] = a1[j]
                j += 1

            i += 1
        
        if j == m:
            while k < n:
                result[i] = a2[k]
                k += 1
                i += 1
                
            
        elif k == n:
            while j < m:
                result[i] = a1[j]
                j += 1
                i += 1

    return result

# try this without extra space (inplace)    


def brute_force(a1, a2):
    return sorted(a1 + a2)

def simulate_examples():
    MAX_LEN = 10000
    MAX_INT = 1000


    m, n = random.randint(1, MAX_LEN), random.randint(1, MAX_LEN)
    a1, a2 = random.choices(range(MAX_INT), k=m), random.choices(range(MAX_INT), k=n)

    return sorted(a1), sorted(a2)




if __name__ == "__main__":
    def prim_test():
        a1 = [1, 3, 5, 7]
        a2 = [0, 2, 6, 8, 9]
        print(solve(a1, a2))
        print(brute_force(a1, a2))

    # prim_test()


    def brute_force_test():
        NUM_TEST_ITERS = 100
        time1, time2, success = 0, 0, 0

        for _ in tqdm(range(NUM_TEST_ITERS), 'running brute test'):
            a1, a2 = simulate_examples()

            start_time = time.time()
            solution1 = solve(a1, a2)
            time1 += time.time() - start_time

            start_time = time.time()
            solution2 = brute_force(a1, a2)
            time2 += time.time() - start_time



            if solution1 == solution2:
                success += 1

        print(f'success % {success/NUM_TEST_ITERS}')
        print(f'took time {time1} for {NUM_TEST_ITERS}')
        print(f'brute force took {time2}')

    brute_force_test()


# Given two sorted arrays arr1[] and arr2[] of sizes N and M in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements. 
