#Checking whether a bit is a set(1) or not
def setOrNot(number, n):
    if 1 & (1 << (n-1)):
        print("SET")
    else:
        print("NOT SET")

number = int(input("Enter your number "))
n = int(input("Enter bit position "))
setOrNot(number, n)