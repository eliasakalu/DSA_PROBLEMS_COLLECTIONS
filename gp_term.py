"""
📘 GeeksforGeeks Problem: Geometric Progression Term
🟢 Difficulty: Easy | 🎯 Accuracy: 25.04% | 📊 Submissions: 164K+ | 🏅 Points: 2

🧠 Task:
Given the first two terms `a` and `b` of a Geometric Progression (GP), find the `n`th term.
- The common ratio is calculated as `b / a`.
- Return the value of the `n`th term using integer arithmetic.

📥 Examples:
Input: a = 2, b = 3, n = 1     → Output: 2
Input: a = 1, b = 2, n = 5     → Output: 16
Explanation: Common ratio = 2, so the 5th term is 1 × 2⁴ = 16

📈 Constraints:
-100 ≤ a, b ≤ 100  
1 ≤ n ≤ 9

⏱ Expected Complexities:
Time Complexity: O(log n)  
Auxiliary Space: O(1)
"""

def geometric_term(a, b, n):
    # Calculate the common ratio (integer division assumed)
    r = b // a

    # Compute the nth term using integer exponentiation
    nth_term = a * (r ** (n - 1))

    # Return the result
    return nth_term


if __name__ == "__main__":
    # 🧪 Sample Inputs
    print(geometric_term(2, 3, 1))  # Output: 2
    print(geometric_term(1, 2, 5))  # Output: 16