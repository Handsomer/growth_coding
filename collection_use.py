#coding:utf-8

import collections

PointModule = collections.namedtuple('Point','x,y')

p = PointModule(1,2)
print(p.x, p.y, p[0], p[1])

print('------ -------')
counter_obj = collections.Counter('aaaabfbbbbb')
print(counter_obj['a'])
print(counter_obj.most_common(3))

print('------ -------')
counter_obj = collections.Counter([12,1,1,1,4,4,6,6,6])
print(counter_obj.most_common(3))
