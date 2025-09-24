# Approach 1: Naive Approach => Time Complexity: O(min(a,b)) Auxiliary Space: O(1)
def simple_gcd(a, b):
    temp = min(a, b)
    for i in range(temp, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1

# Approach 2: Euclidean Approach => Time Complexity: O(min(a,b)) Auxiliary Space: O(1)
def euclidean_gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Approach 3: Optimized Euclidean Approach => Time Complexity: O(log(min(a,b))) Auxiliary Space: O(1)
def optimized_euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Approach 4: Mixed Approach => Time Complexity: O(min(a,b)) Auxiliary Space: O(min(a,b))
def mixed_gcd(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Base case
    if a == b:
        return a

    # a is greater
    if a > b:
        if a % b == 0:
            return b
        return mixed_gcd(a - b, b)
    if b % a == 0:
        return a
    return mixed_gcd(a, b - a)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        (20, 28),    # GCD = 4
        (98, 56),    # GCD = 14  
        (12, 15),    # GCD = 3
        (54, 24),    # GCD = 6
        (7, 13),     # GCD = 1
        (100, 10),   # GCD = 10
        (17, 17),    # GCD = 17
        (0, 5),      # GCD = 5
        (5, 0),      # GCD = 5
        (81, 27)     # GCD = 27
    ]
    
    print("GCD Comparison of All Approaches:")
    print("=" * 70)
    print(f"{'Numbers':<12} {'Naive':<8} {'Euclidean':<10} {'Optimized':<10} {'Mixed':<8}")
    print("-" * 70)
    
    for a, b in test_cases:
        result1 = simple_gcd(a, b)
        result2 = euclidean_gcd(a, b)
        result3 = optimized_euclidean_gcd(a, b)
        result4 = mixed_gcd(a, b)
        
        print(f"({a:2d}, {b:2d})     | {result1:^6} | {result2:^8} | {result3:^9} | {result4:^6}")
    
    # Your original example
    print("\nOriginal Example:")
    a = 98
    b = 56
    print(f"GCD of {a} and {b} is {mixed_gcd(a, b)}")