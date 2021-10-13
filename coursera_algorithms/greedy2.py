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


'''Many children came to a celebration.
Organize them into the minimum possible
number of groups such that the age of any
two children in the same group differ by at
most one year'''

@tester_decorator('group_children', ['ages', 'allowed_diff'])
def group_children(age_of_children, allowed_diff):
    if not age_of_children: return 0
    number_of_groups = 1
    lowest_aged = min(age_of_children)
    age_of_children.remove(lowest_aged)
    while True:
        curr_lowest = min(age_of_children) 
        while age_of_children and (curr_lowest - lowest_aged <= allowed_diff):
            age_of_children.remove(curr_lowest)

            if not age_of_children:
                return number_of_groups

            curr_lowest = min(age_of_children)

        number_of_groups += 1
        lowest_aged = curr_lowest

@tester_decorator('group_children2', ['ages', 'allowed_diff'])
def group_children2(age_of_children, allowed_diff):
    if not age_of_children: return 0
    age_of_children.sort()
    lowest_aged = age_of_children[0]
    i = 0
    num_of_groups = 1
    while i < len(age_of_children):
        if (age_of_children[i] - lowest_aged) <= allowed_diff:
            i += 1
        
        else:
            lowest_aged = age_of_children[i]
            num_of_groups += 1
    
    return num_of_groups

    
        


if __name__ == '__main__':

    children_ages = [3, 2, 1, 3, 5, 5, 8, 9, 6, 2, 4, 5, 6, 11]
    allowed_diff = 2
    group_children(children_ages, allowed_diff)

    children_ages = [3, 2, 1, 3, 5, 5, 8, 9, 6, 2, 4, 5, 6, 11]
    allowed_diff = 2
    group_children2(children_ages, allowed_diff)
