#输入输出
# a=input('请输入str')  input()返回的是str  int(str)返回整形
# print(a)

#r' ' 表示默认不转义  多换行
print(r'\\\\\\\t\\\\\\')
print('''line1
line2
line3''')

#and or not
print(1<2 or 1>8)

#空值 None
#/ 和 // 全大写表示常量PI
#Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf
print(10/3)
print(10//3)
print(10%3)


#ASCII-->Unicode(扩展4bits)-->UTF-8(节省内存)
# 中文字符和编码有关系的，utf-8编码下，是3个字节
# str和bytes互相转换时 使用UTF-8
print(ord('中'))
print(chr(25991))
print('中文测试')
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print(b'ABC'.decode('ascii'))

#类似c格式化输出 format()格式输出
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


# list -1获取最后一个元素,同理-2倒数第二个
#list里面可以是不同类型
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[-1])
classmates.append('Adam')
classmates.insert(1, 'Jack')
classmates.pop(2)
print(classmates)
s = ['python', 'java', ['asp', 'php'], 'scheme']

#tuple 元组类似于list  不可修改 即是指向不变
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
classmates = ('Michael', 'Bob', 'Tracy')
t=(1,)
print(classmates,t)


#循环 elif     循环 for in
sum=0;
for x in range(101):
	sum+=x
print(sum)
#while break和continue不可滥用,防止出错
n=1
while n<11:
	if n==5:
		break
	print(n)
	n+=1
print('end')

#dict字典 相对于map,key不可变,list不可以作为key
d = {'Michael': 95, 'Bob': 75, 'Tracy':90}
d['Bob']=88
print(d['Bob'])
print('Kizuk1' in d)  #判断Kizuk1是否在d
print(d.get('Kizuk1'))
print(d.get('Kizuk1','不存在-1'))
print(d.pop('Bob'))  #删除Bob
#set 不重复 list初始化
s = set([1, 1, 2, 2, 3, 3])
s.add(4) 
s.add(4)
s.remove(4)
# &和|  交和并
print(s&set([1,2]))
print(s|set([1,2,7,8]))


#list和str
a=['s','b','a']
a.sort()
print(a)

s='abc'
print(s.replace('a','A'))  #replace 创建了新的字符串'Abc'
print(s)


#函数 内置函数 别名
a=abs
print(a(-12))
print(hex(17))
#自定义和导入 from filename import funname 
def my_fun():
	print('hello world!')
def nop():   #空函数
	pass

#函数可以检测参数个数 TypeError,但是不能检测出参数类型不同
#函数返回值实际上是tuple
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('参数类型不同')
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-32))
# my_abs('s')

#定义默认参数要牢记一点：默认参数必须指向不变对象！ 改法
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
#可变参数思路 1.传入list和tuple 2.参数前面加入*-->可变参数 传入的是tuple
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
#*nums表示把nums这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))

#关键词参数 **kw
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值
#组合参数顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#尾递归 汉诺塔 斐波那契
def fact(n):
	return fact_iter(n,1)
def fact_iter(num,product):
	if(num==1):
		return product
	return fact_iter(num-1,num*product)

def move(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(3,'A','B','C')




#高级特性 切片 左闭:右开:隔几个
l=list(range(10))
print(l[0::2])
#迭代 iterator 测试迭代  enumerate函数建立list索引
from collections import Iterable
print(isinstance('adsf',Iterable))

for i,v in enumerate(['A','s']):
	print(i,v)

def find(L):
	max=min=0
	for a in L:
		if a>max:
			max=a
		if a<min:
			min=a
	return (min,max)

print(find([7,1,5,2,3,1,5]))

# 列表生成器  限制生成列表
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'ABC' for n in 'xz'])
#字典
d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([x.lower() for x in L1 if isinstance(x,str)])

#生成器 []列表 ()generator 生成器返回一个generator对象
#这个不是函数 是一个generator next()调用获取下一个数据 实际上用for获取下一个值
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n+=1
	return 'done'
f=fib(6)
print(f)

# 杨辉三角生成器 L.append(0)加一个元素
def triangles():
	L=[1]
	while True:
		yield L
		L.append(0)
		L=[L[i-1]+L[i] for i in range(len(L))]
		

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
# Iterator对象表示的是一个数据流，惰性计算

#map高阶函数
def f(x):
	return x*x
print(list(map(f,range(10))))

#reduce
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


#filter求素数 惰性过滤
def odd_iter():
	n=1
	while True:
		n+=2
		yield n
def not_divisible(n):
	return lambda x:x%n>0
def primes():
	yield 2
	it=odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(not_divisible(n), it)
# 应用 打印100以内的素数
for n in primes():
	if n<100:
		print(n)
	else:
		break

# 排序 sorted() 默认ASCII的大小比较 key作为条件 reverse反向输出
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# def by_name(t):
#     return t[0].lower()
# def by_score(t):
#     return -t[1]

# 函数作为返回参数
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# decorator就是一个返回函数的高阶函数   未看

