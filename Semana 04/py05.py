#!/usr/bin/python3
#Vídeo 05 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print("student =", student,"\nstudent['name'] =", student['name'],"\nstudent['courses'] =", student['courses'])
print("student.get('name') =", student.get('name'),"\nstudent.get('phone') =", student.get('phone'))
print("student.get('phone', 'Not Found') =", student.get('phone', 'Not Found'))

student1 = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student1['phone'] = '555-5555'
student1['name'] = 'Jane'

print("student['phone'] = '555-5555'\nstudent['name'] = 'Jane'\nstudent =", student1)
print("student.get('phone', 'Not Found') =", student1.get('phone', 'Not Found'))

student2 = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student2.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

print("student.update(update({'name': 'Jane', 'age': 26, 'phone': '555-5555'}) =", student2)

student3 = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
del student3['age']
student4 = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
age = student4.pop('age')

print("del student['age'] =", student3,"\nage = student.pop('age') =", age,"and student =", student4)
print("len(student) =", len(student),"\nstudent.keys() =", student.keys(),"\nstudent.values() =", student.values())
print("student.items() =", student.items(),"\nfor key in student:\n\tprint(key)\nResposta:")

for key in student:
	print(key)

print("\nfor key, value in student.items():\n\tprint(key, value)\nResposta:")

for key, value in student.items():
	print(key + ":", value)
