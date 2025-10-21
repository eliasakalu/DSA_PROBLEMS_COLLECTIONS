# 🚀 Naive Approach 1: Using sorted()
# Time Complexity: O(n log n) | Space Complexity: O(n)
num = [6, 5, 2, 3, 1]
sorted_num = sorted(num, reverse=False)  # Set reverse=True for descending order
print(f"🔢 Sorted Array Using sorted(): {sorted_num}")

# 🚀 Naive Approach 2: Using .sort()
# Time Complexity: O(n log n) | Space Complexity: O(1)
num = [6, 5, 2, 3, 1]
num.sort(reverse=False)  # Set reverse=True for descending order
print(f"🔢 Sorted Array Using .sort(): {num}")

# 🚀 Naive Approach 3: Custom sort using key function
def myKey(val):
    return len(val)  # Sort by length of each string

list_ = ["Elias", "Cat", "Doom"]
custom_sorted = sorted(list_, key=myKey)  # Result: ['Cat', 'Doom', 'Elias']
print(f"🔠 Sorted by Length: {custom_sorted}")

# 🚀 Naive Approach 4: Sorting Custom Objects by Attribute
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def sort_by_x(p):
    return p.x  # Sort by x-coordinate

points = [Point(1, 5), Point(10, 5), Point(3, 8)]
points.sort(key=sort_by_x)

print("📍 Points Sorted by x-coordinate:")
for pt in points:
    print(f"({pt.x}, {pt.y})")

