#电教服务——作业统计
#version=1.2.3
import os

subjects=['语文','数学','英语','物理','化学','生物','政治','地理']
names=['姜某某','邱某','王某某','空','吴某某','王某某','仁某某','滑某']
l=[]

for i in subjects:
    os.system('cls')
    print('电教服务——作业统计[322]\n')
    for j in range(8):
        print('%d.%s'%(j+1,names[j]))
    print()
    l.append(input('请选择[%s]优秀的同学：'%i))

for i in range(8):
    for j in range(8):
        l[i]=l[i].replace(str(j+1),names[j]+'、')
    l[i]=l[i][:len(l[i])-1]
    
os.system('cls')

for i in range(8):
    a=subjects[i]+'：'+l[i]+'优秀'
    if a.count('、') != 6:
        a+='，'
        for j in names:
            if a.count(j)==0:
                a=a+j+'、'
        a=a.replace('空、','')
        a=a[:len(a)-1]+'合格'
    print(a)

while True:
    pass
