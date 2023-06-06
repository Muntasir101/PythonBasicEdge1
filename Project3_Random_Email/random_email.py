import random
import string


def generate_random_email(length):
    domain_name = ['gmail', 'yahoo', 'icloud', 'hotmail']
    postfix = ['.com', '.org', '.bd', '.edu']
    characters = string.ascii_letters + string.digits
    domain_select = random.choice(domain_name)
    postfix_select = random.choice(postfix)
    random_sting = ''.join(random.choice(characters) for _ in range(length))
    return random_sting + "@" + domain_select + postfix_select


email_list = []

for i in range(5):
    email_list.append(generate_random_email(5))

print(email_list)
