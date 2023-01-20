#函数的返回值拆包
'''
def get_info():
    high = 180
    weight = 70
    age = 18
    return high,weight,age #默认元组

#get_info()
#print(get_info())

a,b,c = get_info() #a,b,c,d = get_info() 会报错
print(a)
print(b)
print(c)

#通过*进行拆包
def test(a,b,c):
    print(a+b+c)

num =[11,22,33]

#问题:调用test函数,传递num列表中的值
    #test(num[0],num[1],num[2])
#若列表中的值很多，就很麻烦

test(*num) #可对列表，元组，集合进行拆包
#集合的顺序是随机的，所以拆包后如果顺序有影响
# 结果也就是随机的

#**进行拆包
def test2(name,web_site,age):
    print(name)
    print(web_site)
    print(age)

info = {
    "name":"小明",
    "web_site":"www.baidu.com",
    "age":18
    }
#test2(info) #会报错,info整体传给name

test2(**info) #对字典进行拆包
#相当于test2(name="小明",web_site="www.baidu.com",age=18)
#即命名参数 (前提：固定名字)
'''
#怎么解决固定名字所带来的崩溃问题
def test3(*args,**kwargs):
    print("---test3---")
    print("args:",args)
    print("kwargs:",kwargs)

def test4(*args,**kwargs):
    print("---test4---")
    print("args:",args)
    print("kwargs:",kwargs)
    #test3(args,kwargs) #均属实参，成为元组
    #此时test3的kwargs是一个空字典
    test3(*args,**kwargs) #拆包
    #相当于test3(11,22,33,name="小明",age=18)
test4(11,22,33,name="小明",age=18)





