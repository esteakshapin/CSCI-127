#Name: Esteak Shapin #Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 7, 2022
#This program prints out the ASCII code (+ next 2 letters) from the given input

phrase = input("Enter a phrase: ")

print("letter \tASCII \tnext_two_letters")
for s in phrase:
    print("%s \t %s \t%s,%s" % (
        s, ord(s), chr(ord(s) + 1), chr(ord(s) + 2)
    ))