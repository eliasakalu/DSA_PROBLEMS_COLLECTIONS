"""
GeeksforGeeks Problem: Exactly 3 Divisors
Difficulty: Easy | Accuracy: 22.85% | Submissions: 130K+

🧠 Task:
Given a positive integer n, count how many numbers ≤ n have exactly 3 divisors.

📌 Insight:
A number has exactly 3 divisors if and only if it is the square of a prime.
Example: 4 → divisors are [1, 2, 4] → count = 3

📥 Examples:
Input: n = 6     → Output: 1   (Only 4 has 3 divisors)
Input: n = 10    → Output: 2   (4 and 9)

📈 Constraints:
1 ≤ n ≤ 10⁹

⏱ Expected Complexities:
Time Complexity: O(n^(3/4))
Auxiliary Space: O(1)
"""

def isprime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def exactly3Divisors(n):
    count = 0
    i = 2
    while i * i <= n:
        if isprime(i):
            count += 1
        i += 1
    return count

# --- User Can Test ---
if __name__ == "__main__":
    try:
        n = int(input("Enter a number (1 ≤ n ≤ 10⁹): "))
        if n < 1 or n > 10**9:
            print("❌ Input out of range. Please enter a number between 1 and 10⁹.")
        else:
            print("✅ Count of numbers with exactly 3 divisors:", exactly3Divisors(n))
    except ValueError:
        print("❌ Invalid input. Please enter a valid integer.")