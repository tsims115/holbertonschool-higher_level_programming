#!/usr/bin/python3
def main():
    import sys
    count = 0
    print("{}".format(len(sys.argv) - 1), end=" ")
    if len(sys.argv) == 1:
        print("argument:")
    else:
        print("arguments:")
    for i in sys.argv:
        if count != 0:
            print("{}: {}".format(count, i))
        count += 1
if __name__ == "__main__":
    main()
