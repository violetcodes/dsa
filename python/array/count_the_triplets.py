def solve(array, verbose=0):
    counts = 0
    for ith, i in enumerate(array):
        for jth, j in enumerate(array[:ith]):
            for kth, k in enumerate(array[:jth]):
                if i+j==k or i+k==j or j+k==i:
                    if verbose!=0:
                        print('-->', i, j, k)
                    counts += 1

    return counts 

def solve_efficient(array, verbose=0):
    counts = 0
    array = sorted(array)
    for ith, i in enumerate(array):
        if ith < 2: continue
        start, end = 0, ith - 1
        while start < end:
            if array[start] + array[end] == i:
                # counts += 1
                if verbose!=0:
                    print('-->', array[start], array[end], i)
                
                
                if array[end] == array[start]:
                    leng = end - start + 1
                    counts += int(leng*(leng-1)/2)
                    if verbose!=0: print(f'counts increment-{leng}: ', int(leng*(leng-1)/2))                    
                    break

                left_continuous = 1
                right_continuous = 1
                end_start, start_start = end-1, start+1 
                while array[end_start] == array[end]:
                    end_start-=1
                    right_continuous += 1
                while array[start_start] == array[start]:
                    start_start+=1
                    left_continuous += 1
                

                counts += left_continuous * right_continuous

                if verbose!=0: print('counts increment: ', left_continuous*right_continuous)

                start, end = start_start, end_start               
                
                

                # if array[end-1] == array[end]:
                #     end -= 1
                # else: start += 1    
                # start += 1
                
            elif array[start] + array[end] < i: start += 1
            else: end -= 1

    return counts 
        


# time O(n^3)

if __name__ == "__main__":
    def prim_test():
        # array = [1, 5, 3, 2]
        # print(solve_efficient(array), 2)
    
        array = [85, 15, 17, 34, 46, 34, 17, 17, 48]
        print(sorted(array))
        print(solve_efficient(array, 0), 6)

        # # array = [49, 52, 3, 3, 54]
        # # print(solve_efficient(array, 1), 2)

        # array = [104, 81, 74, 82, 5, 47, 23, 126, 44, 53, 64, 44, 40, 55]
        # print(sorted(array))
        # print(solve_efficient(array, 1), 4)
    
    # prim_test()

    import random
    MAX_LENGTH = 100
    MAX_N = 1000
    TRUE_PROB = 0.3

    
    
    def simulate_example():
        length = random.randint(1, MAX_LENGTH)
        array1 = random.choices(range(MAX_N), k=length//3)
        array2 = random.choices(range(MAX_N), k=length//3)
        array3 = [sum(j) for j in zip(array1, array2) if random.random()<TRUE_PROB]
        array = array1 + array2 + array3
        
        #only non repeating passes 100%
        # array = list(set(array))

        sorted_array = sorted(array)
        counts = []
        for ith, i in enumerate(sorted_array):
            for jth, j in enumerate(sorted_array):
                for kth, k in enumerate(sorted_array):
                    if ith == jth or jth == kth or kth == ith: continue

                    if (i+j==k or j+k==i or i+k==j):
                        ind_tup = tuple(sorted([ith, jth, kth]))
                        if ind_tup not in counts: counts.append(ind_tup)
        
        counts = [[sorted_array[i] for i in j] for j in counts]          

        # counts = [(ith, jth, ith+jth) for i, ith in enumerate(sorted_array[:-1]) for j, jth in enumerate(sorted_array[i+1:])  if ith+jth in sorted_array[i+j+1:]]
        array = random.sample(array, k=len(array))
        # print('ans:')
        # print(*counts, sep='\n')

        counts1 = len(counts)
        return array, counts1, counts
         
        
    # array, ans = simulate_example()
    # print(array)
    # print(ans)

    def brute_test():
        # get n examples
        NUM_EXAMPLES = 10000
        PRINT_NUM = 5
        import time
        from tqdm import tqdm 
        first_algo_times = 0
        second_algo_times = 0
        success1 = 0
        success2 = 0
        sim_time = 0
        for _ in tqdm(range(NUM_EXAMPLES), 'running test'):
            # new_example
            start_time = time.time()
            array, ans, trips = simulate_example()
            sim_time += time.time() - start_time
            
            start_time = time.time() 
            ans1 = solve(array)
            first_algo_times += time.time() - start_time
            
            start_time = time.time()
            ans2 = solve_efficient(array)
            second_algo_times += time.time() - start_time

            if ans1 == ans:
                success1 += 1
            if ans2 == ans:
                success2 += 1

            if PRINT_NUM > 0:
                if ans1 != ans:
                    print(array)
                    print('valid ones')
                    print(trips)
                    print('\nfirst algo fails')
                    print(f'true sum: {ans}, output sum: {ans1}')
                    print('calling again with verbose')
                    solve(array, 1)
                    print('\n**********\n')
                    PRINT_NUM -= 1
                
                if ans2 != ans:
                    print(array)
                    print('valid ones')
                    print(trips)
                    print('\nsecond algo fails')
                    print(f'true sum: {ans}, output sum: {ans2}')
                    print('calling again with verbose')
                    solve_efficient(array, 1)
                    print('\n*********\n')
                    PRINT_NUM -= 1

            else: break



                

        
        first_algo_times, second_algo_times, success1, success2 = [
            i/NUM_EXAMPLES for i in [first_algo_times, second_algo_times, success1, success2]]
        
        print(f'first algo success_rate % {success1} while for second algo it is % {success2}')
        print(f'first algo on avg took % {first_algo_times*10**6 } mic-s wheras second took {second_algo_times* 10**6} mic-s')

        print('simulation_time', sim_time/NUM_EXAMPLES)
    brute_test()




# document
# Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

# running test: 100%|████████████████████████████████████████████████| 10000/10000 [03:54<00:00, 42.62it/s]
# first algo success_rate % 1.0 while for second algo it is % 1.0
# first algo on avg took % 2723.7024784088135 mic-s wheras second took 146.70121669769287 mic-s
# simulation_time 0.02057078354358673
