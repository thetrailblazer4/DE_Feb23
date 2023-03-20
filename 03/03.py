'''

message = ['hello', 'Hi', 'bye']

search_index(messsage, "hi")


'''

message = ['hello', 'Hi', 'bye']

def search_index(args, target):
	for i, v in enumerate(args):
		if v == target:
			return f"The index of '{v}' is {i}"
	return -1

print(search_index(message, 'Bye'))

print(search_index(message, 'Hi'))