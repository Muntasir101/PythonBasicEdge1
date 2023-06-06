# Dictionary is an ordered, modifiable paired(key:value) data type.
user_details = {
    'first_name': 'John',
    'last_name': 'smith',
    'email': 'john.smith@gmail.com',
    'phone': 12345,
    'status': True,
    'tax': 10.5,
    'marks': [20, 44, 50, 80],
    'address': {
        'permanent_address': {
            'house_number': 123,
            'house_name': 'Black House',
            'city': "Dhaka",
            'ward_number': 20
        },
        'present_address': {
            'house_number': '133/A/D',
            'house_name': 'Pearl House',
            'city': "NY",
            'ward_number': 30
        }
    }
}

print(len(user_details))

# Accessing items
print(user_details['first_name'] + ' ' + user_details['last_name'])
print(user_details.get('tax'))

# Adding items
user_details['skills'] = ['python', 'selenium', 'QA']
print(len(user_details))
print(user_details)

user_details['skills'].append("HTML")
print(user_details['skills'])

# get all keys
print(user_details.keys())

# get all values
print(user_details.values())

# get nested values
print(user_details['address']['permanent_address']['ward_number'])

print(user_details.items())

# Get all keys as list
my_list_key = []
for k in user_details.keys():
    my_list_key.append(k)
print(my_list_key)

# get all values as list
my_list_value = []
for v in user_details.values():
    my_list_value.append(v)
print(my_list_value)

