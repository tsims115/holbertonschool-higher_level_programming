#!/usr/bin/python3
for i in range(90):
    if (i / 10) < (i % 10):
        if i == 89:
            break
        print("{:0>2}".format(i), end=", ")
print("{:0>2}".format(i))
