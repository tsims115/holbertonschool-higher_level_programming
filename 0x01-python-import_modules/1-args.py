#!/usr/bin/python3
def main():
    import sys
    count = 0
    args = len(sys.argv) - 1
    print("{}".format(args), end=" ")
    if args == 1:
        print("argument:")
    elif args == 0:
        print("arguments.")
    else:
        print("arguments:")
    for i in sys.argv:
        if count != 0:
            print("{}: {}".format(count, i))
        count += 1
if __name__ == "__main__":
    main()
