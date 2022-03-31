#initialisation
import pygame,sys,random,os,datetime,numpy
from pygame.locals import *
import time as tm
import pygame.freetype
#ctrl r 读取，ctrl s保存

#全局常量
PLLS=(
    'PLL1','PLL2','PLL3','PLL4','PLL5','PLL6','PLL7','PLL8','PLL9','PLL10','PLL11',
    'PLL12','PLL13','PLL14','PLL15','PLL16','PLL17','PLL18','PLL19','PLL20','PLL21')
CLS=('Orange','Red','Blue','Green','White','Yellow')
 


#类区
class Stats():
    def __init__(self):
        '''
        initlist={'PLL1':[0,[],0],'PLL2':[0,[],0],'PLL3':[0,[],0],'PLL4':[0,[],0],'PLL5':[0,[],0],'PLL6':[0,[],0],
        'PLL7':[0,[],0],'PLL8':[0,[],0],'PLL9':[0,[],0],'PLL10':[0,[],0],
        'PLL11':[0,[],0],'PLL12':[0,[],0],'PLL13':[0,[],0],'PLL14':[0,[],0],'PLL15':[0,[],0],
        'PLL16':[0,[],0],'PLL17':[0,[],0],'PLL18':[0,[],0],'PLL19':[0,[],0],'PLL20':[0,[],0],'PLL21':[0,[],0],},
        '''
        
        #数据的格式：initlist里面包含21个键值，'PLL1'对应一个列表。
        #列表的[0]是总次数，列表的[1]是一个列表，包含还原时间的浮点数,[2]对应的是失败的次数
        self.stats={
            'Red':{'PLL1':[0,[],0],'PLL2':[0,[],0],'PLL3':[0,[],0],'PLL4':[0,[],0],'PLL5':[0,[],0],'PLL6':[0,[],0],
        'PLL7':[0,[],0],'PLL8':[0,[],0],'PLL9':[0,[],0],'PLL10':[0,[],0],
        'PLL11':[0,[],0],'PLL12':[0,[],0],'PLL13':[0,[],0],'PLL14':[0,[],0],'PLL15':[0,[],0],
        'PLL16':[0,[],0],'PLL17':[0,[],0],'PLL18':[0,[],0],'PLL19':[0,[],0],'PLL20':[0,[],0],'PLL21':[0,[],0],},
            'Orange':{'PLL1':[0,[],0],'PLL2':[0,[],0],'PLL3':[0,[],0],'PLL4':[0,[],0],'PLL5':[0,[],0],'PLL6':[0,[],0],
        'PLL7':[0,[],0],'PLL8':[0,[],0],'PLL9':[0,[],0],'PLL10':[0,[],0],
        'PLL11':[0,[],0],'PLL12':[0,[],0],'PLL13':[0,[],0],'PLL14':[0,[],0],'PLL15':[0,[],0],
        'PLL16':[0,[],0],'PLL17':[0,[],0],'PLL18':[0,[],0],'PLL19':[0,[],0],'PLL20':[0,[],0],'PLL21':[0,[],0],},
            'White':{'PLL1':[0,[],0],'PLL2':[0,[],0],'PLL3':[0,[],0],'PLL4':[0,[],0],'PLL5':[0,[],0],'PLL6':[0,[],0],
        'PLL7':[0,[],0],'PLL8':[0,[],0],'PLL9':[0,[],0],'PLL10':[0,[],0],
        'PLL11':[0,[],0],'PLL12':[0,[],0],'PLL13':[0,[],0],'PLL14':[0,[],0],'PLL15':[0,[],0],
        'PLL16':[0,[],0],'PLL17':[0,[],0],'PLL18':[0,[],0],'PLL19':[0,[],0],'PLL20':[0,[],0],'PLL21':[0,[],0],},
            'Yellow':{'PLL1':[0,[],0],'PLL2':[0,[],0],'PLL3':[0,[],0],'PLL4':[0,[],0],'PLL5':[0,[],0],'PLL6':[0,[],0],
        'PLL7':[0,[],0],'PLL8':[0,[],0],'PLL9':[0,[],0],'PLL10':[0,[],0],
        'PLL11':[0,[],0],'PLL12':[0,[],0],'PLL13':[0,[],0],'PLL14':[0,[],0],'PLL15':[0,[],0],
        'PLL16':[0,[],0],'PLL17':[0,[],0],'PLL18':[0,[],0],'PLL19':[0,[],0],'PLL20':[0,[],0],'PLL21':[0,[],0],},
            'Green':{'PLL1':[0,[],0],'PLL2':[0,[],0],'PLL3':[0,[],0],'PLL4':[0,[],0],'PLL5':[0,[],0],'PLL6':[0,[],0],
        'PLL7':[0,[],0],'PLL8':[0,[],0],'PLL9':[0,[],0],'PLL10':[0,[],0],
        'PLL11':[0,[],0],'PLL12':[0,[],0],'PLL13':[0,[],0],'PLL14':[0,[],0],'PLL15':[0,[],0],
        'PLL16':[0,[],0],'PLL17':[0,[],0],'PLL18':[0,[],0],'PLL19':[0,[],0],'PLL20':[0,[],0],'PLL21':[0,[],0],},
            'Blue':{'PLL1':[0,[],0],'PLL2':[0,[],0],'PLL3':[0,[],0],'PLL4':[0,[],0],'PLL5':[0,[],0],'PLL6':[0,[],0],
        'PLL7':[0,[],0],'PLL8':[0,[],0],'PLL9':[0,[],0],'PLL10':[0,[],0],
        'PLL11':[0,[],0],'PLL12':[0,[],0],'PLL13':[0,[],0],'PLL14':[0,[],0],'PLL15':[0,[],0],
        'PLL16':[0,[],0],'PLL17':[0,[],0],'PLL18':[0,[],0],'PLL19':[0,[],0],'PLL20':[0,[],0],'PLL21':[0,[],0],},}
        
    #输入文件名称来输出一个infolist
    def checktype(self,filename):
        #位置-生成PLL随机图片的绝对路径
        filename=filename.replace(directory+'Views/','')
        #print(filename)
        info=filename.split('-')
        topcol=info[0].split('/')[0]
        #读取顶层颜色
        pllname=info[1]
        
        infolist=[topcol,pllname]
        #print(infolist)
        #print(topcol,pllname)
        #注意这里要去掉文件夹地址的前缀
        
        return infolist
    #输入infolist和time来增加统计数据
    def addtostat(self,infolist,time):
        topcol,pllname=infolist[0],infolist[1]
        self.stats[topcol][pllname][0]+=1
        self.stats[topcol][pllname][1].append(time)
    def addfailtime(self,infolist):
        topcol,pllname=infolist[0],infolist[1]
        #print(self.stats[topcol][pllname][2])
        self.stats[topcol][pllname][2]+=1
        #print(self.stats[topcol][pllname][2])

    def show_by_name(self):
        namedict={}
        showstr=''
        #print(self.stats)
        for each in PLLS:
            thispllsum=0
            thisplltimes=0
            thispllfail=0
            for i in CLS:
                thispllsum+=sum(float(ttt) for ttt in self.stats[i][each][1])
                thisplltimes+=self.stats[i][each][0]
                thispllfail+=self.stats[i][each][2]

                #上面那一句，加上的是失败次数
            #print(2)
            if thisplltimes==0:
                thispllavg=0
            else:
                thispllavg=float(thispllsum/thisplltimes)
            namedict[each]=[thispllavg,thispllfail]    
        return namedict
    def save(self):
        numpy.save(savingplace,self.stats)     
    def read(self):
        self.stats=numpy.load(savingplace,allow_pickle=True).item()
        #print(type(self.stats))


