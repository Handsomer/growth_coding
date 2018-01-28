#coding=utf-8

def mysum(L):
    first,*rest = L
    return first if not rest else first + mysum(rest)

# a = [1,2,3]
a =['1','2']
print(mysum(a))
