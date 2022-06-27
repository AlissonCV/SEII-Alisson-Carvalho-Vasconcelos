#!/usr/bin/python3
#Vídeo 04 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

courses = ['History', 'Math', 'Physics', 'CompSci']
courses1 = ['History', 'Math', 'Physics', 'CompSci']
courses1.append('Art')
courses2 = ['History', 'Math', 'Physics', 'CompSci']
courses2.insert(0, 'Art')
courses_2 = ['Art', 'Education']
courses3 = ['History', 'Math', 'Physics', 'CompSci']
courses3.insert(0, courses_2)
courses4 = ['History', 'Math', 'Physics', 'CompSci']
courses4.extend(courses_2)
courses5 = ['History', 'Math', 'Physics', 'CompSci']
courses5.remove('Math')
courses6 = ['History', 'Math', 'Physics', 'CompSci']
popped = courses6.pop()

print("courses =", courses,"\nlen(courses) =", len(courses),"\ncourses[0] =", courses[0],"\ncourses[3] =", courses[3])
print("courses[-1] =", courses[-1],"\ncourses[0:2] =", courses[0:2],"\ncourses[:2] =", courses[:2],"\ncourses[2:] =", courses[2:])
print("courses.append('Art') =", courses1,"\ncourses.insert(0, 'Art') =", courses2,"\ncourses_2 =", courses_2,"\ncourses.insert(0, courses_2) =", courses3)
print("courses.extend(courses_2) =", courses4,"\ncourses.remove('Math') =", courses5,"\npopped = courses.pop() =", popped,"and courses =", courses6)

courses7 = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]
courses7.reverse()

print("courses.reverse() =", courses7)

courses7.sort()
nums.sort()

print("courses.sort() =", courses7,"\nnums = [1, 5, 2, 4, 3]\nnums.sort() =", nums)

courses8 = ['History', 'Math', 'Physics', 'CompSci']
nums1 = [1, 5, 2, 4, 3]

courses8.sort(reverse=True)
nums1.sort(reverse=True)

print("couses.sort(reverse=True) =", courses7,"\nnums.sort(reverse=True) =", nums)

sorted_courses = sorted(courses)

print("sorted_courses = sorted(courses) =", sorted_courses)

nums2 = [1, 5, 2, 4, 3]

print("mim(nums) =", min(nums2),"\nmax(nums) =", max(nums2),"\nsum(nums) =", sum(nums2))

courses9 = ['History', 'Math', 'Physics', 'CompSci']

print("courses.index('CompSci') =", courses9.index('CompSci'))

print("'Art' in courses =", 'Art' in courses,"\n'Math' in courses =", 'Math' in courses,"\nfor item in courses:\n\tprint(item)\nResposta:")

for item in courses:
	print(item)

print("\nfor index, course in enumerate(courses):\n\tprint(index, course)\nResposta:")
for index, course in enumerate(courses):
	print(index, course)

print("\nfor index, course in enumerate(courses, start=1):\n\tprint(index, course)\nResposta:")
for index, course in enumerate(courses, start=1):
	print(index, course)

course_str = ', '.join(courses)
course_str1 = ' - '.join(courses)
new_list = course_str1.split(' - ')

print("course_str = ', '.join(courses) =", course_str,"\ncourse_str = ' - '.join(courses) =", course_str1,"\nnew_list = course_str.split(' - ') =", new_list)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
cs_courses1 = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Designe'}

print("cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'} =", cs_courses,"\nart_courses =", art_courses,"\ncs_courses.intersection(art_courses) =", cs_courses.intersection(art_courses))
print("cs_courses.difference(art_courses) =", cs_courses.difference(art_courses),"\ncs_courses.union(art_courses) =", cs_courses.union(art_courses),"\n")

print("-Criando listas vazias:\nempty_list = [] ou list()\nempty_tuple = () ou tuple()\nempty_set = set()")
