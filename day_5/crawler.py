#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
爬虫技巧
"""
import urllib2
import urllib
import cookielib
from threading import Thread, Lock
from Queue import Queue
import time

# 基本抓站
content = urllib2.urlopen('http://www.baidu.com').read()

# 代理服务器
# IP被封，或者IP访问的次数受到限制等
proxy_support = urllib2.ProxyHandler({'http': 'http://XX.XX.XX.XX:XXXX'})
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen('http://www.baidu.com').read()

# 登录
# cookie
cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen('http://XXXX').read()

# 同时用代理和cookie
opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)

# 表单的处理
postdata = urllib.urlencode({
    'username': 'XXXXX',
    'password': 'XXXXX',
    'continueURI': 'http://www.verycd.com/',
    'fk': '1',
    'login_submit': '登录'
})
req = urllib2.Request(
    url='http://secure.verycd.com/signin/*/http://www.verycd.com/',
    data=postdata
)
result = urllib2.urlopen(req).read()

# 伪装成浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
req = urllib2.Request(
    url='http://secure.verycd.com/signin/*/http://www.verycd.com/',
    data=postdata,
    headers=headers
)

# 反”反盗链”
headers = {
    'Referer': 'http://www.cnbeta.com/articles'
}


# 多线程并发抓取
class Fetcher:
    def __init__(self, threads):
        self.opener = urllib2.build_opener(urllib2.HTTPHandler)
        self.lock = Lock()  # 线程锁
        self.q_req = Queue()  # 任务队列
        self.q_ans = Queue()  # 完成队列
        self.threads = threads
        for i in range(threads):
            t = Thread(target=self.threadget)
            t.setDaemon(True)
            t.start()
        self.running = 0

    def __del__(self):  # 解构时需等待两个队列完成
        time.sleep(0.5)
        self.q_req.join()
        self.q_ans.join()

    def taskleft(self):
        return self.q_req.qsize() + self.q_ans.qsize() + self.running

    def push(self, req):
        self.q_req.put(req)

    def pop(self):
        return self.q_ans.get()

    def threadget(self):
        while True:
            req = self.q_req.get()
            with self.lock:  # 要保证该操作的原子性，进入critical area
                self.running += 1
                try:
                    ans = self.opener.open(req).read()
                except Exception, what:
                    ans = ''
                    print(what)
            self.q_ans.put((req, ans))
            with self.lock:
                self.running -= 1
            self.q_req.task_done()
            time.sleep(0.1)  # don't spam


if __name__ == "__main__":
    links = ['http://www.verycd.com/topics/%d/' % i for i in range(5420, 5430)]
    f = Fetcher(threads=10)
    for url in links:
        f.push(url)
        while f.taskleft():
            url, content = f.pop()
            print(url + str(len(content)))
