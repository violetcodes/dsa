'''polynomial multiplication'''
def polynomial_multiplication(x1_coef, x2_coef):
    '''given 3x^2 + 5x + 6 i.e. x1_coef = [3, 5, 6]
    and x^3 + 2x + 5 i.e. [1, 0, 2, 5], returns the coef of multiplied expression'''

    x_res = [0] * (len(x1_coef)-1 + len(x2_coef)-1 + 1)
    for i, x1 in enumerate(x1_coef):
        for j, x2 in enumerate(x2_coef):
            x_res[i+j] += x1*x2
    return x_res

def polynomial_multiplication1(x1_coef, x2_coef):
    '''recursive'''
    l1, l2 = len(x1_coef), len(x2_coef)
    if l1 == 0 or l2 == 0: return []
    if (l1, l2) == (1, 1): return [x2_coef[0]*x1_coef[0], ]
    if (l1, l2) == (2, 1): return [x2_coef[0]*x1_coef[0], x2_coef[0]*x1_coef[1]]
    if (l1, l2) == (1, 2): return [x1_coef[0]*x2_coef[0], x1_coef[0]*x2_coef[1]]
    
    m1, m2 = l1//2, l2//2

    D1, D2 = x1_coef[:m1], x1_coef[m1:]
    E1, E2 = x2_coef[:m2], x2_coef[m2:]

    D1E1 = polynomial_multiplication1(D1, E1)
    D1E2 = polynomial_multiplication1(D1, E2)
    D2E1 = polynomial_multiplication1(D2, E1)
    D2E2 = polynomial_multiplication1(D2, E2)

    R = [0] * (l1 + l2 - 1)

    R[:len(D1E1)] = D1E1
    R[-len(D2E2):] = D2E2
    for i, d in enumerate(D1E2):
        R[m2+i] += d
    for i, d in enumerate(D2E1):
        R[m1+i] += d

    return R

if __name__ == '__main__':

    w = [3, 5, 6, 5, 6]
    v = [1, 0, 1,]

    print(polynomial_multiplication(w, v))
    print(polynomial_multiplication1(w, v))
             
