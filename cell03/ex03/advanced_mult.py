import sys

if len(sys.argv) != 1:
    print("none")
else:
    number = 0
    while number <= 10:
        print(f"Table de {number}:", end="")
        multiplier = 0
        while multiplier <= 10:
            print(f" {number * multiplier}", end="")
            multiplier += 1
        print()
        number += 1
