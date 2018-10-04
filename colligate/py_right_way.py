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


#一切都是对象, 使用对象的方式来代替需要多次调用的情景
#比如加减乘除的四则运算
# bad
def print_addition_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x + y) + '\n')

def print_subtraction_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x - y) + '\n')

def print_multiplication_table():
        for x in range(1, 3):
            for y in range(1, 3):
                print(str(x * y) + '\n')

def print_division_table():
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(x / y) + '\n')

print_addition_table()
print_subtraction_table()
print_multiplication_table()
print_division_table()

# good, python一切都是对象，可以函数作为参数，类似技巧可以用来简化代码
import operator as op

def print_table(operator):
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(operator(x, y)) + '\n')

for operator in (op.add, op.sub, op.mul, op.div):
    print_table(operator)

# bad
def apply_operation(left_operand, right_operand, operator):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand
# good
def apply_operation(left_operand, right_operand, operator):
    import operator as op
    operator_mapper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return operator_mapper[operator](left_operand, right_operand)


#使用字典来代替switch case的使用场景
# bad
def apply_operation(left_operand, right_operand, operator):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand
# good
def apply_operation(left_operand, right_operand, operator):
    import operator as op
    operator_mapper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return operator_mapper[operator](left_operand, right_operand)
