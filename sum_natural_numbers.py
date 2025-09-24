#Naive Approach - Beginner
def findSum(n) :
	sum = 0
	x = 1
	while x <=n :
		sum = sum + x
		x = x + 1
	return sum
#Efficent Approach -Advanced 
def findNumSum(n) :
	return n * (n + 1) / 2

#Both can do same but the first one is O(n) Time complexity and the second one is O(1)	
n = 5
print (findSum(n))
print (findNumSum(n))