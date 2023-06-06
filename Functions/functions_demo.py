# Defining function

def greeting():
    print("Hello")


# calling function
greeting()
for i in range(5):
    greeting()


# Function without arguments
def summation():
    number1 = 20
    number2 = 10
    print(number1 + number2)


summation()


# Function with arguments
def subtraction(number1, number2):
    result = number1 - number2
    print(result)


subtraction(50, 40)


# function with return values
def multiplication(number1, number2):
    return number1 * number2


multiple_result = multiplication(20, 10)
print(multiple_result)


def divide(number1, number2):
    return number1 / number2


divide_result = divide(50, 10)
print(divide_result)

final_result = multiplication(20, 20) - divide(50, 25)
print(final_result)


# function with default parameters
def multiple_default_parameter(number1=20, number2=10):
    return number1 * number2


print(multiple_default_parameter(60, 50))


# function with multiple parameters : *args represents tuple
def calculate_sum(*args):
    total = sum(args)
    return total


print(calculate_sum(20, 10, 30, 40))


# function with doc string
def square(a):
    """Returns the square root:"""
    return a ** 2


print(square.__doc__, square(2))
