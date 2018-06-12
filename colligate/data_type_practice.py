# coding=utf-8


#-----------list的基本操作----------------------------------
ori_list = [1,2,2,3,2]

#list_基本操作)
print("ori_list:",ori_list)
ori_list.append(4)
#追加元素)
print("ori_list.append(4):",ori_list)
#元素个数)

print("ori_list.count(2):",ori_list.count(2))
#追加一个列表
ori_list.extend([6,6,6])
print("ori_list.extend([6,6,6]):",ori_list)

#某个值的序号,匹配到第一个的索引,不在则返回 Value Error
print("ori_list.index(2):",ori_list.index(2))
#确定位置插入

#某个值的序号,匹配到第一个的索引,不在则返回 Value Error)
print("ori_list.index(2):",ori_list.index(2))
#确定位置插入)

print("ori_list.insert(2,88):",ori_list)
#pop 删除最后一个元素
ori_list.pop()
print("ori_list.pop():",ori_list)
#remove 删除匹配的第一个元素
ori_list.remove(2)
print("ori_list.remove(2):",ori_list)
#reverse 翻转,原始列表发生翻转
ori_list.reverse()
print("ori_list.reverse():",ori_list)
#sort 排序,对原始列表排序
ori_list.sort()
print("ori_list.sort():",ori_list)

#-----------set的基本操作----------------------------------

ori_list = [1,2,2,3]
#set_基本操作
a = set(ori_list)
b = set([6,7,8])

print(type(a))

print("a:",a)
print("b:",b)
#并集
print("a|b:",a|b)
#交集
print("a&b:",a&b)
#差集
print("a-b:",a-b)
#对称差集
print("a^b:",a^b)
# 添加数据
a.update([11,22])
print("a.update([11,22]):",a)# ====    a |= b
# 删
a.remove(11)
print("a.remove(11):",a)
# 长度
print("len(a):",len(a))
# 判断
print('123 in a:',123 in a)
print('22 in a:',22 in a)
#是否全包含
print("a <= b:",a <= b)
print("a.issubset(b):",a.issubset(b))
print("set([7,8]).issubset(b)",set([7,8]).issubset(b))
'''
#pop 随机删除，clear　清空set，discard　存在则删除，remove存在则删除，不存在则报异常．
=======
print(type(a))
print(a)
print("a:",a)
print("b:",b)
#并集)
print("a|b:",a|b)
#交集)
print("a&b:",a&b)
#差集)
print("a-b:",a-b)
#对称差集)
print("a^b:",a^b)
# 添加数据
a.update([11,22])
print("a.update([11,22]):",a) # ====　　a |= b
# 删
a.remove(11)
print("a.remove(11):",a)
# 长度)
print("len(a):",len(a))
# 判断)
print('123 in a:',123 in a)
print('22 in a:',22 in a)
#是否全包含)
print("a <= b:",a <= b)
print("a.issubset(b):",a.issubset(b))
print("set([7,8]).issubset(b)",set([7,8]).issubset(b))
#pop 随机删除，clear　清空set，discard　存在则删除，remove存在则删除，不存在则报异常．)
'''