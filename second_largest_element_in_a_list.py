# Efficient Approach
# Time Complexity: O(n) | Auxiliary Space: O(1)

def getSecMaxEfficient(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None
    for x in l:
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar is None or x > slar:
                slar = x
    return slar

#  Naive Approach
# Time Complexity: O(n) | Auxiliary Space: O(1)

def getMax(l):
    if not l:
        return None
    res = l[0]
    for i in range(len(l)):
        if l[i] > res:
            res = l[i]
    return res

def getSecMaxNaive(l):
    if len(l) <= 1:
        return None
    lar = getMax(l)
    slar = None
    for i in l:
        if i != lar:
            if slar is None:
                slar = i
            else:
                slar = max(i, slar)
    return slar

# 🧪 Driver Code
if __name__ == "__main__":
    List = [10, 5, 20, 8, 20]

    print("🐢 Naive Second Max:", getSecMaxNaive(List))
    print("⚡ Efficient Second Max:", getSecMaxEfficient(List))