#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if j > i:
            print(i, end="")
            if i == 8 and j == 9:
                print(j)
                break
            print(j, end=", ")
