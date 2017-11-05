import functools


def run_time(func):
	#修改生成器函数的名称
	#相当于wrapper.__name__ = func.__name__ 
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print("%s %s():" %(func.__name__,"start begin"))
		return func(*args,**kw)
	return wrapper

@run_time
def f_tmp():
	print("run f_tmp")

f_tmp()
print(f_tmp.__name__)