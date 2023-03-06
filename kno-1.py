# 输出hello world
print("hello world")

#注释：单行注释  多行注释
"""
多行注释
"""
'''
多行注释
'''

#变量名=数值或者表达式
a=1

#数据类型：int(有符号整型) float(浮点型)
#  str set list(列表) complex(复数)
# String(字符串)...
#type()函数可以查看变量的数据类型/交互模式下直接输入变量名

#print(value,...,sep=' ',end='\n',file=sys.stdout,flush=False)
#sep:分隔符，默认空格
#end:结束符，默认换行
#file:文件对象，默认sys.stdout
#flush:刷新缓冲区，默认False

print(type(100))
print(100)
print(type("hello world"))#str
print("hello","world",sep="*",end="**")
#标识符
#1.字母、数字、下划线组成
#2.不能以数字开头
#3.区分大小写
#4.不能是关键字if等
#命名规范：小驼峰命名法myName，大驼峰FirstName，下划线send_msg
#变量名，函数名<下划线开头>，类名<大驼峰>，全局变量<大写+下划线>
import keyword
print(keyword.kwlist)#查看关键字
print(len(keyword.kwlist))#查看关键字个数



