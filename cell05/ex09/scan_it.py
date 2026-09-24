import sys

if len(sys.argv) != 3 or sys.argv[1] == "":
    print("none")
else:
    count = sys.argv[2].count(sys.argv[1])
    if count == 0:
        print("none")
    else:
        print(count)
