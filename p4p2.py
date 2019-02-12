import math
length = float(input("Enter a value for lengths: "))
area_of_square = length*length
volume_of_cube = length**3
area_of_circle = (length**2)*math.pi
volume_of_sphere = (4/3)*math.pi*(length**3)
volume_of_cylinder = math.pi*(length**2)*length

print("Square area:",area_of_square)
print("Cube volume:", volume_of_cube)
print("Circle area:", area_of_circle)
print("Sphere volume:", volume_of_sphere)
print("Volume cylinder:", volume_of_cylinder)
