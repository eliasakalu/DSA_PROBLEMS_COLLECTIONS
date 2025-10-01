"""
✖️ GeeksforGeeks Problem: Multiplication Under Modulo
🟢 Difficulty: Basic | 🎯 Accuracy: 83.95% | 📊 Submissions: 37K+ | 🏅 Points: 1

🧠 Task:
Given three integers `a`, `b`, and `M`, compute the result of the modular multiplication:
→ (a × b) % M

📌 Note:
This operation returns the remainder when the product of `a` and `b` is divided by `M`.
The result will always be an integer between 0 and M−1.

📥 Examples:
Input: a = 5, b = 3, M = 11     → Output: 4
Explanation: 5 × 3 = 15, and 15 % 11 = 4

Input: a = 12, b = 15, M = 7    → Output: 5
Explanation: 12 × 15 = 180, and 180 % 7 = 5

📈 Constraints:
1 ≤ a, b ≤ 10⁴  
2 ≤ M ≤ 10⁹

⏱ Expected Complexities:
Time Complexity: O(1)  
Auxiliary Space: O(1)
"""

def multiplication_under_modulo(a, b, M):
    # Multiply the two numbers
    product = a * b
    # Apply modulo to keep result within [0, M-1]
    result = product % M
    # Return the final result
    return result

#  Driver code for testing
if __name__ == "__main__":
    print(multiplication_under_modulo(5, 3, 11))     
    print(multiplication_under_modulo(12, 15, 7))    