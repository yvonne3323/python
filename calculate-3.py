#赋值运算符
age = 18 # =赋值(右边结果赋值给左边)
name,age = "小明",18 

#算术运算符
age+=1 # age = age + 1
print(age)

age-=1 # age = age - 1
print(age)

num = 4*3
print(num)
test_str = "hello"*3 #连着的
print(test_str)
print("abc" * 3)#abcabcabc

# / 除法，返回浮点数float 带有小数点
num2 = 5/2
print(num2,type(num2)) # 2.5 float

num3 = 5//2#取商 整型
print(num3,type(num3)) # 2 int

num4 = 5 % 2 #取余
print(num4,type(num4)) # 1 int

print(2**3) # 2的3次方 指数

num5 = 5
num5 *= 2 + 4# =右边是一个表达式，先计算表达式的结果，再赋值给左边
#=右边是一个表达式，相当于给这个表达式添加了()
print(num5)

#优先级顺序：**高于* / // % 高于 + - 避免歧义，加括号
#不同类型数字运算，整型会转换成浮点型

z = 0o11 #八进制 0O11
x = 0b11 #二进制 0B11
y = 0x11 #十六进制 0X11
print(z,x,y)
v = int("1001",base=4) #字符串转换成整型 将4进制的1001转换成10进制
print(v)
n = int("1001",base=0) #不对应会报错
print(n) #base 范围2-36 0
#浮点型 E/e 10的指数 后面只能跟一个整数
f = 1.23e3
print(f,type(f)) #1230.0 float
print(0.4-0.1==0.3) #False 存在误差，差值绝对值足够小判断相等