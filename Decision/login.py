default_username = 'admin'
default_password = "123456"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == default_username or password == default_password:
    print("Login successful")
else:
    print("Login failed")