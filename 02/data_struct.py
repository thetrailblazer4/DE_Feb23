# # Mutable

# # list_1 = ['Hello', 'Hi', 'Hey']
# # list_2 = list_1

# # print(list_1)
# # print(list_2)

# # list_1[0] = 'Bye'

# # print(list_1)
# # print(list_2)

# # Immutable

# # tuple_1 = ('Hello', 'Hi', 'Hey')
# # tuple_2 = tuple_1

# # print(tuple_1)
# # print(tuple_2)

# # tuple_1[0] = 'Bye'

# # print(tuple_1)
# # print(tuple_2)


# # Sets
# # message = {'Hello', 'Hi', 'Hey', 'Hi', 'Hey'}
# # new_msg = {'Bye', 'Hi','Goodbye'}

# # print('Hey' in message)

# # print(message.intersection(new_msg))
# # print(message.difference(new_msg))
# # print(message.union(new_msg))

# # # Empty Lists
# # empty_list = []
# # empty_list = list()

# # # Empty tuple
# # empty_list = ()
# # empty_list = tuple()

# # # Empty sets
# # empty_set = {} #<--- Avoid using this method, it is also used for creating dict
# # empty_set = set()


# # Dictionaries: {key1:value1, key2:value2 }

# # emp_1 = ['John','26', 'python','java']
# # emp_2 = ['python', 'Tom', '24']

# # print(emp_1[0])
# # print(emp_2[0])

# emp = {'name':'John', 'age':29, 'prog_lang':['Python', 'Java']}

# # print(emp)
# # print(emp['email'])
# # print(emp.get('email', 'Not Found'))

# # print(emp.keys())
# # print(emp.values())
# # print(emp.items())

# # for k, v in emp.items():
# # 	print(f"This is Key '{k}' - the value '{v}'")

# # emp['email'] = 'John@company.com'
# # emp['name'] = 'Tom'

# # emp.update({'name':'Tom', 'email':'John@company.com'})
# # del emp['age']
# age = emp.pop('age')
# print(age)
# print(emp)