
#场景一 因为一个的更改而许多下标的更改
names = ['Alice', 'Beth', 'Dee-Dee']
print(names[2])
names.insert(0, 'Mike')
print(names[2])

#场景二 因为一个的更改而改变数据的位置
students = [[1001,"张三",18], [1002,"李四",19], [1003,"王五",20]]
print(students[1][2])

#字典 {}

#区分集合和字典
blank_set = set() #空集合
blank_dict = dict()  #空字典

#{key1:value1, key2:value2, key3:value3}

#定义一个人的信息
my_info = {'name':'张三', 'age':18,'web_site':'www.baidu.com'} #键值对
print(my_info['name'])

#场景一的更改
names_dict = {"001":"张三", "002":"李四", "003":"王五"}

print(names_dict["003"]) #永远是王五

#场景二的更改
students = {
    "1001":{"id": 1001,"name":"张三","age":18},
    "1002":{"id": 1002,"name":"李四","age":19},
    "1003":{"id": 1003,"name":"王五","age":20}
}
print(students["1002"]["age"]) #永远是19


class_info = {
    "name":"二年级xxx班",
    "bzr_name":"xxx",
    "students_num":30,
    "average_height":130
}

#字典的遍历 集合的遍历不一定是有序的,字典的遍历也是

for temp in class_info: #默认只会获得key
    print(temp)

for temp in class_info.values():
    print(temp)

for temp in class_info.items():
    print(temp)

for temp in class_info.items():
    print("%s:%s" % (temp[0],temp[1]))
#    print("%s:%s" % (temp))

#字典的增删改查
#增加

class_info["average_weight"] = 30
print(class_info)

#删除

#删除某个键值对

del class_info["average_weight"]
print(class_info)

#清空整个字典

class_info.clear()
print(class_info) #{}

#删除整个字典
del class_info
print(class_info) #报错

#修改
class_info["name"] = "python1805"
print(class_info)

#查找

print(class_info["name"])
# 有隐患 print(class_info["name1"]) #报错

#安全的查找
print(class_info.get("name1")) #None
print(class_info.get("name1","没有这个键")) #没有这个键


#使用场景总结
#列表
#如果储存多个相同数据的时候，且可能需要对数据进行操作

#元组
#如果储存多个相同数据的时候，且不需要对数据进行操作
#eg:储存每年国家颁布的银行存款利率

#集合
#往往在需要去重的时候使用

#字典
#如果需要储存多个不同数据的时候，且这些数据相当于一个整体
#eg:储存一个班级的信息

# class_info = {
#     "class_name":"python1805",
#     "class_teacher":"张三",
#     "students":[
#         {"name":"张三","age":18},
#         {"name":"李四","age":19},
#         {"name":"王五","age":20}
#     ]
# }
