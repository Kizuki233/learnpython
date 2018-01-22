#模块
import sys
#args存储了命令行的所有参数
#python 1.py 25(后面是参数)
def test():
	args=sys.argv
	if len(args)==1:
		print('Hello')
	elif len(args)==2:
		print('Hello,%s!'% args[1])
	else:
		print('to many')
	print(__name__)

if __name__=='__main__':
	test()