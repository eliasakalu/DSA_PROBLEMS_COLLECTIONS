#Naive LCM Approach
def naive_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    res = max(a, b)
    while True:
        if res % a == 0 and res % b == 0:
            return res
        res += 1

#Efficient LCM Approach using GCD
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def efficient_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

# --- Test Runner ---
if __name__ == "__main__":
    test_cases = [(0, 0), (2, 0), (0, 4), (14, 16)]
    print("LCM Calculation Results:\n")
    for a, b in test_cases:
        naive = naive_lcm(a, b)
        efficient = efficient_lcm(a, b)
        print(f"Inputs: ({a}, {b})")
        print(f"  Naive LCM     → {naive}")
        print(f"  Efficient LCM → {efficient}")
        print("-" * 30)