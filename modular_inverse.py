"""
🔁 GeeksforGeeks Problem: Modular Inverse
🟢 Difficulty: Easy | 🎯 Accuracy: 43.0% | 📊 Submissions: 87K+ | 🏅 Points: 2

🧠 Task:
Given two integers `n` and `m`, find the smallest modular multiplicative inverse of `n` under modulo `m`.
→ Return the smallest integer `x` such that (x × n) % m == 1
→ If no such `x` exists, return -1

📥 Examples:
Input: n = 3, m = 11     → Output: 4
Explanation: (4 × 3) % 11 = 12 % 11 = 1

Input: n = 10, m = 17    → Output: 12
Explanation: (12 × 10) % 17 = 120 % 17 = 1

📈 Constraints:
1 ≤ n ≤ 10⁴  
1 ≤ m ≤ 10⁵

⏱ Expected Complexities:
Time Complexity: O(m)  
Auxiliary Space: O(1)
"""

def modular_inverse(n, m):
    # Try all values from 1 to m-1 to find the inverse
    for i in range(1,m):
        if (i*n)%m==1:
            return i
    # No inverse found
    return -1

# 🚀 Driver code for testing
if __name__ == "__main__":
    print(modular_inverse(3, 11))   
    print(modular_inverse(10, 17))  