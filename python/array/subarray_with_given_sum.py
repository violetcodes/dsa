def solve(unsorted_array, subtotal):
    start = 0
    curr = 0
    sum_so_far = 0
    while (curr < len(unsorted_array)):
        if sum_so_far < subtotal - unsorted_array[curr]:
            sum_so_far += unsorted_array[curr]
            curr += 1
        elif sum_so_far > subtotal - unsorted_array[curr]:
            while (start<=curr) and sum_so_far > subtotal - unsorted_array[curr]:
                sum_so_far -= unsorted_array[start]
                start += 1
        else:
            return unsorted_array[start:curr+1]
    return -1

# notes 
# space complexity = O(1)
# time complexity = O(n)
# fails in case of negative numbers


if __name__ == '__main__':
    # testing
    # primary testing 
    def prim_test():
        unsorted_array = [1, 2, 3, 4, 5, 6, 7]
        sum1, sum2, sum3 = 28, 12, 99
        print('unsorted_array:', unsorted_array)
        print(f'for sum1: {sum1}', solve(unsorted_array, sum1))
        print(f'for sum2: {sum2}', solve(unsorted_array, sum2))
        print(f'for sum3: {sum3}', solve(unsorted_array, sum3))
    
    def brute_test():
        # test_parameters
        MAX_ARRAY_LEN = 101
        NUM_ITERS = 1000
        NUM_BATCH_SIZE = 100
        MAX_POSSIBLE_NUM = 100000

        from tqdm import tqdm
        import random, time
        fail = 0
        success = 0
        time_taken = []
        for _ in tqdm(range(NUM_ITERS), 'running test'):
            time_for_iter = 0
            for _ in range(NUM_BATCH_SIZE):
                
                length = random.randint(1, MAX_ARRAY_LEN)
                unsorted_array = random.choices(range(0, MAX_POSSIBLE_NUM), k=length)
                start, end = random.randint(1, length), random.randint(1, length)
                start, end = min(start, end), max(start, end)
                sum1 = sum(unsorted_array[start:end])
                flag = 0
                if random.random() < 0.1:
                    flag = 1
                    sum1 = 98400390923
                start_time = time.time()
                returned = solve(unsorted_array, sum1)
                time_for_iter += time.time() - start_time
                if returned == -1 and flag==0: fail += 1
                if returned != -1 and sum(returned) != sum1: fail += 1
                if (flag == 1 and returned == -1) or ((flag==0) and sum(returned) == sum1):
                    success += 1

            time_taken.append(time_for_iter)
        print('success %:', 1-fail/(NUM_ITERS*NUM_BATCH_SIZE), success/(NUM_ITERS*NUM_BATCH_SIZE))
        print('avg time for each step:', sum(time_taken)/(NUM_BATCH_SIZE*NUM_ITERS) * 1_000_000, 'microsec')

prim_test()
# brute_test()

#brute test is passed. time taken for above setting ~10 microseconds
                



# document
# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
# 
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.
# 
# Output:
# For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.


