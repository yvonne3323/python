#函数嵌套调用

def func1():
    print("func1() is called")
def func2():
    print("func2() is called")
    func1()
func2()

#demo 一个函数（打印一条线）另一个函数（打印自定义行数的横线）
def print_line():
    '''
    打印一条横线
    :return:
    '''
    print("-" * 50)


#print_line()

def print_lines(num): # param 参数
    '''
    打印多条横线
    :param num: 打印的行数 
    :return: 
    '''
    for i in range(num):
        print_line()
print_lines(5)

#demo2 一个函数（三个数的和）另一个函数（三个数的平均值）
def sum_3_nums(num1, num2, num3):
    '''
    三个数的和
    :param num1: 
    :param num2: 
    :param num3: 
    :return: 
    '''
    return num1 + num2 + num3

def avg_3_nums(a,b,c):
    '''
    三个数的平均值
    :param num1: 
    :param num2: 
    :param num3: 
    :return: 平均值 float
    '''
    return sum_3_nums(a,b,c) / 3

print(sum_3_nums(1, 2, 3))
print(avg_3_nums(1, 2, 3))


#局部变量：在函数内部定义的变量，只能在函数内部使用
def test1():
    num = 10
    print("在test1函数内部的变量是%d" % num)

def test2():
    num = 20
    print("在test2函数内部的变量是%d" % num)

test1()
test2()

#全局变量：在函数外部定义的变量，一般放在所有函数最前面
num = 10 #建议大写加下划线
def test1():
    num = 100 #如果在一个函数中直接使用全局变量 =新数据，
    #那么在函数内部会定义一个局部变量 与全局变量同名
    print("在test1函数内部的变量是%d" % num)

def test2():
    global num #如果在一个函数中想要修改全局变量的值,需要使用global关键字
    num = 200
    print("在test2函数内部的变量是%d" % num)

def test3():
    print("在test3函数内部的变量是%d" % num)

test1()
test2()
test3()


#函数之间的关联

#共用同一个变量（全局变量）

#函数的返回值被当作实参
def testa():
    return 100
def testb(num):
    print(num)
result = testa()
testb(result)

#函数中调用另一个函数（函数嵌套调用）

#高内聚，低耦合
#一个函数的改变尽量不会影响到其他函数

#封装思想
#把独立功能做成一个函数