number = int(input("Enter your number : "))

if number > 0:
     print("Positive")
     if number %2 == 0:
          print("Even")
          if number %4 == 0:
               print("Even and Divisible by 4!")
    
     elif number %2 != 0:
          print("Odd")
          if number %5 == 0:
               print("Odd and Divisible by 5!")
elif number < 0:
     print("Negative") 
else: 
     print("Zero")

