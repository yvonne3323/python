#range的使用

range(x)
#从0开始,到x-1结束

range(x,y)
#从x开始,到y之前的位置结束

range(x,y,z)
#从x开始,到y之前的位置结束,但是要看z的步长

for i in range(1,6,2):
    print(i)#1,3,5

for j in range(1, 6, -1):
    print(j)#空

for k in range(6, 1, -1):
    print(k)#6,5,4,3,2


#break(结束整个循环)

i=1
while i<=5:
    break
    print(i)
    i+=1

i=1
while i<=5:
    if i==3:
        break
    print(i)
    i+=1

for i in range(1,6):
    print(i)
    break

for i in range(1,6):
    if i==3:
        break
    print(i)

#continue(结束本次循环)

i=1
while i<=5:
    print("-----")
    continue #剩下的代码不执行，死循环
    print(i)
    i+=1

i=1
while i<=5:
    print("-----")
    i+=1
    continue
    print(i)

i=1
while i<=5:
    print("---")
    i+=1
    if i==3:
        continue
    print(i)

for i in range(1,6):
    print("---")
    continue
    print(i)

for j in range(1,6):
    print("---")
    if j==3:
        continue #结束的是循环,不是单独的if语句
    print(j)


#用户登录（三次机会）


i = 1
while i <= 3:
    name = input("请输入用户名：(还剩%d次机会)" % (4-i))
    password = input("请输入密码：")
    if name == "admin" and password== "123456":
        print("登录成功")
        break
    else:
        print("登录失败")
        i += 1

i=3
while i>=1:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if name == "admin" and password=="123456":
        print("登录成功")
        break
    i-=1


i = 0
while i < 5:
    print("-----")
    i += 1
    j=0
    while j < 3:
        print("j=%d" % j)
        j += 1
      #  break #结束的是内层循环

#else

# while xxx
#     xxx
# else:
#     xxx

# for xxx
#     xxx
# else:
#     xxx

#while

#升级用户登录（三次机会）
i = 1
while i <= 3:
    name = input("请输入用户名：(还剩%d次机会)" % (4-i))
    password = input("请输入密码：")
    if name == "admin" and password=="123456":
        print("登录成功")
        break
    else:
        print("登录失败")
        i += 1
else: #当循环正常结束时,执行else
    print("输入错误次数过多，程序退出")

#升级用户登录(初阶版)
i = 0
login_flag = False #True表示登录成功,False表示登录失败
while i <= 3:
    name = input("请输入用户名：(还剩%d次机会)" % (4-i))
    password = input("请输入密码：")
    if name == "admin" and password=="123456":
        print("登录成功")
        login_flag = True
        break
    else:
        print("登录失败")
        i += 1
if login_flag == False:
    print("明日再来")


#for
for i in range(5):
    print("i=%d" % i)
    if i == 3:
        break
else:
    print("循环正常结束")

for j in range(5):
    print("j=%d" % j)
    if j == 3:
        continue #else执行
else:
    print("循环正常结束")