#类(模板)

class Person: 
    #Person 也为变量名  与函数名(全局变量名)类似
    #Person 类名(建议大驼峰取名)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("姓名：", self.name, "年龄：", self.age)
        #函数——>又称:方法(功能)
#类还有属性(即数据),此例子中无

#对象(实例),真实存在,具体对象
stus = Person("张三", 18) #创建对象的方式：类名()
#stus 变量指向 Person所在内存
stus.print_info() #指向print_info 加上()调用

stus2 = Person("李四", 19) #又创建对象,所以与stus不是一个
stus2.print_info()


class Dog: #经典类 
    color = "yellow"
    def run(self):
        print("狗在跑")

#定义类
class Dog2(object): #新式类 在python3与经典类一样
    pass

dog1 = Dog() #变量指向,像绳子拴着对象,好找
dog2 = Dog2()
dog3 = Dog()

print(id(dog1))
print(id(dog2))
print(id(dog3))
#均不一致

#实例方法
#通过类创建的对象，称为实例对象 dog1=Dog()

class Cat(object):
    def eat(self):
        print("猫在吃鱼")
    def drink(self):
        print("猫在喝水")
    def run(self):
        print("猫在跑")
    #def introduce(self):
        #name = "Tom"
        #age =2
        #print("我是%s,今年%d岁"%(name,age))
        #若此时这样描述,name是局部变量,
        #cat1与cat2的name不同,需要改变写法
    def introduce(self,name,age): #name,age为形参
        print("我是%s,今年%d岁"%(name,age))
cat1 = Cat()
cat1.eat() #通过 对象名.方法名() 调用方法
cat1.drink()
cat1.run()
cat1.introduce("Tom",2) #Tom,2为实参

cat2 = Cat()
cat2.eat()
cat2.drink()
cat2.run()
cat2.introduce("Jerry",3)

#实例属性
#上述例子中猫在吃喝跑，但都是统一的称为小猫，模棱两可

#按照introduce方法太麻烦
class Cat(object):
    def eat(self,name):
        print("%s在吃鱼" % name)
    def drink(self,name):
        print("%s在喝水" % name)
    def run(self,name):
        print("%s在跑" % name)
    def introduce(self,name,age): 
        print("我是%s,今年%d岁"%(name,age))
cat1 = Cat()
cat1.eat("Tom") 
cat1.drink("Tom")
cat1.run("Tom")
cat1.introduce("Tom",2) 
#如果要改名字，需要改四处，麻烦

class Cat(object):
    def set_name_age(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃鱼" % self.name)
    def drink(self):
        print("%s在喝水" % self.name)
    def run(self):
        print("%s在跑" % self.name)
    def introduce(self): 
        print("我是%s,今年%d岁"%(self.name,self.age))
#想象成有五个方法
cat1 = Cat()
cat1.set_name_age("Tom",2)
cat1.eat() 
cat1.drink()
cat1.run()
cat1.introduce() 

cat2 = Cat()
cat2.set_name_age("Jerry",3) #相当于set_name_age(cat2,"Jerry",3)
cat2.eat()
cat2.drink()
cat2.run()
cat2.introduce()
