import sys

if len(sys.argv) != 3:
    print("none")
else:
    first_number = int(sys.argv[1])
    last_number = int(sys.argv[2])
    numbers = list(range(first_number, last_number + 1))
    print(numbers)
