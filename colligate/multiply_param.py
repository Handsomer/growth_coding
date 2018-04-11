#coding:'utf-8'

'''
此脚本用于练习python传多个参数时的使用.
'''
def one(*args):
        for count, thing in enumerate(args):
            print (count,thing)


def two(**kwargs):
    for name,value in kwargs.items():
        print (name,value)

def three(*args,**kwargs):
    for count, thing in enumerate(args):
        print (count, thing)
    for name,value in kwargs.items():
        print (name,value)

one('apple','banana','cabbage')
two(apple = 'fruit',cabbage = 'vagetable')
three('apple','banana','cabbage',apple = 'fruit',cabbage = 'vagetable')




