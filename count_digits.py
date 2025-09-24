"""
Count Digits in a Number
Problem: Count the number of digits in a given integer

Example:
Input: 12345
Output: 5

Input: -789
Output: 3 (ignores negative sign)

Time Complexity: O(d) where d is number of digits
Space Complexity: O(1)
"""

def count_digits(n):
    """
    Count number of digits in an integer
    """
    # Handle negative numbers
    if n < 0:
        n = -n
    
    # Handle zero case
    if n == 0:
        return 1
    
    # Your logic with improvement
    res = 0
    while n > 0:
        n = n // 10
        res = res + 1
    return res

def count_digits_simple(n):
    """
    Simple version with input handling - similar to your approach
    """
    x = abs(n)  # Handle negative numbers
    if x == 0:
        return 1
    
    res = 0
    while x > 0:
        x = x // 10
        res = res + 1
    return res


if __name__ == "__main__":
    # User input version
    x = int(input("Enter a number: "))
    result = count_digits_simple(x)
    print("Count of digits is:", result)
    