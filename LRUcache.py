#coding:utf-8

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=128):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val

    def put(self,key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            if len(self.od) >= self.capacity:
                self.od.popitem(last=False)
            self.od[key] = value

def test_lru():
    lru_obj = LRUCache(3)
    lru_obj.put(100,200)
    print(lru_obj.get(100))
    assert lru_obj.get(100) == 200
    lru_obj.put(100,201)
    assert lru_obj.get(100) == 201
    lru_obj.put(101, 202)
    assert list(lru_obj.od.keys())[-1] == 101
    print(list(lru_obj.od.keys()))
    lru_obj.put(102, 203)
    assert list(lru_obj.od.keys())[-1] == 102
    lru_obj.get(100)
    assert list(lru_obj.od.keys())[-1] == 100
    assert len(lru_obj.od) == 3
    assert list(lru_obj.od.keys()) == [101, 102, 100]
    lru_obj.put(103,204)
    assert len(lru_obj.od) == 3
    assert list(lru_obj.od.keys()) == [102, 100, 103]
    assert lru_obj.get(101) == None
    assert lru_obj.get(102) == 203
    assert lru_obj.get(100) == 201
    assert lru_obj.get(103) == 204
    lru_obj.put(101,99)
    assert list(lru_obj.od.keys()) == [100, 103, 101]


test_lru()
