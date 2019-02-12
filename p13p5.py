#Program to illustrate scoping in Python
def f(x, b):
    """Function that adds 1 to its arguements and prints it out"""
    print("In function f: ")
    x += 1
    y = 1
    a = 2
    b += 10
    print("x is", x)
    print("y is", y)
    print("z is", z)
    print("a is", a)
    print("b is", b)
    return x

x, y, z, a, b = 5, 10, 15, 20, 25

print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)

z = f(x, b)

print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)
