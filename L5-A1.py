#Swapping two numbers

def method1(a, b):
    a = a^b
    b = a^b
    a = a^b
    print("After swapping, a =", a, "and b =", b)

def method2(a, b):
    a = (a&b) + (a|b)
    b = a+(~b)+1
    a = a+(~b)+1
    print("After swapping again, a =", a, "and b =", b)

method1(10, 20)
method2(10, 20)

# ~b = -b -1
# ~b = -b +1