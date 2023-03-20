# def outer_func(msg):
# 	def inner_func():
# 		print(msg)
# 	return inner_func


# my_func = outer_func('Hello')
# my_func()


# # def square(x):
# # 	return x * x


# # result = square
# # print(result(6))


def dec_func(org_func):
	def wrapper_func():
		print('hello')
		return org_func()
	return wrapper_func

@dec_func
def disp():
	print('This is disp function')

# dec_disp = dec_func(disp)
# dec_disp()

disp()