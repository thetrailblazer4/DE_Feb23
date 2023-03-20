class Employee:
	
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.salary = salary

	def fullname(self):
		return f"{self.first} {self.last}"

	def __repr__(self):
		return f"Employee('{self.first}', '{self.last}', {self.salary})"

	def __str__(self):
		return f"{self.fullname()} - {self.salary}"


emp_1 = Employee('John', 'K', 50000)


print(emp_1.__repr__())
print(emp_1.__str__())