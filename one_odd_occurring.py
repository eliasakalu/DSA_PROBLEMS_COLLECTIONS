'''
 Problem: Find elements that occur an odd number of times in an array

📥 Input:
    [4, 3, 4, 4, 5, 5, 3, 3]

📤 Output:
    [4, 3]  # Elements that appear an odd number of times
'''

#Naive Approach:=> Time Complexity: O(n^2) Auxiliary Space: O(1)
def find_odd_naive(arr):
    odd_occurrence_collection = []
    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        if count % 2 != 0:
            if i in odd_occurrence_collection:
                continue
            odd_occurrence_collection.append(i)
    return odd_occurrence_collection

#XOR-Based Approach (Only works if ONE element occurs odd times):=>  Time Complexity: O(n)  Auxiliary Space: O(1)
def find_single_odd_xor(arr):
    res = 0
    for num in arr:
        res=res^num
    return res  # Only valid if exactly one element occurs odd times

#Driver Code
if __name__ == "__main__":
    arr = [4, 3, 4, 4, 5, 5, 3, 3]
    arr2 = [4,3,4,4,4,5,5,3,3] # array from single odd xor since that algorthm solves a single number in list that oddly occured.
    print(f"Original array: {arr}")
    print(f"Odd occurrences (Naive): {find_odd_naive(arr)}")
    print(f"Single odd occurrence (XOR): {find_single_odd_xor(arr2)}")