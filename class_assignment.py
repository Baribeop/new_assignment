# Program to calculate the area of a trapezium
class Trapezium():
    
 def __init__(self, a, b, h):
    self.a = a
    self.b = b
    self.h = h
    return
a = float(input("enter value first parallel side of the trapezium: "))
b = float (input("enter value second parallel side of the trapezium: "))
h = float(input("enter value height of the trapezium: "))
trap_val = Trapezium(a, b, h)
# print(trap_val.a)
area_trap = ((trap_val.a + trap_val.b)*trap_val.h)/2
print(area_trap)


