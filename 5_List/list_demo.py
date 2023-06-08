student_name = ['Student1', 'Student1', 'Student2', 'Student3', 'Student4', 'Student5']
total_student = len(student_name)
print('Total student:', total_student)

second_student_name = student_name[1]
print('Second student:', second_student_name)

last_student_name = len(student_name) - 1
print('Last student:', student_name[last_student_name])

# Check student name exist in list of students
new_student_name = input('Student Name:')

if new_student_name in student_name:
    print("You are in List")
else:
    print("You are not in List")

# print all students name
for name in student_name:
    print('Student Name:', name)

# New student admit
# student_name.append("Student6")
# print(student_name)

print(student_name)

student_name.insert(1, "StudentA")
print(student_name)

count = student_name.count("Student1")
print(count)

student_name.reverse()
print(student_name)

numbers = [1, 22, 33, 1, 122, 33, 44]
numbers.sort(reverse=True)
print(numbers)

numbers.pop(0)
print(numbers)

numbers.remove(22)
print(numbers)

student_name.clear()
print(student_name)
