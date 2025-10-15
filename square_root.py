'''
Square Root
Given an integer X, find its square root. If X is not a perfect square, then return floor(√x).
Examples : 
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2.
Input: x = 11
Output: 3
Explanation:  The square root of 11 lies in between 3 and 4 so floor of the square root is 3.
'''
#Naive Approach:=>
#Use built in function
import math
def sqroot(x):
    return int(math.sqrt(x)) #you can remove int to see the real sqrt.
#Better Approach:
def sqroot2(x):
    if x==0 or x==1:
        return x
    i=1
    while i*i<=x:
        i+=1
    return i-1
#Efficent Approach:=> Binary Search
def findsqrt(x):
    s=0
    e=x//2
    while s<=e:
        mid=(s+e)//2
        if mid**2==x:
            return mid
        elif mid**2>x:
            e=mid-1
        else:
            s=mid+1
            ans=mid
    return ans


if __name__=="__main__":
    x=87
    print(f"Using Built in:sqroot of {x} is {sqroot(x)}")
    print(f"Using While loop:sqroot of {x} is {sqroot2(x)}")
    print(f"Using Binary Search:sqroot of {x} is {findsqrt(x)}")