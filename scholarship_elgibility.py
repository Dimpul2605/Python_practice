marks = int(input("Enter your marks : " ))
family_income = int(input("Enter your family_income : "))

if marks >= 90 and family_income <= 300000 :
    print("Full Scholarship!")
elif marks >=75 and marks <=89 and family_income <= 500000 :
    print("Half Scholarship")
elif marks >=90 and family_income > 500000:
    print("Merit Certificate Only")

else :
    print("Not Eligible")