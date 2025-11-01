#Write a program to check if the user input is a number with power of two or not

def power2(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0

n = int(input("Enter your number"))
if power2(n):
    print("\n", n, "is a power of 2")
else:
    print("\n", n, "is not a power of 2")