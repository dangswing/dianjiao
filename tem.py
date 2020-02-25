#电教服务——体温统计
from random import randint
from os import system
names=['姜某某','邱某','王某某','吴某某','王某某','仁某某','滑某']
while True:
    print('体温统计')
    for i in names:
        print('%s体温：%s℃'%(i,str(randint(361,369)/10)))
    input()
    system('cls')
