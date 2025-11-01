#Program to find two numbers that are odd ocurring

def TwoOdd(arr, size):

    # XORof2 will hold XOR of 2 odd ocurrings numbers
    XORof2 = arr[0]

    # These will hold 2 odd ocurring numbers
    x = 0
    y = 0

    # This will hold the rightmost set bit from XORof2
    setbit = 0

    for i in range(1, size):
        XORof2 = XORof2 ^ arr[i]

    setbit = XORof2 & ~(XORof2 - 1)

    # If number is having set bit at location we need then XOR it with x, else y
    for i in range(size):
        if (arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("Two odd elements are ", x, "and", y)

#Create an empty array
arr = []

#Take array size and elements as input
arr_size = int(input("Enter size of array"))
for i in range(0, arr_size):
    z = int(input("Enter element"))
    arr.append(z)

TwoOdd(arr, arr_size)