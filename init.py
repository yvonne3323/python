#魔法方法:__init__,__str__,__del__
#python自带的，有一些特殊功能，往往带有双下划线
'''
class MacBookPro(object):
    def set_pro(self):
        self.cpu = "i7"
        self.memory = "16G"

    def print_info(self):
        print("当前电脑配置：",self.cpu,self.memory)

#常见一个苹果笔记本电脑对象
my_mac_book = MacBookPro()
my_mac_book.set_pro() #不加这条会报错
my_mac_book.print_info()

class MacBookPro(object):
    def __init__(self):
        """"__init__方法一般会对刚刚创建成功的对象 进行初始化(设置一些默认属性)"""
        self.cpu = "i7"
        self.memory = "16G"

    def print_info(self):
        print("当前电脑配置：",self.cpu,self.memory)

#常见一个苹果笔记本电脑对象
my_mac_book = MacBookPro() #1,创建对象 2,自动调用__init__方法 且self指向刚刚创建的对象
my_mac_book.print_info()

my_mac_book2 = MacBookPro() #调用__init__的时候,括号里的实参传递给__init__,
#括号里什么都没有,就默认传递一个self
#my_mac_book2 = MacBookPro("i11",64) 没有地方给,init已经传递了一个self给对象
my_mac_book2.print_info() #结果一样
'''
#改变不能更改属性的问题

class MacBookPro(object):
    def __init__(self,cpu="i7",memory="16G"):
        self.cpu = cpu
        self.memory = memory

    def print_info(self):
        print("当前电脑配置：",self.cpu,self.memory)

my_mac_book = MacBookPro() 
my_mac_book.print_info()

my_mac_book2 = MacBookPro("i11","64G")
my_mac_book2.print_info()
