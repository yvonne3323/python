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
test_str = "hello"*3
print(test_str)
print("abc" * 3)

num2 = 5/2
print(num2,type(num2)) # 2.5 float

num3 = 5//2#取商
print(num3,type(num3)) # 2 int

num4 = 5 % 2 #取余
print(num4,type(num4)) # 1 int

print(2**3) # 2的3次方

num5 = 5
num5 *= 2 + 4# =右边是一个表达式，先计算表达式的结果，再赋值给左边
print(num5)
