#Name: Esteak Shapin 
#Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 16, 2022
#This program alters string
inp = input("input: ")

rvs = inp[::-1]
print("user reverse: " + rvs)
print("user reverse upper: " + rvs.upper())

abb = inp.split(" ")
ret = ""
for i in abb:
    ret += i[0]
    
print("user abbreviation: " + ret)