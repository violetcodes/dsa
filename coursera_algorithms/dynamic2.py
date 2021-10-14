'''edit distance, sequence alignment'''

def backtracking(array, string1, string2):
    i = len(string1)
    j = len(string2)
    path = [[],[],[]]
    while i>0 and j>0:
        curr = array[i][j]
        prev1, prev2, prev3 = array[i-1][j-1], array[i-1][j], array[i][j-1] 

        if prev1 == min(prev1, prev2, prev3):
            path[0].append(string1[i-1])
            path[1].append(string2[j-1])
            path[2].append('M' if prev1==curr else 'X')
            i-=1; j-=1
        
        elif prev2 == min(prev1, prev2, prev3):
            path[0].append(string1[i-1])
            path[1].append('_')
            path[2].append('I')
            i-=1
        
        elif prev3 == min(prev1, prev2, prev3):
            path[0].append('_')
            path[1].append(string2[j-1])
            path[2].append('D')
            j-=1
    
    if i>0:
        path[0].extend(list(string1)[:i][::-1])
        path[1].extend(['_']*i)
        path[2].extend(['I']*i)

    else:
        path[1].extend(list(string2)[:j][::-1])
        path[0].extend(['_']*j)
        path[2].extend(['D']*j)


    path = list(map(lambda x: ' '.join(x), [path[0][::-1], path[1][::-1], path[2][::-1]]))
    return path
        






def alignment_game(string1, string2):
    array_2d = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]
    array_2d[0] = list(range(len(string2)+1))
    for i, ar in enumerate(array_2d):
        ar[0] = i

    for i in range(1, len(string1)+1):
        for j in range(1, len(string2)+1):
            if string1[i-1] == string2[j-1]:
                bk = array_2d[i-1][j-1]
            
            else:
                bk = array_2d[i-1][j-1] + 1

            array_2d[i][j] = min(array_2d[i-1][j]+1, array_2d[i][j-1]+1, bk)



    path = backtracking(array_2d, string1, string2)
    print(*path, sep='\n')

    return array_2d[-1][-1]
    





if __name__ == '__main__':
    string1 = 'editing'
    string2 = 'distance'

    # string1 = ''

    score = alignment_game(string1, string2)
    print('score:', score)