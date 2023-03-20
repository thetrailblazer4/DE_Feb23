
# Regular methods, Class Methods, staticmethod

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


	@classmethod
	def update_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True



emp_1 = Employee('John', 'K', '50000')

new_emp_str = 'Tom-M-70000'

new_emp = Employee.from_str(new_emp_str)

# first, last, pay = emp_str.split('-')
# emp_2 = Employee(first, last, pay)

# print(new_emp.fullname())

import datetime

my_date = datetime.date(2023, 3, 11)

print(Employee.is_workday(my_date))



# Employee.update_raise_amt(1.09)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)



