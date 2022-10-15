#Name: Esteak Shapin #Email: esteak.shapin50@myhunter.cuny.edu
#Date: September 7, 2022
#This program generates a map

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

fileName = input("Enter file name: ")
img = plt.imread(fileName)
countSnow = 0
threshold = float(input("Enter threshold: "))

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        #Check if red, green, and blue are > t:
          if (img[row,col,0] > threshold) and (img[row,col,1] > threshold) and (img[row,col,2] > threshold):
               countSnow = countSnow + 1

print("Number of white pixels", countSnow)
print("percent of white pixels: ", countSnow / (img.shape[0] * img.shape[1]) * 100)