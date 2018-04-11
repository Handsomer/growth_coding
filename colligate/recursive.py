#coding=utf-8

def mysum(L):
    first,*rest = L
    return first if not rest else first + mysum(rest)

def iterator_way():
    print(sum(i for i in range(10)))# 这种写法等效于下面

if __name__ == "__main__":
    # a = [1,2,3]
    a =['1','2']
    print(mysum(a))
