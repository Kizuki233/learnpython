
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
    'Cookie': 'GUID=�����Լ���;__guid=�����Լ���;sidyaohuo=�����Լ���',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

yaohw='http://yaohuo.me'
counts =12735 #ҳ��
ubbtxt='\n' #������ַ


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
    ubbtxt='' #����ı�
    print('��'+str(counts)+'ҳ������Ŷ------------------------------------------------------')
	
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
        if ('���' in x ) and ('��0' not in x):
            ubbtxt+='\n'+'����[url='+yaohw+url+']'+x[x.find('��')+2:len(x)-1]+'��[/url]'


if __name__ == '__main__':
    f=open('yaohw.txt','w')
    f.write('��ʼ�������Ŷ\n')
    f.close()
    url = 'http://yaohuo.me/bbs/book_list.aspx?action=class&siteid=1000&classid=177&page='  
    reload(sys)
    sys.setdefaultencoding('utf-8')
    while counts != 0:
        crawl(url+str(counts))
        counts=counts-1
        

