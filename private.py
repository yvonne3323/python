#私有属性
'''
class Cat(object):
    def __init__(self,new_name,new_age):
        self.name =new_name
        self.age = new_age
    
    def set_age(self,age):
        if age > 0:
            self.age = age
        
    def print_info(self):
        print("%s的年龄是:%d" % (self.name,self.age))

tom_cat = Cat("汤姆",40)

#tom_cat.age = -100   有问题,加set_age限制
tom_cat.set_age(-100) #具体方法:如果一个属性,想对他赋值或者更改的时候,进行判断或验证,
                      #可以在类中定义一个方法,专门用来对这个属性进行判断
#但并不能实现因为定义了一个方法,而不能用类似下面的cat.age =100
#限制不能完全防住
tom_cat.age = 100

tom_cat.print_info()

#如果想要完全限制,即不可以用cat.age = 100这种语句更改属性,可以在属性名前加上两个下划线
class Cat(object):
    def __init__(self,new_name,new_age):
        self.name =new_name
        self.__age = new_age
    
    def set_age(self,age):
        if age > 0:
            self.__age = age
        
    def print_info(self):
        print("%s的年龄是:%d" % (self.name,self.__age))

tom_cat = Cat("汤姆",40)
#print(tom_cat.__age) 这是用不了的,私有属性,对外界不可见,会崩溃
tom_cat.__age = 100 #这样写,并不能更改属性,相当于给tom_cat添加了一个新的属性
tom_cat.print_info()

#为什么tom_cat.__age = 100不会崩溃
#在python中,私有是假的,其实是进行了名字重整
#格式: 将__属性名  改为  _类名__属性名
print(tom_cat._Cat__age)


#私有方法 不能在外界调用 
class BankService(object):
    def __bank_2_bank(self, money): #私有方法
        print("这里是一行之间的转账代码....")
        return True

    def transfer(self):
        money = int(input("请输入转账金额"))
        if money > 100000:
            if self.__bank_2_bank(money):
                print("转账成功")
            else:
                print("转账失败...")
        else:
            print("都没钱，还转什么啊！自己留着花吧!")


bank_service = BankService()
bank_service.transfer()  # 可以调用，是公有方法
#可以调用私有方法,但是没有意义,所以不要强制调用私有方法
#bank_service.__bank_2_bank()

#对象关联
class Classroom(object):
    def __init__(self,name):
        self.name = name

class Student(object):
    def __init__(self,name):
        self.name = name

#这是分别指向两个对象,怎么让学生在教室里
#让教室对象的属性指向学生对象

class205 = Classroom("205班")
stu1 = Student("学生1")

class205.student = stu1 #在教室对象中添加一个属性,指向学生对象

#也可以通过定义一个方法,然后调用这个方法的时候将另外一个对象的引用当作实参
class Classroom(object):
    def __init__(self,name):
        self.name = name
    def add_student(self,new_student):
        self.student = new_student
class Student(object):
    def __init__(self,name):
        self.name = name

class205 = Classroom("205班")
stu1 = Student("学生1")

class205.add_student(stu1)

#对象有了关系,怎么取用
class205.student #————>stu1————>Student("学生1")
class205.student.name #学生1


#关联多个对象
class Classroom(object):
    def __init__(self,name):
        self.name = name
    def add_student(self,new_student):
        self.student = new_student
class Student(object):
    def __init__(self,name):
        self.name = name

class205 = Classroom("205班") #创建教室对象
stu1 = Student("学生1") #创建学生1对象
stu2 = Student("学生2") #创建学生2对象
class205.add_student(stu1) #将学生1对象关联到教室对象
class205.add_student(stu2) #这样写,重新指向,会把stu1覆盖掉,只有stu2
print(class205.student.name) #学生2

'''
#要想不覆盖,应该使用列表
class Classroom(object):
    def __init__(self,name):
        self.name = name
        self.student = list() #创建一个空列表,用来存放学生对象
    
    def add_student(self,new_student):
        self.student.append(new_student) #将学生对象添加到列表中

class Student(object):
    def __init__(self,name):
        self.name = name

class205 = Classroom("205班")  #创建教室对象,name =205班,student = []
stu1 = Student("学生1") #创建学生1对象 name = 学生1
stu2 = Student("学生2") #创建学生2对象 name = 学生2

class205.add_student(stu1) #self指向class205,new_student指向stu1,append让stu1添加到列表中
class205.add_student(stu2) #self指向class205,new_student指向stu2,append让stu2添加到列表中

for temp in class205.student:
    print(temp.name) #学生1 学生2
