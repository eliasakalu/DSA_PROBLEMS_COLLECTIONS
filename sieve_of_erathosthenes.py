#Sieve of Eratosthenes: =>   Time Complexity : O(n*log(log(n)))   Auxiliary Space : O(n)
def seiveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for i in range(2, n + 1):
        if prime[i]:
            print(i, end=" ")

#Driver Code
if __name__ == "__main__":
    number = int(input("Enter the number up to which you want primes: "))
    print(f"Prime numbers up to {number} are:", end=" ")
    seiveOfEratosthenes(number)