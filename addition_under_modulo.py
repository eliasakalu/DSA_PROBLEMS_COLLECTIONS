"""
➕ GeeksforGeeks Problem: Addition Under Modulo
🟢 Difficulty: Basic | 🎯 Accuracy: 65.19% | 📊 Submissions: 63K+ | 🏅 Points: 1 | ⏱ Avg Time: 10m

🧠 Task:
Given three integers `a`, `b`, and `M`, compute the result of the modular addition:
→ (a + b) % M

📌 Note:
Modular operations return the remainder when divided by `M`.
The result will always be an integer between 0 and M−1.

📥 Examples:
Input: a = 10, b = 20, M = 3     → Output: 0
Explanation: (10 + 20) % 3 = 30 % 3 = 0

Input: a = 100, b = 13, M = 107  → Output: 6
Explanation: (100 + 13) % 107 = 113 % 107 = 6

📈 Constraints:
1 ≤ a, b, M ≤ 10⁹

⏱ Expected Complexities:
Time Complexity: O(1)  
Auxiliary Space: O(1)
"""
def addition_under_modulo(a,b,M):
    total=a+b
    result=total%M
    return result #Instead of these 3 lines of code we can use return (a+b)%M.

if __name__ == "__main__":
    print(addition_under_modulo(10, 20, 3))     # Output: 0
    print(addition_under_modulo(100, 13, 107))
