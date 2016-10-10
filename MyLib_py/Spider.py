# !/usr/bin/python
# encoding:utf-8
"""
    常用爬虫类

author     :   @`13
version    :   0.0.9
last-update:   2016.10.10

# history：
version 0.0.9
    *   + 读取页面内容方法
    *   + 模拟登陆方法 [重写
    *   + 信息处理方法 [重写
    *   + 读取页面内容方法 [重写

"""

import urllib
import urllib2
from random import choice


class Spider:
    """爬虫类
    子类集成这个父类，有必要时重写getPageText 方法
    然后重写/新建子类需要的方法
    """

    def __init__(self, url=None):
        """
        :param url: 基础链接
        """
        self.baseURL = url

    @staticmethod
    def getPageText(url, timeOut=5, Header=None, useHaeder=False, reSetHaeder=False, ):
        """
        获取页面内容
        :param url: URL
        :param timeOut:超时设置
        :param Header:头部设置
        :param useHaeder: 使用默认头部标志
        :param reSetHaeder: 重设头部标志
        :return: url的内容
        """

        # 头部信息 浏览器标示集合
        USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

        # 火狐（Firefox）标准Linux头部信息
        send_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Connection': 'keep-alive'
        }

        # 重设头部
        if reSetHaeder:
            send_headers['User-Agent'] = choice(USER_AGENTS)
            # print send_headers['User-Agent']

        # 特定头部
        if Header:
            url_header = Header
        else:
            url_header = send_headers

        # 使用头部
        if useHaeder:
            req = urllib2.Request(url, headers=url_header)
            try:
                response = urllib2.urlopen(req, timeout=timeOut)
            except Exception as errorMassage:
                print errorMassage
                print "[urllib2_Error]解析" + str(url) + "内容失败！"
                return None
            return response.read()
        # 不使用头部（简单urllib打开
        else:
            try:
                text = urllib.urlopen(url).read()
            except Exception as errorMassage:
                print errorMassage
                print "[urllib_Error]解析" + str(url) + "内容失败！"
                return None
            return text

    @staticmethod
    def infoDeal(HTMLtext, type=0, iterationNum=2500):
        """
        :param HTMLtext:HTML页面内容/其他含有需要提取的内容
        :param type:返回信息类型 0-迭代器，1-其他对象， other-其他
        :param iterationNum:迭代器每次迭代的数两
        :return:可迭代的信息对象/其他格式
        """
        # 根据情况重写
        pass

    @staticmethod
    def login(login_url, username, password, ):
        """
        模拟登陆
        :param login_url:登陆页面url
        :param username:用户名
        :param password:密码
        :return:是否成功登陆的布尔值
        """
        # 根据情况重写
        pass

