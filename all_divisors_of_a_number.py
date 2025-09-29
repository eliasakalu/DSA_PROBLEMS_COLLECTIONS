#Naive Solution: =>   Time Complexity : O(n)   Auxiliary Space : O(n)
def printDivisors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

#Efficient Approach: =>   Time Complexity : O(sqrt(n))   Auxiliary Space : O(1)
def printDivisorsEfficent(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                print(i, end=" ")
            else:
                print(i, n // i, end=", ")
        i += 1

if __name__ == "__main__":
    number = int(input("Enter the number you want to check: "))
    print(f"The factors of {number} using Naive approach are: {' '.join(map(str, printDivisors(number)))}")
    print(f"The factors of {number} using Efficient approach are:", end=" ")
    printDivisorsEfficent(number)