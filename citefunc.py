#引用:就是地址，
# 可以理解为存放数据的空间在内存中的编号
'''
a = 1
b = a
b = 2

print(a) #1
print(b) #2

c =[11,22]
d = c
d.append(33)
print(c) #[11,22,33]
print(d) #[11,22,33]
print(id(c)) 
print(id(d)) #与上一致
#可以认为c,d指向同一个地址,所以是一致的
#一字节*1024=1kb
#一kb*1024=1mb
#一mb*1024=1gb
#一gb*1024=1tb



aa = [111,222,333]
bb = aa
bb = [444,555,666]
#此时bb指向新的地址,aa指向原来的地址
#=不是赋值，而是引用(指向)


def test(p):
    p.append(33)
    print("p",p)

nums = [11,22]
print("nums",nums)
test(nums) #此时将列表的引用当作了实参进行传递
print("nums",nums)
#说明实参都是指向，不是复制
#如果nums是元组,但是元组不能改,所以也不会有p


#函数名也是引用,是变量名

def test2():
    print("in test2")
    return 100
num = test2 
#此时漏了()但没有崩溃,即num指向test1(内存代码)
print(num)
print(test2)

def test3():
    print("in test3") #test3指向代码
    return 100

def test3():
    print("in test4") #test3指向新代码

test3() #in test4
xx = test3
xx() #in test4
#做什么:装饰器


#匿名函数，没有名字的函数,常用于简单的函数
#lambda 形参1,形参2,形参3....:表达式

#举例
lambda x,y:x+y #默认返回值为表达式的结果

#调用
#一般情况下，先定义一个变量，然后用这个变量指向匿名函数
#那么此时就可以通过变量名()来调用匿名函数

my_test = lambda x,y:x+y
num = my_test(1,2)
print(num) 

#方式二：将匿名函数当作实参
def fun(a,b,opt):
    print("a=%d" %a)
    print("b=%d" %b)
    print("result = %d" %opt(a,b))

fun(1,2,lambda x,y:x+y) #opt指向匿名函数

#注意点：
#1,如果匿名函数不需要参数
#lambda :表达式
#2,如果匿名函数只有一个参数
'''
#匿名函数应用:对列表中嵌套字典，进行排序

stus = [
    {"name":"zhangsan","age":18},
    {"name":"lisi","age":19},
    {"name":"wangwu","age":17},
    {"name":"zhaoliu","age":20}
]

#nums = [11,22,3,55,223,45645,1,33,0]
#nums.sort() #默认升序
#print(nums)
#那字典怎么排序
#stus.sort() #报错

#stus.sort(key=函数的引用)
def sort_by_age(temp_dict):
    return temp_dict ["age"]
stus.sort(reverse=True,key=sort_by_age) #不要多写括号
print(stus)

#匿名函数更简略
#stus.sort(key=lambda x:x["age"]) #x是字典
stus.sort(key=lambda temp_dict:temp_dict["age"])

#递归函数 函数自己调用自己

#求阶乘 限制：嵌套次数少于1000次
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5)) #120

#之前的方法
def factorial2(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial2(5)) 

