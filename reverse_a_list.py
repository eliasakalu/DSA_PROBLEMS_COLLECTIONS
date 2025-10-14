# 🔁 List Reversal Techniques
# - reverse() method: Reverses the original list in place
# - reversed() function: Returns a new reversed iterator
# - slicing [::-1]: Creates a new reversed list using slicing

def reverse(l):
    s, e = 0, len(l) - 1
    while s < e:
        l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1

# 🧪 Driver Code
if __name__ == "__main__":
    List = [1, 2, 3, 4, 5]
    reverse(List)
    print("🔁 Reversed:", List)