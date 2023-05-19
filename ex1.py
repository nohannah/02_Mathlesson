#1. Asks for the radius and the depth of a cylinder and displays the total volume rounded to three decimal
#points.
#circle area = π * radius2
#volume = circle area * depth
from math import pi
r=int(input("Enter number of radius:"))
d=int(input("Enter dept of cylinder:"))
cicle_area= pi * r**r 
volume= cicle_area * d
print(round(volume , 3))