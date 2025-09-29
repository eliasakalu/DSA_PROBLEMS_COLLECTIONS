#Iterative Approach: =>   Time Complexity: O(log n)   Auxiliary Space: O(1)
def power(x, n):
    res = 1
    while n > 0:
        if n % 2 != 0:
            res = res * x
        x = x * x
        n = n // 2
    return res

#Driver Code
if __name__ == "__main__":
    x = int(input("Enter the base number (x): "))
    n = int(input("Enter the exponent (n): "))
    print(f"Power of {x}^{n} is:", power(x, n))