#函数区
#读取图片.
def readpics(colourstate):
    #图片目录

    #位置-PLL随机图片的位置
    path=directory+'Views/'
    #print(path)
    allfiles=[]
    allpic=[]
    for each in colourstate:
        print(each,colourstate[each])
        
        if colourstate[each]==True:
            pathx=path+each+'/'
            #print(pathx)
            files=os.listdir(pathx)
            for i in files:
                apath=pathx+i
                allpic.append(apath)
        else:
            pass
    print('Language:%s'%lan[:-3])        
    '''
    for file in files: #遍历文件夹
        apath=path+file
        allpic.append(apath)
        '''
    del files,path
    return allpic
#读取相应PLL变化图
def showans(ainfolist):
    pllname=ainfolist[1]
    pllorder=pllname.replace('PLL','')
    #位置
    thispic=directory+'Arrows/PLL-'+pllorder+'.png'
    #print(thispic)
    ansimg=pygame.image.load(thispic)
    ansposi=ansimg.get_rect()
    screen.blit(ansimg,ansposi)
#获得绝对位置
def getpath():
    dir_path=(os.path.abspath(__file__)).replace('\\','/').replace('Main.py','')
    return dir_path
#预检测-若没有txt文件则自动生成
def checktxt(directory):
    try:
        stxt=open(directory+'colours.txt','r')
        if stxt.readline=='':
                  raise Exception
    except:
        stxt=stxt=open(directory+'colours.txt','w')
        stxt.write('Yellow:1\nWhite:0\nOrange:0\nRed:0\nBlue:0\nGreen:0\n'#colors
        +'EN:1\nCN:0'#language setting  
        )
        stxt.close()

















