age = int(input("Enter your age: "))
Day = input("Enter if it is Weekday or Weekend : ")

if age < 12:
    ticket_price = 100
elif age <= 59:
    ticket_price = 200
else :
    ticket_price = 150

print (f"your ticket price is : {ticket_price}")

if Day == "weekend":
    weekend_ticket_price = ticket_price + 50
    print(f"your weekend ticket price is : {weekend_ticket_price}")

print("Enjoy The Movie!")