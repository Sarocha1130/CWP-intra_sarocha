import sys

if len(sys.argv) != 2:
    print("none")
else:
    letters = ""
    for character in sys.argv[1]:
        if character == "z":
            letters += character
    if letters:
        print(letters)
    else:
        print("none")
