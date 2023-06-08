"""
1. TypeError
2. ValueError
3. indexError
4. keyError
5. FileNotFoundError
6. importError
7. ZeroDivisionError
8. MemoryError
"""

"""
#  ZeroDivisionError
number1 = 10
number2 = 0

try:
    result = number1 / number2
    print(result)
except Exception as e:
    print("Exception: ", e)

print("program end")
"""
"""
# typeError
try:
    number = input("Enter a number:")
    result = number + 2
    print(result)
except Exception as e:
    print("Exception: ", e)

print("program end")
"""

"""
# ValueError
try:
    age = int(input("Enter age: "))
    if age < 0:
        print("Your age is negative :", age)
    else:
        print("Your age is :", age)
except Exception as e:
    print(e)
    print("Exception Type: ", type(e).__name__)

print("program end")
"""
try:
    numbers = [122, 33, 44, 2]
    print(numbers[4])
except Exception as e:
    print("Exception Type: ", type(e).__name__)

print("program end")
