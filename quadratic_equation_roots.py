"""
GeeksforGeeks Problem: Quadratic Equation Roots
Difficulty: Basic | Accuracy: 12.78% | Submissions: 250K+ | Points: 1

🧠 Task:
Given a quadratic equation ax² + bx + c = 0, find its roots.
- If the equation has real roots, return the floor value of each root in decreasing order.
- If the roots are imaginary, return -1. (Driver code will print "Imaginary")

📥 Examples:
Input: a = 1, b = -2, c = 1     → Output: 1 1
Input: a = 1, b = -7, c = 12    → Output: 4 3

📈 Constraints:
-10³ ≤ a, b, c ≤ 10³

⏱ Expected Complexities:
Time Complexity: O(1)
Auxiliary Space: O(1)
"""
import math
def rootfinder(a,b,c):
    discrimnant=b*b-4*a*c
    if discrimnant<0:
        return [-1]
    sqrt_d=math.sqrt(discrimnant)
    r1,r2=math.floor((-b+sqrt_d)/(2*a)),math.floor((-b-sqrt_d)/(2*a))
    return [max(r1,r2),min(r1,r2)]

# Driver code for testing
if __name__ == "__main__":
    # Example inputs
    test_cases = [(1, -2, 1), (1, -7, 12), (1, 2, 5)]

    for a, b, c in test_cases:
        result = rootfinder(a, b, c)
        if result == [-1]:
            print("Imaginary")
        else:
            print(*result)
