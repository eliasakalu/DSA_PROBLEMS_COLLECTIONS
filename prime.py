# Naive Approach: => Time Complexity: O(n) Auxiliary Space: O(1)
def isPrime(n):
    if n==1:
        return "One is neither prime nor composite"
    for i in range(2,n):
        if n%i==0:
            return "Composite (Not Prime)"
        
    return "Prime"


# Efficient Approach : => Time Complexity: O(sqrt(n)) Auxiliary space: O(1)
def isPrime_Efficent(n):
    if n==1:
        return "One is neither prime nor composite"
    i=2
    while i*i<=n:
        if n%i==0:
            return "Composite (Not Prime)"
        i+=1
    return "Prime"

# More Efficient Approach: => Time complexity: O(sqrt(n)) Auxiliary space: O(1)
def isPrime_Most_Efficent(n):
    if n==1:
        return "One is neither prime nor composite"
    if n==2 or n==3:
        return "Prime"
    if n%2==0 or n%3==0:
        return "Composite (Not Prime)"
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return "Composite (Not Prime)"
        i+=6
    return "Prime"

if __name__ == "__main__":
    # Test cases
    test_numbers = [1, 2, 3, 4, 5, 7, 9, 11, 15, 17, 25, 29, 49, 97]
    
    print("🔍 PRIME NUMBER CHECKER - ALL METHODS COMPARISON")
    print("=" * 60)
    print(f"{'Number':<8} {'Naive':<20} {'Efficient':<20} {'Most Efficient':<20}")
    print("-" * 60)
    
    for num in test_numbers:
        result1 = isPrime(num)
        result2 = isPrime_Efficent(num)
        result3 = isPrime_Most_Efficent(num)
        
        print(f"{num:<8} {result1:<20} {result2:<20} {result3:<20}")
    
    print("=" * 60)
    print("\n📊 PERFORMANCE COMPARISON:")
    print("Naive Method: O(n) - Checks all numbers from 2 to n-1")
    print("Efficient Method: O(√n) - Checks up to square root of n") 
    print("Most Efficient: O(√n) - Uses 6k±1 optimization pattern")
    
    # Demo with a larger number
    print("\n🎯 DEMO WITH LARGER NUMBER (n = 1009):")
    large_num = 1009
    print(f"Number: {large_num}")
    print(f"Naive Method: {isPrime(large_num)}")
    print(f"Efficient Method: {isPrime_Efficent(large_num)}")
    print(f"Most Efficient: {isPrime_Most_Efficent(large_num)}")