try:
    file_path = "user_details.txt"
    with open(file_path, 'a') as file:
        username = input("Enter Name:")
        email = input("Enter Email:")
        file.write('\n' + "Username:" + username + '\n')
        file.write("Email:" + email)

except Exception as e:
    print("Exception Type: ", type(e).__name__)
