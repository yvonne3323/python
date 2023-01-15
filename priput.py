# Description: print
print()#输出空行
print(100,100+200)#100 300



#格式化输出
for i in range(1,3):
    print("我今年%d岁了"% i)#快速复制一行:alt + shift + ↑ or ↓

print("我是%s,今年%d岁了,我的money是%f,我的钱是%0.7f" % ("小明",18,3.14,3.14))

#转义字符
print("hello\nworld")#换行（反斜杠）
print("hello\tworld")#制表符（Tab）

#input()函数
print("请输入你的名字：")
input()#换行

input("请输入你的名字：")#不换行

password = input("请输入你的密码：")#多个数据用多个input
print("你输入的密码是：%s" % password)



