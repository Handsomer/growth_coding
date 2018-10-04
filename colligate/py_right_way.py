'''
避免使用可变(mutable)变量作为函数参数的默认初始化值
'''
#bad EX
def function_bad(l = []):
    l.append(1)
    return l

print(function_bad())
print(function_bad())
print(function_bad())

def function_right(l=None):
    if l is None:
        l = []
    l.append(1)
    return l


print(function_right())
print(function_right())
print(function_right())
