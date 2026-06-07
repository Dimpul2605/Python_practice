salary = int(input("Enter your salary amount : "))
years_of_service = int(input("years of service: "))

if years_of_service >=10:
    bonus = salary*20/100

elif years_of_service >=5:
    bonus = salary*10/100

else:
    bonus = salary*5/100

print (f"your total salary is : {salary + bonus}")

if salary > 50000:
    bonus = bonus + salary*5/100
    print(f"salary with extra bonus is : {salary + bonus}")






