# 电教服务——网课进度伴侣
# 如果网课真的无聊：
# 1.解决上网课的人
# 2.解决被上网课的人
# 这里采用了方案二
import os,time

sec=int(input('请输入时间(秒)：'))
hz=input('请输入刷新频率(秒)：')
os.system('cls')
t1=time.time()
while True:
    t=time.time()
    if t-t1>=sec:
        break
    tin=t-t1
    print('网课进度：'+str(round(tin/sec*100,2))+'%')
    time.sleep(eval(hz))
    os.system('cls') #这句话加不加可以实现不同效果
print('网课进度：100%！')
while True:
    pass
