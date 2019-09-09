f = open('C:\\Users\\Administrator\\PycharmProjects\\untitled\\jiqinag\\12.txt','a',encoding='utf-8')
#print(f.readlines())
#print(f.read())
#f.close()

#f.write('kajdkalkd')
f.writelines(['jkas\n','jnfkd\n','nfjewfk\n','uhjik\n','你是谁\n'])


def div(a,c):
    try:
        c=a/c
    except ZeroDivisionError:
        print('分母不能为0')
        return
    return c
print(div(19,0))
def operate_file():
    try:
        #open('jind','r')
        s=open('12.txt','w')
        s.read()
        s.write('jbijhb')
    except FileNotFoundError:
        print('文件不存在')
    except ValueError:
        print('文件已关闭')
operate_file()


