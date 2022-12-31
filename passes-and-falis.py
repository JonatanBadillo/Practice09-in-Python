'''
Develop a program that asks for number of students,then the program has to ask for the notes of the students.
Finally show the number of passed and failed students
'''

number_students = int(input("Introduce the number of students: "))

failed = 0
passed = 0

for i in range (number_students):
    note = float(input("Introduce you final note: "))
    if note <= 5 :
        failed +=1
    else:
        passed +=1

print(f"The number of passed students is: {passed}")
print(f"The number of failed students is: {failed}")

