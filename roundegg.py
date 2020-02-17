from random import randint
import time

print('电教服务——元旦特别版')
T=3 #倒计时
a=input('开始抽奖：')
if a=='test': #便于测试
    T=0
for i in range(T):
    print(T-i)
    time.sleep(1)
while True: #防止重复
    a,b,c=randint(2301,2364),randint(2301,2364),randint(2301,2364)
    if a!=b and b!=c and a!=c:
        break
    
time.sleep(1)
print('恭喜[%d]号同学获得一等奖：[精美钥匙链]x1！'%a)
time.sleep(1)
print('恭喜[%d]号同学获得二等奖：[精美圆蛋]x1！'%b)
time.sleep(1)
print('恭喜[%d]号同学获得一等奖：[精美气球]x1！'%c) #后来气球变成了鸡腿
time.sleep(1)
print('[抽奖结束]')
while True:
    pass
