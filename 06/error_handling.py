'''syntax
name error
indentation 

FileNotFoundError

'''


# try:
# 	pass
# except:
# 	pass

try:
	f = open('my_file.txt')

except FileNotFoundError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(f.name)
	print(f.read())

finally:
	print('Executing.....')
