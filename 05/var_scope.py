# # # LEGB --> Local --> Enclosing --> Global -->Builtin

# # x = 'global x'

# # def outer(z):
# # 	# global x
# # 	x = 'local x'
# # 	print(z)


# # outer('local z')
# # print(x)


# # import builtins

# # # print(dir(builtins))

# # print(help(max))




# nums = [12,43,1,2,89]

# # def max():
# # 	pass

# print(max(nums))


x = 'global x'
def outer():
	# x = 'outer x'
	def inner():
		# x = 'inner x'
		print(x)
	inner()
	print(x)


outer()