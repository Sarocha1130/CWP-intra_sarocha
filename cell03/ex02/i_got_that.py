prompt = "What you gotta say? : "

while True:
    message = input(prompt)
    if message == "STOP":
        break
    prompt = "I got that! Anything else? : "
