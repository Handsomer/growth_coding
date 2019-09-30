#coding:utf-8

import collections

PointModule = collections.namedtuple('Point','x,y')

p = PointModule(1,2)
print(p.x, p.y, p[0], p[1])