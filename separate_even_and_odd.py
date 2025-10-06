def identifier(n):
    even, odd = [], []
    for i in n:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return sorted(even), sorted(odd)

if __name__ == "__main__":
    List = [2, 3, 4, 5, 6]
    even, odd = identifier(List)
    print("Even:", even)
    print("Odd:", odd)