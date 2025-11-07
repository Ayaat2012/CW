#Write a program to divide 2 numbers without using the division operator

def divide(divident, divisor):
    sign = (-1 if((divident < 0) ^ (divisor < 0)) else 1)
    divident = abs(divident)
    divisor = abs(divisor)

    quotient = 0
    temp = 0

    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= divident):
            temp += divisor << i
            quotient |= 1 << i

    if sign == -1:
        quotient = -quotient
    return quotient

a = int(input("Enter a for a/b")) #divident
b = int(input("Enter b for a/b")) #divisor
print("Result of", a, "/", b, "is", divide(a, b))