#Naive Approach: =>   Time Complexity: O(n)   Auxiliary Space: O(1)
def power(x, n):
    counter = 1
    store = 1
    while counter <= n:
        store *= x
        counter += 1
    return store

#Efficient Approach: =>   Time Complexity: O(log n)   Auxiliary Space: O(log n)
def power_efficient(x, y):
    if x == 0 and y == 0:
        return "Undefined"
    if y == 0 and x != 0:
        return 1
    temp = power_efficient(x, y // 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp

#Driver Code
if __name__ == "__main__":
    x = int(input("Enter the base number (x): "))
    n = int(input("Enter the exponent (n): "))
    print(f"Naive Power of {x}^{n} is:", power(x, n))
    print(f"Efficient Power of {x}^{n} is:", power_efficient(x, n))