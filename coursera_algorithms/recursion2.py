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

def add_fn(a1, b1):
    a2, b2 = (a1, b1) if len(a1) >= len(b1) else (b1, a1) 

    added = [0] * len(a2)
    for i, d in enumerate(a2):
        added[i] += d 
    
    for i, d in enumerate(b2):
        added[i] += d 

    return added


def karatsuba_mult(x1_coef, x2_coef):
    '''karatsuba algorithms for polynomial multiplication'''
    l1, l2 = len(x1_coef), len(x2_coef)
    if l1 == 0 or l2 == 0: return []
    if (l1, l2) == (1, 1): return [x2_coef[0]*x1_coef[0], ]
    if (l1, l2) == (2, 1): return [x2_coef[0]*x1_coef[0], x2_coef[0]*x1_coef[1]]
    if (l1, l2) == (1, 2): return [x1_coef[0]*x2_coef[0], x1_coef[0]*x2_coef[1]]
    
    flag = 0
    if l1 < l2:
        flag = 1
        x1_coef = [0] * (l2-l1) + x1_coef
    
    elif l2 < l1:
        flag = 2
        x2_coef = [0] * (l1-l2) + x2_coef

    l = len(x2_coef)
    m = l//2

    a1, a2 = x1_coef[:m], x1_coef[m:]
    b1, b2 = x2_coef[:m], x2_coef[m:]

    
    a1b1 = karatsuba_mult(a1, b1)
    a2b2 = karatsuba_mult(a2, b2)

    a_add = add_fn(a1, a2)
    b_add = add_fn(b1, b2)

    cross = karatsuba_mult(a_add, b_add)

    for i, d in enumerate(a1b1):
        cross[i] -= d 
    
    for i, d in enumerate(a2b2):
        cross[i] -= d

    R = [0] * (2*l - 1)
    R[:len(a1b1)] = a1b1
    R[-len(a2b2):] = a2b2 

    for i, d in enumerate(cross):
        R[m+i] += d

    if flag == 1:
        R = R[(l2-l1):]
    
    if flag == 2:
        R = R[(l1-l2):]


    return R


if __name__ == '__main__':

    w = [3, 5, 6, 15, 1]
    v = [1, 0, 13]

    print(polynomial_multiplication(w, v))
    print(polynomial_multiplication1(w, v))
    print(karatsuba_mult(w, v))
             
