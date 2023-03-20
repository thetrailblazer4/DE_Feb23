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


class Developer(Employee):
	raise_amt = 1.09

	def __init__(self, first, last, salary, prog_lang):
		super().__init__(first, last, salary)
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self, first, last, salary, emps=None):
		super().__init__(first, last, salary)

		if emps is None:
			self.emps = []
		else:
			self.emps = emps


	def add_emp(self, emp):
		if emp not in self.emps:
			self.emps.append(emp)

	def remove_emp(self, emp):
		if emp in self.emps:
			self.emps.remove(emp)

	def disp_emps(self):
		for i in self.emps:
			print(i.fullname())


emp_1 = Employee('John', 'K', 50000)
emp_2 = Developer('Tom', 'M', 60000, 'python')
mgr = Manager('Ravi', 'A', 900000, [emp_1])


# mgr.add_emp(emp_2)

# print(mgr.fullname())

# mgr.disp_emps()

print(isinstance(emp_2, Employee))