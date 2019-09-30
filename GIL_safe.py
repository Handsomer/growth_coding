#coding:utf-8
import dis
import threading

lock = threading.Lock()

def incr_list(l):
    l[0] += 1

n = 0
def incr_int(n):
    n += 1
dis.dis(incr_list)
print('hello --- --- ---')
dis.dis(incr_int)