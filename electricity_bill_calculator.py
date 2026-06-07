units = int(input("Enter your units : "))
bill = 0

if units <=100:
    bill = units*2
elif units <=200:
    bill = units*5
elif units <=300:
    bill = units*8
elif units >300:
    bill = units*10

print (f"your electricity bill final_amount : {bill}")

tax = bill*18/100

if bill > 5000:
    final_bill = bill + tax
    print(f"Tax amount : {tax}")
    print(f"your electricity bill final_amount : {final_bill}")
    

