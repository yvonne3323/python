
#self往往指向自己,即谁调用的方法,那么self就指向谁
#xxxx.test()  test()方法中的self就指向xxxx
#self可以更改名字,但是一般都是self

class Dog(object):
    def set_name(a,b): #原本 def set_name(self,name) 这也说明这两个参数名字是可以改变的
        a.name = b #这里的name要与下面self.name的name一致

    def print_name(self):
        print(self.name)

xiaohuang = Dog()
xiaohuang.set_name('小黄') #等价于set_name(xiaohuang,'小黄')
xiaohuang.print_name()

class Hero(object):
    def set_name(self,new_name):
        self.name = new_name  #这里的self.name的name决定了内存中的命名,属性名字
    def get_name(self):
        print(self.name) #对象中有叫name的属性,所以可以直接调用,如果不一致则会报错
        #print(self.name1) 这里会报错,因为对象中没有叫name1的属性
chen = Hero()
chen.set_name("陈") 
#上述也可以写成 chen.name = "陈" 但是这样写不利于后期维护,无法添加限制
chen.get_name()

#为age添加限制,需要chen.set_name,这样反而chen.name不好
class Hero(object):
    def set_name_age(self,new_name,new_age):
        if new_age > 0:
            self.age = new_age
        else:
            self.age = 0 #年龄不合法
        self.name = new_name 
    def get_name(self):
        print(self.name,self.age)
chen = Hero()
chen.set_name_age("陈",20) 
chen.get_name()