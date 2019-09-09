#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'


# 求出1+2+3.。。+100和
def qiu_he():
    s = 0
    for i in range(100):
        s = s + i + 1
    print(s)
# 求出100! 1*2*3*4....*100
def qiu_jie_cheng():
    s = 1
    for i in range(1,101):
        s *= i
    print(s)
# 求出100以内的质数
def zhi_shu():
    for i in range(2,101):
        if(i == 2):
            print(i)
            continue
        f = 1 # 1代表这个数是质数，0代表这个数不是质数
        for j in range(2, i):
            if (i % j == 0):
                f = 0
                break
        if(f == 1):
            print(i)


# 打印出九九乘法表（循环嵌套）
def jiu_jiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print(j,"X",i,'=',i*j,"\t",end="")
        print()
# 冒泡排序
def mao_pao():
    a = [90, 43, 2, 63, 6, 3, 4]
    #外层循环确定待排序的位置
    for i in range(len(a)-1,0,-1):
        #内层循环依次取相邻的两个数据
        for j in range(i):
            # if判断比较相邻两个数据的大小，如果前边大于后边的，则交换位置
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
    print(a)



if __name__ == '__main__':
    a = [90, 43, 2, 63, 6, 3, 4]
    #外层循环确定待排序的位置
    for i in range(len(a)-1,0,-1):
        #内层循环依次取相邻的两个数据
        for j in range(i):
            # if判断比较相邻两个数据的大小，如果前边大于后边的，则交换位置
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
    print(a)
i=1
while(i<101):
    print(i)
    i=i+1
def nmsl(a,b):
    print(a+b)

nmsl(7,8)

def nmsl(a,b):
    return a + b
c = nmsl(7,8)
print(c)



def jiqiang(*args,**kwargs):
    print(args)
    print(kwargs)
jiqiang({'name':'jiqina'},1,10,20,c=20,n=100)

if __name__ == '__main__':
   print("wo")


class ClassDemo():
    def aaa(self):
        print("woshiaaa")
    def bbb(self):
        print("woshibbb")
        self.aaa()

if __name__ == '__main__':
    c = ClassDemo()
    c.aaa()
    c.bbb()
p = 'caonima nshishui masl'
print(p.split())
s = "   bjkbajksjka     "
print(s.strip())
h = 'hsbd"jsa'
print(h.replace('"',"'"))

p = [1,4,4,8,6,7,9]
p.append(80)
print(p)

p.insert(2,90)
print(p)
m = [5,5,5,5]
p.extend(m)
print(p)
print(m)

p.pop()
print(p)
p.pop(-3)
print(p)

p.remove(1)
print(p)

d = {'name':'jiqinag','sex':'nan'}
d['age'] = 18
print(d)
print(d.pop('name'))
print(d)
del d['sex']
print(d)

i = {'id':80,'name':'io','mr.zhang':'leslie','po': 8}
i.clear()
print(i)


q = {'ji':'niu','sa':'ni','sn':'ui'}
e = {'mn':'bh','ob':'sb','ki':'pl'}
q.update(e)
print(q)
q = {'ji':'niu','sa':'ni','sn':'ui'}
e = {'mn':'bh','ob':'sb','ki':'pl'}
print(dict(q,**e))








