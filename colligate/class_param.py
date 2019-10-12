#coding:utf-8

#类变量
class Test(object):
    #定义类变量
    num_of_instance = 0
    #定义成员变量, 不可变对象
    instance_param_stubborn = 'aaa'
    #定义成员变量, 可变对象
    instance_param_unstubborn = [1]

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1
    

if __name__ == "__main__":
    print(Test.num_of_instance)
    t1 = Test('Jack')
    t1.instance_param_stubborn = 'bbb'
    print(t1.name, t1.num_of_instance, Test.num_of_instance,t1.instance_param_stubborn, Test.instance_param_stubborn)
    t1.instance_param_unstubborn.append(2)
    print(t1.instance_param_unstubborn, Test.instance_param_unstubborn)
    t2 = Test('lucy')
    print(t2.name, t2.num_of_instance,Test.num_of_instance, t2.instance_param_stubborn, Test.instance_param_stubborn)
    print(t2.instance_param_unstubborn, Test.instance_param_unstubborn)
