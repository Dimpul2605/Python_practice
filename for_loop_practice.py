# #printing 1 to 10 numbers
# for numbers in range(1,11):
#     print(numbers)

# # printing 10 to 1 numbers
# for numbers in range(10,0,-1):
#     print(numbers)

# # printing even numbers
# for numbers in range (2,21,2):
#     print(numbers)
    

# #printing odd numbers
# for numbers in range (1,21,2):        
#     print(numbers)

# # printing multiplication of 5 table
# num = 5

# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# # printing 1 to 20 tables
# for i in range (1,21):
#     print()
#     for j in range(1,11):
#         print(i, "x", j, "=", i*j)

# #printing sum of 1 to 100
# number = 0
# for num in range (1,101):
#     number = number + num

# print(number)

# # printing sum of even numbers
# number = 0
# for num in range (0,51,2):
#     number = number + num 

# print(number)

# #counting numbers between 1 to 100
# count = 0
# for num in range (1,101):
#     count = count + 1

# print(count)


# #factorial of a number

# result = 1
# n = int(input("Enter a number for factorial : "))
# for number in range (1,n):
#     result = result *number

# print(f"factorial of ypur number is {result}")

# #counting digits in a number
# number = input("Enter your number to count digits: ")

# count = 0
# for num in number:
#     count = count + 1

# print(f"No of digits in your number is {count}")

# #sum of digits in a number
# number = input("Enter your number for sum of digits in a number: ")

# sum = 0

# for num in number:
#     num = int(num)
#     sum = num + sum

# print(f"sum of your digits for your number is {sum}")

# # palindrome
# number = input("Enter a number to check palindrome or not: ")
# reversed_num = ""

# for digit in number:
#     reversed_num = digit + reversed_num
    
# print(reversed_num)

# if reversed_num == number:
#     print("it is a palindrome")
# else:
#     print("not a palindrome")

# #Arm strong number
# number = input("Enter your number to check armstrong number or not: ")

# digits = len (number)
# total = 0

# for digit in number:
#     total = total + int(digit)**digits

# if total == int(number):
#     print("Armstrong number")
# else:
#     print("Not an armstrong number")


#finding factors of a number
# number = int(input("Enter your number to find factors of it: "))

# for num in range(1,number+1):
#     if number % num == 0:
#         print(num)

#checking prime number or not

# number = int(input("Enter a number: "))

# if number <= 1:
#     print("Not Prime")
# else:
#     is_prime = True

#     for num in range(2, number):
#         if number % num == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")

# # -----------OR-------------
# number = int(input("Enter a number: "))

# count = 0

# for num in range(1, number + 1):
#     if number % num == 0:
#         count = count + 1

# if count == 2:
#     print("Prime")
# else:
#     print("Not Prime")
    
# printing prime numbers from 1 to 100

# for num in range(2,101):
#     count = 0
#     for number in range (1,num+1):
#         if num % number ==0:
#             count = count+1

#     if count == 2:
#         print(num)
    
#printing the largest digit in a number

number = input("Enter a number to find largest number: ")

largest = 0

for digit in number:
    if int(digit) > largest:
        largest = int(digit)

print("Largest digit is:", largest)