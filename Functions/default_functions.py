import random

"""
number = -5
print(abs(number))

numbers = [2.2, 30, 44, 50, 22]
print(len(numbers))
print(max(numbers))
print(min(numbers))

print(sorted(numbers))
"""

"""
# generate random float number between 0 and 1
random_number_float = random.random()
print(random_number_float)

# generate random number
random_number_int = random.randint(0, 10)
print(random_number_int)

# generate random number within given list
my_numbers = [100, 200, 300, 400, 500, 600, 700]
random_element = random.choice(my_numbers)
print(random_element)

# shuffle elements
random.shuffle(my_numbers)
print(my_numbers)
"""

# Random String
import string


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_sting = ''.join(random.choice(characters) for _ in range(length))
    return random_sting


print(generate_random_string(8))


def generate_random_email(length):
    domain_name = ['gmail', 'yahoo', 'icloud', 'hotmail']
    postfix = ['.com', '.org', '.bd', '.edu']
    characters = string.ascii_letters + string.digits
    domain_select = random.choice(domain_name)
    postfix_select = random.choice(postfix)
    random_sting = ''.join(random.choice(characters) for _ in range(length))
    return random_sting + "@" + domain_select + postfix_select


print(generate_random_email(5))
