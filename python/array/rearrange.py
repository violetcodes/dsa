
# fix this using A = A + B*N, B = A // N method (storing two at one place)

if __name__ == "__main__":
    def prim_test():
        arr = list(range(1, 7))
        arr = [2, 4, 8, 9, 12, 40, 50]
        # arr = [1969, 2677, 3142, 4631, 4764, 5748, 6476, 6487]

        print(arr)
        sol = solve(arr, verb=1)
        print(*sol, sep=' ')

    prim_test()
