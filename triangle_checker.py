x = int(input("side1 :"))
y = int(input("side2 :"))
z = int(input("side3 :"))

if x+y > z and x+z > y and y+z > x :
    print("Triangle formed")
    if x == y == z:
        print(" It is an equaliteral triangle")
    elif x == y or x == z or y == z :
        print("It is an isosceles triangle")
    elif x != y != z :
        print("It is a scalene triangle")
else :
    print ("Not a traiangle")