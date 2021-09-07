#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if  number[len(number)-1] > 5:
  comparision = "and is greater than 5"
elif number[len(number)-1] == 0:
  comparision = "and is 0"
elif number[len(number)-1] < 6 and number[len(number)-1]  !== 0:
  comparision = "and is less than 6 and not 0"
  
print("Last digit of {:d} is {:d} {}".format(number, number[len(number)-1]))
