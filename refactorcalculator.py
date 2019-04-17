import string
# refactoring https://github.com/sobolevn/python-code-disasters/blob/master/python/my_first_calculator.py

if 3/2 == 1:  # Because Python 2 does not know maths
        input = raw_input  # Python 2 compatibility

# Takes a number x and a number y and a sign, and calculated x sign y
def calculator(x, y, sign):
    if (sign == '+'):
        return x + y
    if (sign == '-'):
        return x - y
    if (sign == '*'):
        return x*y
    if (sign == '/'):
        return x/y

def isSign(sign):
    return sign == '+' or sign == '-' or sign == '/' or sign == '*'

# Takes a string of math equation and calculates it
def advancedCalculator(equation, sign='+', acc=0, i = 0):
    # check if reached end of equation
    if i >= len(equation):
        return acc

    curr = equation[i]
    # TODO: check if reached a parantheses: if so, evaluate that
    if (curr == '('):
        pass
    if curr == ' ':
        return advancedCalculator(equation, sign, acc, i+1)
    # check if reached a sign, if so: set sign to that
    if (isSign(curr)):
        sign = curr
        return advancedCalculator(equation, sign, acc, i+1)
    # if a number: use sign before it to evaluate
    assert curr.isnumeric()
    acc = calculator(acc, int(curr), sign)
    return advancedCalculator(equation, sign, acc, i+1)


if __name__ == "__main__":
    print('Welcome to this calculator!')
    print('It can add, subtract, multiply and divide numbers')
    # num1 = int(input('Please choose your first number: '))
    # sign = input('What do you want to do? +, -, /, or *: ')
    # num2 = int(input('Please choose your second number: '))
    # print('RESULT: %d'%calculator(num1, num2, sign))

    equation = input("Give me a equation without parantheses, using +, -, /, or *")
    print('RESULT: %d'%advancedCalculator(equation))