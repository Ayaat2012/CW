#Checking if a number is even or odd

def IsEvenOdd(n):
    if (n ^ 1 == n +  1):
        return True
    else:
        return False
    
num = int(input("Enter your desired number "))

if IsEvenOdd(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")