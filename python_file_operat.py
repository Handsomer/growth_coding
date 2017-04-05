#!/usr/bin/env python
# coding=utf-8
import sys

m_fileType = sys.getfilesystemencoding()

xiaoqu_content = ''
#该文件包含有  ‘市，自治州，等名称’
try:
	with open('C:\\tmp\\xiaoqu_info.log','r') as fd_xiaoqu:
		xiaoqu_content = fd_xiaoqu.read().decode('utf-8').encode(m_fileType)
except:
	print 'error'

try:
	with open('url_city.log','r') as fd_url:
		while 1:
			url_contend = fd_url.readline().decode('utf-8').encode(m_fileType).split('\n')[0]
			if len(url_contend):
				if xiaoqu_content.find(url_contend) == -1:
					print url_contend
			else:
				break
except:
	print 'open url file error'

