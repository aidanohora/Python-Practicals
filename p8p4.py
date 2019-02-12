x = 1
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
while x > 0:
    x = int(input("Enter a number: "))
    if x == 0:
        a =+ 1
    if 0<x<=20:
        b =+ 1
    if 20<x<=40:
        c =+ 1
    if 40<x<=60:
        d =+ 1
    if 60<x<=80:
        e =+ 1
    if 80<x<=10:
        f =+ 1
    if x>100:
        g =+ 1

print("Number of numbers that were equal to 0: "+str(a))
print("Number of numbers that were between 0 and 20: "+str(b))
print("Number of numbers that were between 20 and 40: "+str(c))
print("Number of numbers that were between 40 and 60: "+str(d))
print("Number of numbers that were between 60 and 80: "+str(e))
print("Number of numbers that were between 80 and 100: "+str(f))
print("Number of numbers that were equal to 100: "+str(g))
