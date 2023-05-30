# age = 20

"""
age = 20
age = 20
age = 20
age = 20
"""

# Case Sensitive
age = 20
Age = 20

# variable reassignment
number1 = 30
number1 = 40

# Never use any python keyword as variable name

"""
variable types:
1. Numeric types: integer, float
age = 20
discount = 100.22
2. Text types: string
my_city = "Dhaka"
3. Boolean types: True or False
account_status = True
4. Sequence types: list, tuple
5. Mapping types: dictionary
6. Set types: set
"""
my_age = 20
discount = 100.22
my_city = "Dhaka"
your_city = 'Ny'
account_status = True

# tuple
students_name = ('Student1', 'Student2', 'Student3', 12, True, ['Student34'])

# list
students_id = [20, True, "Student", 122.2, students_name]
students_name2 = (students_id)

# key: pair value
# Nested dictionary
user_details = {
    "user_id": 20,
    "user_name": "Student1",
    "address": {
        "present_address": {
            "area": "Dhaka",
            'road': 123,
            "house_number": {
                "old_house_number": 123,
                "new_house_number": 222
            }
        },
        "permanent_address": {
            "area": "NY",
            'road': 1
        }
    },
    "email": "Student@mail.com",
    "marks": [12, 323, 44, 56]
}

# set
city = {"dhaka", "ny", "tokyo"}


print(city)