#布尔类型(bool)：True，False
#隐式转换为整型，True为1，False为0 
print(True+1) #2
#bool(x)函数，将x转换为布尔类型 0，空字符串，空列表，空元组，空字典，空集合，None都是False
#其他都是True
print(bool(0)) #False
#程序执行方式：顺序，选择if，循环while

#定义一个变量为True，打印我喜欢你，然后变量为False，打印我不喜欢你
can_like_you = False

if can_like_you:#条件
    print("我喜欢你")
else:
    print("我不喜欢你")

if True:
    print("我")
else:
    print("你")#永远不会执行，淡黄色

#比较运算符

print(1 == 1) #True
print(1 != 1) #False
print(100 > 1)
print(100 < 1)
print(1 >= 1)#True 理解为大于或者等于
print(1 <= 1)

print("abc">"123") #True 从字符串第一个开始依次比大小

print("你的年龄是")
age = input()#  age = input("你的年龄是")
if int(age) >= 18: # '>=' not supported 'str' and 'int'
    # 如果直接写age>=18，会报错，因为input()输入的是字符串，而18是整数，两者不能比较
    #int()函数可以将字符串转换为整数,前提是数字
    print("你可以看")
else:
    print("你不能看")

#逻辑运算符
#and 与
print(True and False)#False

#or 或
print(True or False)#True

#not 非
print(not (100>2))#False

#demo1:用户登录 and
name = input("请输入用户名：")
password = input("请输入密码：")
print("能登陆吗？")
print(name == "admin" and password == "123456")
#默认用户是admin，密码是123456 最后一句输出True/False

#demo2:开门
role = input("请输入角色：")
print("能开门吗？")
print(role == "admin" or role == "manager")

#demo3:判断是否是18~50之间的女性，然后，判断不在这个范围之间的人
gender = "女"
age = 18

# print("范围内的女性吗？")
# print(age>=18 and age<=50 and gender=="女")

print("范围外的人吗？")
print(not(age>=18 and age<=50 and gender=="女"))

#特殊情况
print(100 and 200)#200(最后的结果)
#C语言中，0为假，非0为真，python中，0为False，非0为True
#相当于True and True，and左右两边没有Ture和False，所以取最后一个值返回
#200不是0，所以是True

print(0 and 200)#0(and中是False就不再执行右侧)--熔断

print(100 or 200)#100--熔断(or中是True就不再执行右侧)
print(0 or 200)#200

#位运算符
#& 按位与 两个都是1才是1
print(3 & 5)#1 0011 & 0101 = 0001
#| 按位或 两个都是0才是0
print(3 | 5)#7 0011 | 0101 = 0111
#^ 按位异或 两个相同为0，不同为1
print(3 ^ 5)#6 0011 ^ 0101 = 0110
#~ 按位取反 0变1，1变0
print(~3) #-4 0000 0011 取反 = 1111 1100 = -4
#<< 左移 二进制向左移动，右边补0
print(3<<2) #12 0000 0011 << 2 = 0000 1100 = 12
#>> 右移 二进制向右移动，左边补0
print(3>>2) #0 0000 0011 >> 2 = 0000 0000 = 0

#成员运算符
#in 判断某个值是否在序列中 
print(1 in [1,2,3]) #True
print("a" in "abc") #True
#not in 判断某个值是否不在序列中
print("ac" not in "abc") #True

#身份运算符
#is 判断两个标识符是不是引用自一个对象
#is not 判断两个标识符是不是引用自不同对象
a = 1
b = 1
print(a is b) #True
