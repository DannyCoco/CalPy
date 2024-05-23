def valid_nums():
    try:
        num = float(input('Enter a number: '))
        return num
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return valid_nums()  # Recursively call the function
    
def addition(a,b):
    answer = a+b
    return answer

def subtraction(a,b):
    answer = a-b
    return answer

def divide(a,b):
    try:
        answer = a/b
        return answer
    except ZeroDivisionError:
        print("You cannot divide by 0. Must choose a new number to divide by.")
        b_new = valid_nums()
        return divide(a,b_new)  # Recursively call the function

def multiply(a,b):
    answer = a*b
    return answer