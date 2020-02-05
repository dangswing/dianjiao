#电教服务1923班
from random import randint
import time,os

fn='py.vbs' #模式3所需文件名
def mode3(ne): #模式3主体
    f=open(fn,'w')
    f.write(ne)
    f.close()
    os.system(fn)
            
print('''23班专属电教服务
1.取消关机
2.定时关机
3.消息提示''')

while True:
    ans=input('请输入序号：')
    if ans=='1':
        os.system('cls')
        os.system('shutdown -a')
        
    elif ans=='2':
        while True:
            try:
                os.system('cls')
                T=input('请输入时间（分钟）：')
                T=int(T)*60
                os.system('shutdown -s -t %d'%T)
                
                break
            except:
                print('请正确输入数字！')
    
    elif ans=='3':
        os.system('cls')
        cho=input('请选择类型：\n1.可关闭\n2.不可关闭')
        if cho=='1':
            ne=input('请输入内容：')
            ne='msgbox("'+ne+'")'
            mode3(ne)
        if cho=='2':
            ne=input('请输入内容：')
            ne='do\nmsgbox("'+ne+'")\nloop'
            mode3(ne)
            
        
