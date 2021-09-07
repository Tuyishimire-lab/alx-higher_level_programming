#!/usr/bin/python3
for i in range(1,10):
    for j in rang(i+1, 10):
        if (i is not 8) and (j is not 9):
            print("{}{}, ".format(i, j),end="")
        else:
            print("{}{}".format(i, j))
