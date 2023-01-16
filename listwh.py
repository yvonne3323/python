#列表(可以包括任意类型的数据，但是一般不建议)
nums = [11,22,33,44,55,66,77,88,99]
names =["yvonne","lily","lucy"]

print(names)
print(names[0])

print(names[3])
#越界，程序会报错

print(names[0:2]) #2不包含

#遍历：依次取出列表中的每一个元素

#while
i=0
while i<len(names): #len()获取列表的长度
    print(names[i])
    i+=1

# for(不需要知道列表的长度)
for name in names:
    print(name)

#列表的增删改查

#增加
names.append("chenxin") #在列表的最后添加一个元素
print(names)

#extend() 在列表的最后添加多个元素
names2 = ["老大","老二"]
names.extend(names2)
print(names)

#insert() 在指定位置添加元素(多了相当于增加)
names.insert(1,"老大") #老大成为1
print(names)

#删除

#del 删除指定位置的元素

del names[0]
print(names)

#pop() 删除最后一个元素

ret = names.pop()
print(ret) #要删除的数据
print(names)

#remove() #删除指定的元素

names.remove("lucy")
print(names)

#修改(小心越界)

names[0] = "Yvonne"
print(names)

#查找

#in

print("lucy" in names) #True/False

if "lucy" in names:
    print("找到了")

find_name = input("请输入要查找的名字：")
if find_name in names:
    print("找到了%s" % find_name)

#not in

ip = ["192.168.1.1","192.168.1.2"]
user_ip = input("请输入网站：")
if user_ip not in ip:
    print("可以正常浏览")
else:
    print("不可以浏览")

#count #统计某个元素在列表中出现的次数
print(names.count("lucy"))
print(names.count("cc"))

num=[1,4,7,8,3,5]
#sort() 排序(默认升序)

num.sort()
print(num)  

#不可以直接打印，因为sort()是在原列表上进行操作的
#即print(num.sort())是错误的

num.sort(reverse=True) #降序
print(num)

#reverse() 反转

num.reverse()
print(num)

#嵌套(最好三层以内)
school_names = [["北京大学","清华大学"],
["复旦大学","上海交通大学"],
["南京大学","东南大学"]
]

print(len(school_names)) #不关心元素类型

print(len(school_names[0]))

print(school_names[0][0]) #北京大学(小心越界)

