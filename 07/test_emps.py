import unittest
from emps import Employee


class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')


	def setUp(self):
		self.emp_1 = Employee('John', 'K', 50000)
		self.emp_2 = Employee('Tom', 'M', 60000)

	def tearDown(self):
		print('tearDown\n')


	def test_email(self):

		self.assertEqual(self.emp_1.email, 'John.K@company.com')
		self.assertEqual(self.emp_2.email, 'Tom.M@company.com')

		self.emp_1.first = 'Ravi'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.email, 'Ravi.K@company.com')
		self.assertEqual(self.emp_2.email, 'Jane.M@company.com')


	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'John K')
		self.assertEqual(self.emp_2.fullname, 'Tom M')

		self.emp_1.first = 'Ravi'
		self.emp_2.first = 'Jane'

		self.assertEqual(self.emp_1.fullname, 'Ravi K')
		self.assertEqual(self.emp_2.fullname, 'Jane M')


	def test_inc(self):

		self.emp_1.inc()
		self.emp_2.inc()

		self.assertEqual(self.emp_1.salary, 54000 )
		self.assertEqual(self.emp_2.salary, 64800)





if __name__ == '__main__':
	unittest.main()