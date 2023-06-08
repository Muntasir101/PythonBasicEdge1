try:
    file_path = "user_details.txt"
    with open(file_path, 'r') as file:
        content = file.read()

    print(content)
except Exception as e:
    print("Exception Type: ", type(e).__name__)
