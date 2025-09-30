# --- Naive Approach ---
# ✅ No math library used.
# ❌ But for very large n (like 10000!) it becomes slow and uses a lot of memory
def digits_factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return len(str(fact))

# --- Efficient Approach ---
# ✅ Uses Stirling’s Approximation
# ✅ O(1) Time and Space
# --- Stirling’s Approximation ---
# n! ≈ sqrt(2πn) * (n/e)^n
#
# Take log base 10 to avoid big numbers:
# log10(n!) ≈ n*log10(n/e) + (1/2)*log10(2πn)
#
# Number of digits = floor(log10(n!)) + 1
# Number of digits = floor(n*log10(n/e)+(1/2)*log10(2πn))) + 1

import math

def digits_factorial_efficient(n):
    if n == 0 or n == 1:
        return 1
    e = math.e
    pi = math.pi
    digits = math.floor(n * math.log10(n / e) + 0.5 * math.log10(2 * pi * n)) + 1
    return digits

# --- User Input ---
n = int(input("Enter a number to find digits in its factorial: "))
print("Naive Approach:", digits_factorial(n))
print("Efficient Approach:", digits_factorial_efficient(n))