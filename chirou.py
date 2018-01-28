
# -*- coding: utf-8 -*-
import os
import sys
import requests
import time
from lxml import html

headers = {
    'Host': 'yaohuo.me',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'GUID=填你自己的;__guid=填你自己的;sidyaohuo=填你自己的',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

yaohw='http://yaohuo.me'
counts =12735 #页数
ubbtxt='\n' #肉贴地址


def crawl(url):
    global ubbtxt
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    #print(str(page).encode('GB2312'))
    intro_raw = root.xpath('//div/img[@*]/following::a[1]/@href')
    for i in intro_raw:
        if len(str(i)) <= 30:
            time.sleep(0.2)
            neiye (i[0:i.find('html')+4])
    f=open('yaohw.txt','a')
    f.write(ubbtxt)
    f.close()
    ubbtxt='' #清空文本
    print('第'+str(counts)+'页爬完了哦------------------------------------------------------')
	
def neiye(url):
    global ubbtxt
    resp = requests.get(yaohw+url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    #print (page)
    intro_raw = root.xpath('//div[@class=\'content\']/child::text()')
    for i in intro_raw:
        x=str(i).replace(u'\xa0', u' ').encode('gb18030')
        print x
        if ('礼金' in x ) and ('余0' not in x):
            ubbtxt+='\n'+'还有[url='+yaohw+url+']'+x[x.find('余')+2:len(x)-1]+'肉[/url]'


if __name__ == '__main__':
    f=open('yaohw.txt','w')
    f.write('开始找肉吃了哦\n')
    f.close()
    url = 'http://yaohuo.me/bbs/book_list.aspx?action=class&siteid=1000&classid=177&page='  
    reload(sys)
    sys.setdefaultencoding('utf-8')
    while counts != 0:
        crawl(url+str(counts))
        counts=counts-1
        

