correct_username = "traveller"
correct_password = "simpledimple@26"

username =input("Enter your username : ")
password =input("Enter your password : ")

if username != correct_username:
    print("Wrong Username")
elif password != correct_password:
    print("Wrong Password")
else :
    print("login Successfully! ")