#主程序区
#位置-成绩存储位置,检查txt是否正常
print('欢迎使用PLL练习软件')
directory=getpath()
savingplace=directory+'data.npy'
checktxt(directory)
#初始化pygame
pygame.init()

#创建窗口,读取字体
size=width,height=600,600
bg=(30,30,30)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('PLL练习软件')
engfont=pygame.freetype.Font(directory+'ARLRDBD.TTF')
cnfont=pygame.freetype.Font(directory+'STCAIYUN.TTF')

#读取打乱模式
facef=open(directory+'colours.txt','r')
colourstate={}
clsx=['Yellow','White','Orange','Red','Blue','Green']
for i in range(6):
    x=facef.readline()
    colourstate[clsx[i]]=('1' in x)
# Language
lan=facef.readline()# ENGLISH
if '1' in lan:#use english
    language='EN'
    cnfont=engfont
else:
    language='CN'

allpic=readpics(colourstate)

#使用说明

if language=='CN':
    linea='使用说明'
    lineb='S键：生成存档，R键：读取存档'
    linec='X键：记入识别失败'
    lined='其他任意键：启动/结束计时'
    linee='最后一列的数字是失败次数'
    lines=[linea,lineb,linec,lined,linee]

elif language=='EN':
    linea='Instructions'
    lineb='S: Save records, R: Read records'
    linec='X: Mark this attempt failure'
    lined='Other keys: Start/End timing'
    linee='Last row is faliure count.'
    lines=[linea,lineb,linec,lined,linee]
#读取图片
asd=random.choice(allpic)
#print(asd)
img=pygame.image.load(asd)
position=img.get_rect()
#计时器状态初始化
interval,timing,showscore,startsaving=True,False,True,False
time=0.00
allstats=''
saved=0
astats=Stats()
try:
    astats.read()
except:
    pass

#一开始没有图片，空格键松开加载第一张图片，开始计时
#第二次按下停止计时，换成中场图片，打印时间
#第三次按下的时候和第一次按下效果相同
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        #读取与保存

        elif event.type ==KEYDOWN and event.key==115  and startsaving==False:
            startsaving=True
            astats.save()
        elif event.type ==KEYDOWN and event.key==114  and startsaving==False :
            startsaving=True
            astats.read()
        elif event.type== KEYUP and startsaving==True:
            startsaving=False 
        #启动计时，终止间隔
        elif event.type == KEYUP and event.key!=120 and interval==True and event.key!=306 and startsaving==False:
            saved=0
            timing=True
            interval=False
            tmp=random.choice(allpic)
            imga=pygame.image.load(tmp)
            infolist=astats.checktype(tmp)
            showscore=False
            timea=datetime.datetime.now()
        #进入间隔
        elif event.type == KEYUP  and interval==False and event.key!=306 and startsaving==False:
            interval=True
        #终止计时-失败
        elif event.type==KEYDOWN  and event.key==120:
            #print('FFFF')
            timeb=datetime.datetime.now()
            del timeb
            if saved==0:
                astats.addfailtime(infolist)
                saved=1
            #print(time)
            imga=None
            timing=False
            showscore=True
            allstats=astats.show_by_name()
            #print(astats.stats)
        #终止计时-成功
        elif event.type==KEYDOWN and timing==True and event.key!=306:
            timeb=datetime.datetime.now()
            tgap=timeb-timea
            #print(tgap)
            time='%.3f'%(tgap.seconds+tgap.microseconds/1000000)
            astats.addtostat(infolist,time)
            #print(time)
            imga=None
            timing=False
            showscore=True
            allstats=astats.show_by_name()
#显示单个PLL成绩
    screen.fill(bg)
    arect=engfont.render_to(screen,(20,200),str(time)+'S',fgcolor=(255,255,255),size=50)
#显示图片
    try:                                                       
        if showscore==True:
            pllname=infolist[1]
            pllorder=pllname.replace('PLL','')
            #位置
            thispic=directory+'Arrows/PLL-'+pllorder+'.png'
            ansimg=pygame.image.load(thispic)
            screen.blit(ansimg,(40,40))
            #print(1)
        screen.blit(imga,position)
    except:
        pass
#显示各个PLL成绩
    height=0
    for each in allstats:
        atime=allstats[each][0]
        failtime=allstats[each][1]
        if len(each)==4:
            each=each.replace('LL','LL0')
        astr=each+'   :   '+'{:.3f}'.format(atime)+'s'+'      '+str(failtime)
        height+=23
        engfont.render_to(screen,(350,height),astr,fgcolor=(255,255,255),size=20)
#显示使用说明
    ilheight=300
    for each in lines:
        ilheight+=25
        cnfont.render_to(screen,(20,ilheight),each,fgcolor=(255,255,255),size=20)
    pygame.display.update()
            





