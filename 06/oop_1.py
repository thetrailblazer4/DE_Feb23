# classes and Instances

class Employee:
	
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.salary = salary

	def fullname(self):
		return f"{self.first} {self.last}"



emp_1 = Employee('John', 'K', 50000)
emp_2 = Employee('Tom', 'H', 60000)




# print(emp_1.first)
# print(emp_1.last)


print(emp_1.fullname())
print(emp_2.fullname())
# print(f"{emp_1.first} {emp_1.last}")
# print(f"{emp_2.first} {emp_2.last}")





