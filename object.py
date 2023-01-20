#面向对象(object-oriented Programming)-OOP

# 编写一个程序，完成1个学生的基本操作
#可以输出学习信息(姓名，年龄)

#遍历
def print_info(name_temp,age_temp):
    print("姓名：",name_temp,"年龄：",age_temp)

#定义一个变量储存姓名
name = "张三"
#定义一个变量储存年龄
age = 18
#遍历姓名-年龄
print_info(name,age)

#方法一:打印3个学生的信息

name = "张三"
age = 18
print_info(name,age)
name = "李四"
age = 19
print_info(name,age)
name = "王五"
age = 20
print_info(name,age)
#这样的代码，如果学生的数量很多，就会很麻烦

#方法二：
names = ["张三","李四","王五"]
ages = [18,19,20]
print_info(names[0],ages[0])
print_info(names[1],ages[1])
print_info(names[2],ages[2]) #也可以for循环
#但如果下标错位就会出错


#避免容易出错的问题
#方法三：
stus = [ #stus 全局变量 
    {
        "name":"张三",
        "age":18
    },
    {
        "name":"李四",
        "age":19
    },
    {
        "name":"王五",
        "age":20
    }
]
print_info(stus[0]["name"],stus[0]["age"])
#数据(stus)多,功能少(def),且脱离,容易出乱

#方法四：
class Person: #将数据和功能封装在一起
    #数据
    def __init__(self,name,age): 
        self.name = name
        self.age = age
    #功能
    #遍历打印所有姓名——年龄
    def print_info(self):
        print("姓名：",self.name,"年龄：",self.age)

stu = Person("张三",18)
stu.print_info()
stu2 = Person("李四",19)
stu2.print_info() #类似于a.lower()

