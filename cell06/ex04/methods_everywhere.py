import sys


def shrink(text):
    print(text[:8])


def enlarge(text):
    print(text + "Z" * (8 - len(text)))


if len(sys.argv) == 1:
    print("none")
else:
    for parameter in sys.argv[1:]:
        if len(parameter) > 8:
            shrink(parameter)
        elif len(parameter) < 8:
            enlarge(parameter)
        else:
            print(parameter)
