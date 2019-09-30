#coding:utf-8
import threading

n = [0]

def foo():
    n[0] += 1
    n[0] += 1

threads_list = []
for i in range(5000):
    t = threading.Thread(target=foo)
    threads_list.append(t)

for t in threads_list:
    t.start()

print(n[0])