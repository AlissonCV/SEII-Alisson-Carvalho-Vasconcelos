#!/usr/bin/python3
#Vídeo 11 da playlist https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7

f = open('test.txt', 'r')

print(f.name)
print("\n" + f.mode)

f.close()

with open('test.txt', 'r') as f:
	pass

print("\n" + str(f.closed))
print("\nprint(f.read())\nResposta:\nTraceback (most recent call last):")
print("""  File "/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/./py11.py", line 15, in <module>\n    print("\\n" + f.read())""")
print("ValueError: I/O operation on closed file.")

with open('test.txt', 'r') as f:
	f_contents = f.read()
	print("\n" + f_contents + "\n")

with open('test.txt', 'r') as f:
	f_contents = f.readlines()
	print(f_contents)

with open('test.txt', 'r') as f:
	f_contents_1 = f.readline()
	print("\n" + f_contents_1)
	f_contents_2 = f.readline()
	print(f_contents_2)
	f_contents_3 = f.readline()
	print(f_contents_3, end='')
	f_contents_4 = f.readline()
	print(f_contents_4)

with open('test.txt', 'r') as f:
	for line in f:
		print(line, end='')

with open('test.txt', 'r') as f:
	f_contents = f.read(100)
	print("\n" + f_contents + "\n")

with open('test.txt', 'r') as f:
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(str(f.tell()) + "\n")
	while len(f_contents) > 0:
		print(f_contents, end='*')
		f_contents = f.read(size_to_read)

with open('test.txt', 'r') as f:
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print("\n\n" + f_contents, end='')

	f.seek(0)

	f_contents = f.read(size_to_read)
	print(f_contents)
	f_contents = f.read(size_to_read)

print("\nwith open('test.txt', 'r') as f:\n\tf.write('Test')\nTraceback (most recent call last):")
print("""  File "/home/alisson/Documentos/Sistemas Embarcados II/SEII-Alisson-Carvalho-Vasconcelos/Semana 04/./py11.py", line 64, in <module>\n    f.write('Test')""")
print("io.UnsupportedOperation: not writable")

with open('test2.txt', 'w') as f:
	f.write('Test')

with open('test2.txt', 'r') as f:
	f_contents = f.read()
	print('\n' + f_contents)

with open('test.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

with open('test_copy.txt', 'r') as f:
	f_contents = f.read()
	print('\n' + f_contents)

with open('bronx.jpg', 'rb') as rf:
	with open('bronx_copy.jpg', 'wb') as wf:
		for line in rf:
			wf.write(line)

with open('bronx.jpg', 'rb') as rf:
	with open('bronx_copy.jpg', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)
