"""
脚本用途：该脚本是的方法来源于　Python的第三方库requets，
        由于该库对于Python的高质量使用，
        在本脚本里提炼其精妙之处，配合以单独demo规范编码习惯．
auther: sun_pro
time: 2018_01_26
"""

import os
import requests


def file_path():
    '''
    __file__：当前文件夹路径
    os.path.dirname(__file__)  获得所在上一级文件夹路径
    os.path.join()路径拼接
    os.path.abspath　返回路径的绝对路径
    '''
    here = os.path.abspath(os.path.dirname(__file__))
    print (here)
    print (os.path.join(here,"request","__version__.py"))


def exec():
    """
    exec:是Python的built-in函数，其作用很好描述，就是执行以string类型存储的Python代码。
    该实例中ans变量并没有显示的定义，但由于exec的使用在字符串中的ans = i+j，便相当于对ans的定义．
    ＊＊注意：在循环中使用exec时慎用　break．因为break是会寻找最近的for 或者 while跳出循环．
    """
    i = 2
    j = 3
    exec("ans=i+j")
    print("ans=i+j:",ans)

def post_request():
    """
    post:　是requests的比较重要的方法，该函数用于发送form表单，headers 等信息.
           data:存储了requests post表单的信息
    headers:存储了headers包含的所有信息(cookies,Accept,Accept-Encoding等).
    :return:
    """
    data = {"projectName": "项目名称关键字",
            "rblFWType": "q",
            "txtYS": "",
            "txtZH": "",
            "txtCQZH": "证号关键字",
            "developer": "单位名称关键字",
            "txtaddress": "地址关键字",
            "dopIsHouse": -1,
            "currentPage": 4,
            "pageSize": 15}

    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9",
               "Cache-Control": "max-age=0",
               "Content-Length": "326",
               "Content-Type": "application/x-www-form-urlencoded",
               "Cookie": "JSESSIONID=F3E81A115CD69157AE253810684941AD; Hm_lvt_9ac0f18d7ef56c69aaf41ca783fcb10c=1516871235,1516930646; Hm_lpvt_9ac0f18d7ef56c69aaf41ca783fcb10c=1516932895",
               "Host": "www.bjjs.gov.cn",
               "Origin": "http://www.bjjs.gov.cn",
               "Proxy-Connection": "keep-alive",
               "Referer": "http://www.bjjs.gov.cn/eportal/ui?pageId=307670",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}

    r = requests.post("http://www.bjjs.gov.cn/eportal/ui?pageId=307670", data=data, headers=headers)
    print(r.status_code)
    b = r.content
    print(r.content)

post_request()