#偏函数 改变默认函数的参数
import functools
int2=functools.partial(int ,base =2)
print(int2('10001001'))



#模块
#args存储了命令行的所有参数
#python 1.py 25(后面是参数)
# import sys

# def test():
# 	args=sys.argv
# 	if len(args)==1:
# 		print('Hello')
# 	elif len(args)==2:
# 		print('Hello,%s!'% args[1])
# 	else:
# 		print('to many')

# if __name__=='__main__':
# 	test()
print('\n')
import test
print(__name__)

#面向对象 初始化函数
#类里面的变量前面加上__变成私有的
class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print(self):
		print('%s:%s point' %(self.__name,self.__score))

brat=Student('甲贺忍蛙',90)
#修改不报错但是不生效
brat.__name=80
brat.print()

#动态语言 鸭子类型 多态 isinstance(dog,Animal)
#getattr()  setattr()  hasattr()
#一个类的属性(类似静态)

#高级面向对象  给一个类绑定方法
# __slots__  对绑定的属性限制 只对该类起作用 不对子类起作用
class Student(object):
	__slots__=('name','age')

def set_(self,name):
	self.name+=name

Student.set_=set_

#@property装饰器就是负责把一个方法变成属性调用  限制属性 没看


#多重继承  MixIn设计
# class Dog(Mammal, RunnableMixIn):
#     pass


#定制类  自己写__str__() 相当于java 的getString()
# 在命令行模式 是用__repr__    偷懒写__repr__ = __str__
# 类的for in 循环 用__iter__
# 类的下标表示 __getitem__  切片需自己继续改写
# 归功于动态语言的“鸭子类型”

# 调用不存在的属性可以在类里面写方法  网站调用动态Api
def __getattr__(self, attr):
    if attr=='score':
        return 99

# __call__() 调用实例

#枚举类
from enum import Enum
Month = Enum('test', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#value 1开始 的int
for name,member in Month.__members__.items():
	print(name,member,member.value)
#派生的enum枚举类

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday)
print(Weekday.Sat)
print(Weekday.Sat.value==6)


# 元类：要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# Traceback (most recent call last):  追踪出错
# 记录错误 logging
# import logging 

# def foo(s):
# 	return 10/int(s)
# def bar(s):
# 	return foo(s)*2
# def main():
# 	try:
# 		bar('0')
# 	except Exception as e:
# 		logging.exception(e)
# main()
# print('END')


# 抛出异常,打印异常
# def foo(s):
# 	n=int(s)
# 	if(n==0):
# 		raise ValueError('invalid value:%s' %s)
# 	return 10/n

# def bar():
# 	try:
# 		foo('0')
# 	except ValueError as e:
# 		print('ValueError!')
# 		raise
# bar()


# 调试print assert -0 关闭assert  logging
# 单步调试 pdb  python -m pdb err.py   pdb.set_trace()
# ide 调试  单元调试 文档测试


# I0编程 file-like Object  流-->read()               
# read()一次性读写 read(size)保险  with 自动调用close()
with open('C:/Users/lenovo/dir/test.txt','r') as f:
	for line in f.readlines():
		print(line.strip())

# encoding error参数
# 写文件  a追加 w覆盖写
with open('C:/Users/lenovo/test.txt','w') as f:
	f.write('\nhello,world!')

# StringIO BytesIO
from io import StringIO
f=StringIO('Hello!\nHi!\nGood!')
while True:
	s=f.readline()
	if s=='':
		break
	print(s.strip())

from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# os和根目录
import os
print(os.name)
# print(os.environ.get('PATH'))
print(os.path.abspath('.'))
# os.mkdir('C:/Users/lenovo/testdir')
# os.rename('kkk.txt','test.txt')
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 把变量从内存中变成可存储或传输的过程称之为序列化 JSON
# dump()方法可以直接把JSON写入一个file-like Object
import json
d=dict(name='Bob',age=20,score=90)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 为Student专门写一个转换函数
def stdtodict(std):
	return{'name':std.name,'age':std.age,'score':std.score}

s = Student('Bob', 20, 88)
# print(json.dumps(s,default=stdtodict))
print(json.dumps(s,default=lambda obj:obj.__dict__))


# 正则表达式 正则切割 分组
# 正则匹配是贪婪匹配 加？变成非贪婪
import re
print(re.split(r'[\s\,\;]+','a s  df     d , d ;s'))
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0),m.group(1),m.group(2))

# 重复使用可以先编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())

# Email地址正则
import re
def is_email(addr):
	if re.match(r'^([\w.]+)@([\w]+.com)',addr):
		return True
	else:
		return False

#小易喜欢的单词
# import re
# def danci(s):
# 	if re.search(r'[^A-Z]+',s) or re.search(r'([A-Z])\1',s) or re.search(r'([A-Z])[A-Z]*([A-Z])[A-Z]*\1[A-Z]*\2',s):
# 		print('Dislikes')  
# 	else:
# 		print('Likes') 
# str=input()
# danci(str)
