# printing 1 to 10 numbers
# number = 0
# while number < 10:
#     number = number + 1
#     print(number)

# printing 10 to 1 numbers
# number = 11

# while number > 0:
#     number = number - 1
#     print(number)

# printing even numbers
# number = 1

# while number <=20:
#     if number %2 ==0:
#         print(number)
#     number = number +1

# printing odd numbers

# number = 1

# while number <=20:
#     if number %2 != 0:
#         print(number)
#     number = number +1

# printing sum of numbers 1 to 100

# number = 1

# total = 0

# while number <= 100:
#     total = total + number
#     number = number + 1

# print(total)


#adding even numbers
# number = 1

# total = 0

# while number <=50:
#     if number %2 ==0:
#         total = total + number
       
#     number = number+1
# print(total)

#adding odd numbers
# number = 1

# total = 0

# while number <=50:
#     if number %2 !=0:
#         total = total + number
       
#     number = number+1
# print(total)

# multiplication table of 7

# number = 1

# while number <=10:
#     print(f"7 X {number} = {7*number}")
#     number = number + 1

# counting numbers from 1 to 100

# number = 1
# count =0
# while number <=100:
#     count = count+1
#     number = number +1

# print(count)

# square of 10 natural numbers

# number = 1

# while number <=10:
#     print(number,"->",number*number)
#     number = number + 1

# factorial of a given number
# number = int(input("Enter your number to find out factorial: "))

# factorial = 1

# while number >0:
#     factorial = number*factorial
#     number = number -1

# print(factorial)

# reversing a number

# number =(int(input("Enter your number to get reversed number: ")))

# last_digit = 0

# reversed_number = 0

# while number >0:
#     last_digit = number % 10
#     reversed_number = reversed_number*10 + last_digit
#     number = number//10
    
# print(reversed_number)

#checking whether a number is palindrome or not

# number =(int(input("Enter your number to get reversed number: ")))

# original_number = number

# reversed_number = 0

# while number >0:
#     last_digit = number % 10
#     reversed_number = reversed_number*10 + last_digit
#     number = number//10
    
# print(reversed_number)

# if original_number == reversed_number:
#     print("it is a palindrome.")
# else:
#     print("not a palindrome.")

# sum of the digits of a given number
# number = int(input("Enter your number to sum the digits: "))

# sum = 0

# while number >0:
#     last_digit = number % 10
#     sum += last_digit
#     number = number//10

# print(sum)

# counting the digits in a number
# number = int(input("Enter your number to count the digits: "))

# count = 0

# while number >0:
#     last_digit = number % 10
#     count += 1
#     number = number//10

# print(count)

# product of the digits of a given number
# number = int(input("Enter your number to product the digits: "))

# product = 1

# while number >0:
#     last_digit = number % 10
#     product *=  last_digit
#     number = number//10

# print(product)

# checking whether a number is armstorong or not

# number = int(input("Enter your number to check if it is an armstrong or not: "))

# temp = number

# count = len(str(number))

# total = 0

# while temp>0:
#     last_digit = temp%10
#     total = total + last_digit**count
#     temp //=10

# if total == number:
#     print("It is an Armstrong.")
# else:
#     print("Not an Armstrong")


# printing Fibonnaci series
# n = int(input("Enter your number to get fibonnaci series: "))

# first_number = 0
# second_number = 1

# while n > 0:
#     print(first_number)
#     previous_number = first_number + second_number
#     second_number = previous_number
#     first_number = second_number
#     n = n-1


# calculating the power of number without using **
# base = int(input("Enter your base number: "))

# exponent = int(input("Enter your exponent number: "))

# result = 1

# while exponent>0:
#     result = result*base
#     exponent = exponent-1

# print(result)


number = int(input("Enter your number to find largest digit: "))

largest_digit = 0

while number >0:
    last_digit = number % 10
    if last_digit > largest_digit:
        largest_digit = last_digit
        
    number //=10


print(largest_digit)

