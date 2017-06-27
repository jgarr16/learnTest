# calculate.py
# this program adds two numbers to get a sum
# used to learn how to unit test in Python

class Calculate(object):
	def add(self, x, y):
		return x + y

if __name__ == '__main__':
	calc = Calculate()
	result = calc.add(2, 2)
	print(result)