def format_number(number):
    if number.is_integer():
        return str(int(number))
    return str(number)


first_number = float(input("Give me the first number: "))
second_number = float(input("Give me the second number: "))
first_text = format_number(first_number)
second_text = format_number(second_number)

print("Thank you!")
print(f"{first_text} + {second_text} = {format_number(first_number + second_number)}")
print(f"{first_text} - {second_text} = {format_number(first_number - second_number)}")
if second_number == 0:
    print(f"{first_text} / {second_text} = Cannot divide by zero.")
else:
    print(f"{first_text} / {second_text} = {format_number(first_number / second_number)}")
print(f"{first_text} * {second_text} = {format_number(first_number * second_number)}")
