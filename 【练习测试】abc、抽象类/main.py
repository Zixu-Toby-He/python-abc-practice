import os
import traceback
from aaa import *

class B(A):
	def __init__(self):
		super().__init__()
	def abf(self, arg):
		print(repr(arg), self.a+1)

def main():
	#a=A()
	#a.f()
	b=B()
	b.f()

if __name__=="__main__":
	try:
		main()
	except:
		traceback.print_exc()
	finally:
		print()
		print()
		print()
		os.system("pause")