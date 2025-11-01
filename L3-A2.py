#Finding which number in an array apears odd number of times
#Assumption: Only one number apears odd number of times

def oddOcurring(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res

arr = []
n = int(input("Enter array size"))
while(n):
    num = int(input("Enter number"))
    arr.append(num)
    n-=1
print("Odd Ocurring number is", oddOcurring(arr))