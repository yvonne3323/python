#布尔类型：True，False
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
print(1 >= 1)#True
print(1 <= 1)

print("你的年龄是")
age = input()#  age = input("你的年龄是")
if int(age) >= 18: # '>=' not supported 'str' and 'int'
    print("你可以看")
else:
    print("你不能看")

#逻辑运算符
#and
print(True and False)#False

#or
print(True or False)#True

#not
print(not (100>2))#False

#demo1:用户登录
name = input("请输入用户名：")
password = input("请输入密码：")
print("能登陆吗？")
print(name == "admin" and password == "123456")

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
print(0 and 200)#0(是False就不再执行右侧)--熔断

print(100 or 200)#100--熔断
print(0 or 200)#200

