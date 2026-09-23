#!/usr/bin/env python3

first_number = float(input("Enter the first number:\n"))
second_number = float(input("Enter the second number:\n"))
result = first_number * second_number

if first_number.is_integer():
    first_number = int(first_number)
if second_number.is_integer():
    second_number = int(second_number)
if result.is_integer():
    result = int(result)

print(f"{first_number} x {second_number} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
