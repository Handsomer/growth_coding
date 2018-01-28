#coding=utf-8
# import functools



def out(func):
    def add(*args,**kwargs):
        print "原有功能"
        r = func(*args,**kwargs)
        print "后增功能"
        return r
    return add

# 装饰器是一个函数
#不需要修改调用方式
#
def out1(func):
    def add(*args,**kwargs):
        print "start"
        r = func(*args,**kwargs)
        print "end"
        return r
    return add

'''
此处@out 相当于
# n = out(f)
# f = n

'''
@out1
@out
def f(a,b):
    print "xianyougongne",a,b


# n = out(f)
# f = n
f(1,2)
'''
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
print(f_tmp.__name__)'''