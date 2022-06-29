#!/usr/bin/python3
#Vídeo 07 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

nums = [1, 2, 3, 4, 5]

print("nums = ", nums,"\n\nfor num in nums:\n\tprint(num)\nResposta:")

for num in nums:
	print(num)

print("\nfor num in nums:\n\tif num == 3:\n\t\tprint('Found!')\n\t\tbreak\n\tprint(num)\nResposta:")

for num in nums:
	if num ==3:
		print('Found!')
		break
	print(num)

print("\nfor num in nums:\n\tif num == 3:\n\t\tprint('Found!')\n\t\tcontinue\n\tprint(num)\nResposta:")

for num in nums:
	if num ==3:
		print('Found!')
		continue
	print(num)

print("\nfor num in nums:\n\tfor letter in 'abc':\n\t\tprint(num, letter)\nResposta:")

for num in nums:
	for letter in 'abc':
		print(num, letter)

print("\nfor i in range(10):\n\tprint(i)\nResposta:")

for i in range(10):
	print(i)

print("\nfor i in range(1, 11):\n\tprint(i)\nResposta:")

for i in range(1, 11):
	print(i)

x = 0

print("\nx = 0\n\nwhile x < 10:\n\tprint(x)\n\tx += 1\nResposta:")

while x < 10:
	print(x)
	x += 1

x = 0

print("\nx = 0\n\nwhile x < 10:\n\tif x == 5:\n\t\tbreak\n\tprint(x)\n\tx += 1\nResposta:")

while x < 10:
	if x == 5:
		break
	print(x)
	x += 1

x = 0

print("\nx = 0\n\nwhile True:\n\tif x == 5:\n\t\tbreak\n\tprint(x)\n\tx += 1\nResposta:")

while True:
	if x == 5:
		break
	print(x)
	x += 1

x = 0

print("\nx = 0\n\nwhile True:\n\tprint(x)\n\tx += 1\nResposta:")

while True:
	print(x)
	x += 1
