#if的三种写法

# if 条件：
#     代码块

# if 条件：
#     代码块
# else：
#     代码块

# if 条件1：
#     代码块1
# elif 条件2：
#     代码块2
# elif 条件3：
#     代码块3
# else：
#     代码块4

#demo1(年龄判断)
age = 17
print("---if判断开始---")
if age >= 18:
    print("你可以看")
    print("你可以写")
print("---if判断结束---")

#demo2（高富帅判断）
cool = True
money = 1000
height = 180

if cool and money >= 1000 and height >= 180:
    print("你是高富帅")

#demo3（用户登录）
name = input("请输入用户名：")
password = input("请输入密码：")

if name == "admin" and password == "123456":
    print("登陆成功")

#if else

# (Ture代表有车票，False代表没车票)
ticket = True
if ticket:   #if ticket == True:
    print("有车票，可以进站")
else:
    print("没车票，不可以进站")

#demo(身高没有超过150cm,则进动物园不用买票)
height = input("请输入身高(cm): ")
if(int(height) <= 150):
    print("可以进入")
else:
    print("不可以进入")

#没想好可以用pass
if(int(height) <= 150):
    pass
else:
    pass

#if elif

#模拟用户输入选项
user_op = input("请输入选项(ABCD):")
if user_op == "A":
    print("你选择了A")
elif user_op == "B":
    print("你选择了B")
elif user_op == "C":
    print("你选择了C")
elif user_op == "D":
    print("你选择了D")
else:
    print("你输入的选项不存在")

#demo1(判断成绩)

score = 77
if score >= 90 and score <= 100:
    print("优秀")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 70 and score < 80:
    print("中等")
elif score >= 60 and score < 70:
    print("及格")
elif score >= 0 and score < 60:
    print("不及格")
else:
    print("输入有误")

#简单写法
if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 70 <= score < 80:
    print("中等")
elif 60 <= score < 70:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("输入有误")

#demo2(判断季节)
month = input("请输入月份：")
#可以先写好month=int(month),后面更简单
#也可以不强调整形，但是数字要加引号
if 1 <= int(month) <= 3:
#or写法：if month == 1 or month == 2  or month == 3 :
    print("春天")
elif 4 <= int(month) <= 6:
    print("夏天")
elif 7 <= int(month) <= 9:
    print("秋天")
elif 10 <= int(month) <= 12:
    print("冬天")
else:
    print("输入有误")

#if嵌套

#乘车(车票＋安检)
ticket = True
knife_length = 9

if ticket:
    print("车票检查通过，准备安检")
    if knife_length <= 10:
        print("安检通过，可以进站")
    else:
        print("安检不通过，公安处理")
else:
    print("车票检查不通过，不可以进站")
#想怎么嵌套都可以

