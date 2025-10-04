def addition(number1, number2):
    return number1 + number2

def multiplication(number1, number2):
    return number1 * number2

def subtraction(number1, number2):
    return number1 - number2

def division(number1, number2):
    return number1 / number2

while True:
    number1 = int(input('Enter the first number: '))
    operation = input('Choose the operation (+, -, *, /): ')
    number2 = int(input('Enter the second number: '))

    match operation:
        case '+':
            result = addition(number1, number2)
        case '-':
            result = subtraction(number1, number2)
        case '*':
            result = multiplication(number1, number2)
        case '/':
            if number2 == 0:
                print("You can't divide a number by 0!")
            else:
                result = division(number1, number2)
        case _:
            print('Unrecognized operation. Only +, -, * or / are accepted')

    if operation in ['+', '-', '*', '/']:
        if number2 != 0 or operation != '/':
            print(f'{number1} {operation} {number2} = {result}')
    again = input('Would you like to continue (y/n)? ').lower()
    while again not in ['y', 'n']:
        print('Maybe you typed it wrong')
        again = input('Would you like to continue (y/n)? ')
    if again == 'y':
        continue
    else:
        break
