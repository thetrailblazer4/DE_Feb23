# property decorators

class Employee:
	
	raise_amt = 1.08
	
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary

	@property
	def email(self):
		return f'{self.first}.{self.last}@company.com'

	@property
	def fullname(self):
		return f"{self.first} {self.last}"


	def inc(self):
		self.salary = int(self.salary * self.raise_amt)


emp_1 = Employee('John', 'K', 50000)

emp_1.first = 'Tom'


print(emp_1.first)
print(emp_1.fullname())
print(emp_1.email)