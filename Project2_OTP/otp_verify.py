import random
import string


def generate_random_otp(length):
    numbers = string.digits
    random_numbers = ''.join(random.choice(numbers) for _ in range(length))
    return random_numbers


random_OTP = generate_random_otp(5)
print(random_OTP)

user_input_otp = input('Enter your OTP: ')
if random_OTP == user_input_otp:
    print("Success")
else:
    print("OTP Error")
