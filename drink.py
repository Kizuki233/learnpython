# x=float(input('你带了多少元？'))
# print('你带了',x,'元')
x=20
a=int(x/2)
b=int(x/2)
n=int(x/2)
while a>=2 or b>=4:    
	if a>=2 and b>=4:        
		c=a%2+int(a/2)+int(b/4)        
		d=b%4+int(a/2)+int(b/4)        
		n=n+int(a/2)+int(b/4)        
		a=c        
		b=d    
	elif a>=2 and b<4:        
		c=a%2+int(a/2)        
		d=b+int(a/2)        
		n=n+int(a/2)        
		a=c        
		b=d    
	elif a<2 and b>=4:        
		c=a+int(b/4)        
		d=b%4+int(b/4)        
		n=n+int(b/4)        
		a=c        
		b=d
	print('那么你最多能喝',n,'瓶啤酒\n剩余',x%2,'元，',a,'个盖',b,'个空瓶')



