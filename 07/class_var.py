class Employee:

	raise_amt = 1.08
	
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.salary = int(salary)

	def fullname(self):
		return f"{self.first} {self.last}"

	def inc(self):
		self.salary = int(self.salary * self.raise_amt)



emp_1 = Employee('John', 'K', '50000')

print(emp_1.salary)
print(emp_1.raise_amt)

emp_1.inc()

print(emp_1.salary)

