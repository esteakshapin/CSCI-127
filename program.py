#Name: Esteak Shapin #Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 7, 2022
#This program collects first and last name and formats it

fullName = input("Enter name in format firstName lastName: ")

[firstName, lastName] = fullName.split(" ")

print("name in LASTNAME, firstName format: %s %s" % (
    lastName.upper(), firstName
))

username = input("Enter user name of email: ")
print("email: %s@hunter.cuny.edu" % (username.lower()))
