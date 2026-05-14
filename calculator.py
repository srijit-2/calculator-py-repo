num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Enter choice from 1–4")
entered_choice = input("1.Addition  2.Subtraction  3.Multiplication  4.Division : ")

if entered_choice == '1':
    print("The sum is:", num1 + num2)

elif entered_choice == '2':
    print("The difference is:", num1 - num2)

elif entered_choice == '3':
    print("The product is:", num1 * num2)

elif entered_choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The quotient is:", num1 / num2)

else:
    print("Invalid input")
