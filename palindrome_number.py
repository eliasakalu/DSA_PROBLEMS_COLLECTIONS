def ispalindrome(n) :
    rev = 0
    temp = n
    while temp != 0 :
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    if (rev == n) :
        print(True)
    else :
        print(False)
if __name__== "__main__" :  
    x = int(input("Enter Integer Number To Check If Its Palindrome: "))
    ispalindrome(x)