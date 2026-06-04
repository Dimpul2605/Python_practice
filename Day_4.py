x = int(input("Enter your first number : "))
y = int(input("Enter your second number : "))
z = int(input("Enter your third  number : "))

if x > y and x > z:
     print("your first number is largest number.")
     if y > x and y > z:
          print("your second number is largest number.")
          if z > x and z > y:
               print("your third number is largest.")
               if x == y == z:
                    print("All numbers are equal.")

