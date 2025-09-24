#Naive Approach -> Simple but bad algorithm
def simple_find_trailing_zeros(n):
    def factorial(x):
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

    x = factorial(n)
    count = 0
    while x > 0:
        if x % 10 == 0:
            count += 1
            x //= 10
        else:
            break
    return count

#Efficient Approach -> Time Complexity: O(log5n)    Auxiliary Space: O(1)
def find_trailing_zeros(n):
    if n < 0:
        return -1
    #Initialize result
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

if __name__ == "__main__":
    ## Both can do same but choose the efficent one. To see which algorithm is fast
    import time
    n = int(input("Enter whole number to find its factorial trailing zeros:"))

    start = time.time()
    print(f"Count of trailing 0s in {n}! is {find_trailing_zeros(n)}")
    end = time.time()

    start2 = time.time()
    print(f"Count of trailing 0s in {n}! is {simple_find_trailing_zeros(n)}")
    end2 = time.time()

    print()
    print(f"Naive Algorithm Time: {end2 - start2:.6f} seconds")
    print(f"Efficient Algorithm Time: {end - start:.6f} seconds")
   