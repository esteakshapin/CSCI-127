#Name: Esteak Shapin #Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 7, 2022
#This program prints out the ASCII code (+ next 2 letters) from the given input

phrase = input("Enter a phrase: ")

print("letter","ASCII", "next_two_letter")
for s in phrase:
    print("%6c %5i %15c"%(i,ord(i), chr(ord(i)+2)))
