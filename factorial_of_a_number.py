#Iterative Approach:    Time Complexity: O(n)  Auxiliary Space: O(1)
def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
#Recursive Approach     Time Complexity: O(n)   Space Complexity: O(n)
def fact2(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

if __name__ == "__main__":
    number = int(input("Enter Whole Numbers:"))
    print(fact(number)) #or you can use fact2(number)