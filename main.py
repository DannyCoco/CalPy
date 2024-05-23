from calculations import * 

def menu(current = None):
    if current == None:
        pass
    else:
        print(f'OUTPUT: {current}')
    print("-------------------------------------")
    print("     Press 'a' for addition.")
    print("     Press 's' for subtraction.")
    print("     Press 'd' for division.")
    print("     Press 'm' for multiplication.")
    print("     Press 'c' to clear.")
    print("     Press 'q' to quit.")
    print("-------------------------------------")

    choice = input()
    
    # QUIT
    if choice.lower() == 'q':
        return 'end'
    # CLEAR PREVIOUS OUTPUT
    elif choice.lower() == 'c':
        return 'clear'
    # ADD
    elif choice.lower() == 'a':
        if current == None:
            a = valid_nums()
            b = valid_nums()
            result = addition(a,b)
            print(a, ' + ', b, ' = ', result)
            print()
            return result
        else:
            a = current
            b = valid_nums()
            result = addition(a,b)
            print(a, ' + ', b, ' = ', result)
            print()
            return result
    # SUB
    elif choice.lower() == 's':
        if current == None:
            a = valid_nums()
            b = valid_nums()
            result = subtraction(a,b)
            print(a, ' - ', b, ' = ', result)
            print()
            return result
        else:
            a = current
            b = valid_nums()
            result = subtraction(a,b)
            print(a, ' - ', b, ' = ', result)
            print()
            return result
    # DIVIDE
    elif choice.lower() == 'd':
        if current == None:
            a = valid_nums()
            b = valid_nums()
            result = divide(a,b)
            print(a, ' / ', b, ' = ', result)
            print()
            return result
        else:
            a = current
            b = valid_nums()
            result = divide(a,b)
            print(a, ' / ', b, ' = ', result)
            print()
            return result
    # MULTIPLY
    elif choice.lower() == 'm':
        if current == None:
            a = valid_nums()
            b = valid_nums()
            result = multiply(a,b)
            print(a, ' x ', b, ' = ', result)
            print()
            return result
        else:
            a = current
            b = valid_nums()
            result = multiply(a,b)
            print(a, ' x ', b, ' = ', result)
            print()
            return result
    # WRONG COMMAND
    else:
        print('Incorrect command.')
        return current

def calculator():
    print()
    print('CalPy: The Python Calculator')
    print()
    result = 'init'

    while (True):
        # initialize
        if result == 'init':
            result = menu()
        # close application
        elif result == 'end':
            print('Thank you for using CalPy!')
            break
        # clear calculator
        elif result == 'clear':
            result = menu()
        else:
            result = menu(result)

if __name__ == '__main__':
    calculator()