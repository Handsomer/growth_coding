#coding:utf-8
# import ptvsd

import os
import ptvsd
ptvsd.enable_attach(address = ('0.0.0.0', 5679))
ptvsd.wait_for_attach()

#添加注释
for i  in range(10):
    print(i,"---" * 10)

print(os.system('which python'))