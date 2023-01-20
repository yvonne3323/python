#缺省参数
#定义一个函数，模拟学生调用之后的结束
'''
def print_myself(name,school_age="xx学校",class_name="101"):
    """
    模拟实现,自我介绍
    """
    print("大家好,我是%s,我在%s上学,我在%s班" % (name,school_age,class_name))

print_myself("小明","xx学校","101")
print_myself("小红","xx学校","101")
print_myself("小刚","xx学校","101")
#实参重复太多，可以使用缺省参数(定义参数写好)
print_myself("小明")

#命名参数

def test(a,b,c):
    print("a=%d" % a)
    print("b=%d" % b)
    print("c=%d" % c)

#test(1,2,3) 普通实参 一一对应

test(b=1,a=2,c=3) #命名参数 不能出现多次

#用命名参数进行传递
print_myself("小明",class_name="xx学校",school_age="101")
print_myself("小灰灰2",class_name="xxx")
#不命名的参数必须在命名参数的前面

#test(a=1,2,c=3) #报错

#不定长参数 传递的实参个数任意

#1, *args 用来接收多余的位置参数
def sum_nums(a,b,*args):
    """
    求和函数
    """
    print("a=%d" % a)
    print("b=%d" % b)
    print("args=%s" %str(args) , type(args))
    sum = a + b
    #遍历元组
    for i in args:
        sum += i
    print(sum)
sum_nums(1,2,3)  #args=(3,) 为了与数学括号区分，写逗号
sum_nums(1,2,3,4,5,6,7,8,9,10)

#2, **kwargs 用来接收多余的关键字参数
def test2(a,b,*args,**kwargs):  #可以改为*c,**d
    print("a=%d" % a)
    print("b=%d" % b)
    print(args)  #多余的
    print(kwargs) #字典 多余带名字的
test2(1,2,3,4,e=5)

def test3(a,b,c=100,d=200,*args,**kwargs):
    print("a=%d" % a)
    print("b=%d" % b)

    print("c=%d" % c) #3
    print("d=%d" % d) #4
    print(args)
    print(kwargs)

test3(1,2,3,4,5,6,7,8,9,10,e=100,f=200)
'''
#若不希望c,d的值被改变 (少见)
def test4(a,b,*args,c=100,d=200,**kwargs):
    print("a=%d" % a)
    print("b=%d" % b)

    print("c=%d" % c) 
    print("d=%d" % d) 
    print(args)
    print(kwargs)

test4(1,2,3,4,5,6,7,8,9,10,e=100,f=200)


