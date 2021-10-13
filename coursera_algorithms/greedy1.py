
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
 
    


@tester_decorator("largest_number")
def largest_number(list_of_digits):
    '''given list of digits, find largest number that can be made from these digits'''
    largest_ordered = []
    while list_of_digits:
        m = max(list_of_digits)
        largest_ordered.append(m)
        list_of_digits.remove(m)
    
    s, c = 0, len(largest_ordered)
    for d in largest_ordered:
        s += d*10**(c-1)
        c -= 1
    
    return s


'''Input: A car which can travel at most L
kilometers with full tank, a source
point A, a destination point B and
n gas stations at distances
x1 ≤ x2 ≤ x3 ≤ · · · ≤ xn in
kilometers from A along the path
from A to B.
Output: The minimum number of refills to
get from A to B, besides refill at A.'''
@tester_decorator("car_refueling", ['gst_stations', 'full_tank_cap'])
def car_refueling(gas_stations, full_tank_cap):
    '''if car can go to the next station with remaining fuel without refueling at current station then then fuel at here'''
    min_fueling = 1
    remaining_fuel = full_tank_cap
    last_place = 0
    for i, x in enumerate(gas_stations[:-1]):
        remaining_fuel -= x - last_place
        if gas_stations[i+1] - x > full_tank_cap:
            return 'IMPOSSIBLE'
        if remaining_fuel < gas_stations[i+1] - x:
            print(f'fueling at: {x}')
            min_fueling += 1
            remaining_fuel = full_tank_cap 
        last_place = x
    return min_fueling

if __name__ == '__main__':

    test1 = [3, 1, 5, 7, 7, 9]
    test2 = [4, 5, 2, 1, 0, 9, 8]
    largest_number(test1)
    largest_number(test2)

    full_tank_cap = 400
    stops = [0, 200, 375, 475, 577, 776, 950, 976]
    car_refueling(stops, full_tank_cap)


