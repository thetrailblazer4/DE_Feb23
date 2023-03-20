# # f = open('demo_file.txt', 'r')

# # print(f.read())

# # f.close()


# with open('demo_file.txt', 'r') as f:

# 	for i in f:
# 		print(i, end='')

# 	# print(f.read())

# # print(f.closed)


with open('my_file.txt', 'w') as f:
	f.write('New Line')
	f.seek(0)
	f.write('Second')