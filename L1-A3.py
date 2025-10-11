#Counting the total number of bits 

def NumberOfBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count

n = int(input("Enter a number "))
print(f"Number of bits is {NumberOfBits(n)}")