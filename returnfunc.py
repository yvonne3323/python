
#return的作用
#1. 能够将函数的结果当作返回值，返回调用的地方
def test():
    print("test函数被调用")
    return 1
print("---1---")
a = test() #存储函数的返回值，用一个变量=函数名()
print("---2---")
print("a=%d" % a ) #打印变量

#2.结束函数的执行

def test2():
    return 1 #有一个return被执行,后面的代码不再执行
    print("test2函数被调用")
    return 1
    print("---1---")
    return 100
   
test2()
# 当然,可以不返回值,直接return

#return返回多个值
def test3():
    a = 100
    b = 200
    c = 300
    return a,b,c  #默认相当于 return(a,b,c)
    #return [a,b,c] 这是列表
ret = test3()
print(ret)

#demo (月工资，计算是否交税)
#    <=5000  无需交税
#    >5000  交税25%
def cal_rate(salary):
    '''
    计算税率
    :return: 返回税额
    '''
    if salary <= 5000:
        return 0
    else:
        return salary * 0.25
money = int(input("请输入月工资："))
rate = cal_rate(money)
print("税额是：%.2f" % rate)



#函数类型
# 无参数，无返回值
def testa():
    print("testa函数被调用")
testa()

# 无参数，有返回值
def testb():  #要求：程序不崩溃
    '''
    获取年龄
    :return: 输入纯数字,返回int类型,否则返回None
    '''
    age = input("请输入年龄：")
    if age.isdigit() == True:
        # 如果是纯数字,转换为int类型
        return int(age)
    else:
        return 0
age = testb() #如果testb()函数代码全部执行完毕，且没有执行到return，那么此时就相当于return None
if age == 0:
    print("输入错误")
elif age >= 18:
    print("成年人")
else:
    print("未成年人")

# 有参数，无返回值
def testc(name,age):
    print("姓名：%s,年龄：%d" % (name,age))
testc("张三",18)

# 有参数，有返回值

def testd(name,age):
    return name,age
name,age = testd("张三",18)
print("姓名：%s,年龄：%d" % (name,age))

def add_nums(num):
    sum_result = 0
    for i in range(1,num+1):
        sum_result += i
    return sum_result
num = int(input("请输入一个数字："))
result = add_nums(num)
print("1到%d的和是:%d" % (num,result))
