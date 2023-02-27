# Description: print
print()#输出空行

#用法一：将要显示的数据直接放入小括号中
#用法二：可以将一个表达式放入小括号中，它会先计算结果，然后将结果显示出来
#用法三：可以在小括号中写多个逗号
print(100,100+200)#100 300
print(100,    200)#100 200 逗号起到空格的作用



#格式化输出
for i in range(1,3):
    print("我今年%d岁了"% i)#快速复制一行:alt + shift + ↑ or ↓

print("我是%s,今年%d岁了,我的money是%f,我的钱是%.7f" % ("小明",18,3.14,3.14))
#%f 6位小数 %.7f 7位小数

#转义字符
print("hello\nworld")#换行（反斜杠）
print("hello\tworld")#制表符（Tab）

#input()函数 字符串str
print("请输入你的名字：")
input()#换行,即输入的名字在下一行显示

#优化
input("请输入你的名字：")#不换行

password = input("请输入你的密码：")#多个数据用多个input
print("你输入的密码是：%s" % password)



