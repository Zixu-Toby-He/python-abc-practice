import abc

class A(abc.ABC):
	def __init__(self, a=0):
		self.a=a
	@abc.abstractmethod
	def abf(self,arg):
		print(arg, self.a)
	def f(self):
		self.abf("test")