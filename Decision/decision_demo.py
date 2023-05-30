pass_mark = 40
student_mark = int(input("marks: "))

# Nested conditions
if student_mark >= pass_mark:
    if 41 <= student_mark <= 50:
        print('Grade D')
    elif 51 <= student_mark <= 60:
        print('Grade C')
    elif 61 <= student_mark <= 70:
        print('Grade B')
    elif 71 <= student_mark <= 80:
        print('Grade A-')
    elif 81 <= student_mark <= 90:
        print('Grade A')
    elif 91 <= student_mark <= 100:
        print('Grade A+')
    else:
        print("Invalid marks")
else:
    print("Fail")


