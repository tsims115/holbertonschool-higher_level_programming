#!/usr/bin/python3
for i in range(100):
    print(i) if i == 99 else print("{:0>2}".format(i), end=", ")
