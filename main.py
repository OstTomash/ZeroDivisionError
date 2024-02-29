def divide_numbers(f_number, s_number):
    """
    Function to divide two numbers and handle ZeroDivisionError and ValueError
    :param f_number:string
    :param s_number:string
    :return:float
    """
    result = 0

    try:
        f_number = int(f_number)
        s_number = int(s_number)
    except ValueError:
        print('Entered wrong numbers, will take default values (1, 1)')
        f_number = 1
        s_number = 1

    try:
        result = f_number / s_number
    except ZeroDivisionError:
        print('Entered wrong second number, will take default value "1"')
        s_number = 1
    finally:
        result = f_number / s_number

    return result


first_number = input('Enter first number: ')
second_number = input('Enter second number: ')

print(divide_numbers(first_number, second_number))
