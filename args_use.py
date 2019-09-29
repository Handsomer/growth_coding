#coding:utf-8

def func_arg(param_1, *args, **kwargs):
    print(param_1,  '---', args, '---', kwargs)

func_arg('hello','memem', 'haha',a=1, b=2)