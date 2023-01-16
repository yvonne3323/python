#给程序传递参数
'''
import sys
#print(sys.argv)
for i in range(5):
    print("参数是：%s",%sys.argv[1])
'''

#元组
#是不可变的，不能修改，能够存储任意类型的数据

num1 = (11,22,33)
num2 = [44,55,66]

print(num1[0])

#以下代码会报错
#num1[0]=100
#del num1[0]

#集合 也是一种数据类型 set
#不重复
num3 = {77,88,99}

print(type(num1)) #元组tuple
print(type(num2)) #列表list
print(type(num3)) #集合set

num4 = {1,2,3,4,5,1,2,3,4,5}
print(num4) #会自动去重

#转换 不是对原数据进行修改，而是生成一个新的数据

print(list(num1)) #元组转换成列表
print(set(num1)) #元组转换成集合

print(list(num3)) #集合转换成列表
print(tuple(num3)) #集合转换成元组

print(tuple(num2)) #列表转换成元组
print(set(num2)) #列表转换成集合

#快速去重
num5 = [11,22,44,33,22,11,55,666,44,33,22]
num6 = set(num5) #去重，但是没有顺序
num7 = list(num6) #转换成列表
print(num7)
