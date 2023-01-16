# 引入，快速生产1，3，5，7，9，最大值99

nums = [] #定义一个空列表,用来存储生成的数据
for i in range(100):
    if i % 2 == 1:
        nums.append(i)
print(nums)

#推导式（列表，集合，字典推导式）

#eg

nums = [i for i in range(100) if i % 2 == 1]
print(nums)

#列表推导式
#[x for x in xxxx]

#demo:生产2，4，6，8，10，最大值20

nums = [i for i in range(21) if i % 2 == 0]
print(nums)

#左边的i决定输出什么，右边的i决定循环次数
#用到if 用于过滤

#for循环嵌套
#eg:
for x in range(1,10):
    for y in range(3):
        print(x,y)

a = [(x,y) for x in range(1,10) for y in range(3)]
print(a)

#demo: [1,2,...,100]变成[[1,2,3],[4,5,6],...]

nums = [i for i in range(1,101)]
print(nums)
print(nums[0:3]) #[1,2,3]

nums2 = [nums[i:i+3] for i in range(0,len(nums),3)]
print(nums2)

#集合推导式 与列表推导式基本一致

nums = {10 for x in range(1,10)}
print(nums) #{10},特点：去重，无序

#字典推导式

#{xxx:xxx for x in range(10)}

nums3 = {x:x*3 for x in range(10)}
print(nums3)

#demo [{1:1},{2:4},{3:9},...,{10:100}]

nums4 = {x:x**2 for x in range(1,11)}

#解包

nums = [11,22,33]
a = nums[0]
b = nums[1]
c = nums[2]

#不够快捷

a,b,c = nums #数目要一致，太多意义不大
print(a,b,c)
#集合会对不上
a,b,c = {11,22,33}
print(a,b,c)

#字典解包 只会解包key，且顺序不一定

a1,b1,c1 = {'a':1,'b':2,'c':3}
print(a1,b1,c1)

#真需要对字典解包，可以用items()

test_dict = {'a':1,'b':2,'c':3}
for temp in test_dict.values(): #values()可换
    print(temp) 

test_dict = {'a':1,'b':2,'c':3}
for temp in test_dict.items(): #items 元组，可再解包
    a,b = temp
    print(a,b)

test_dict = {'a':1,'b':2,'c':3}
for k,v in test_dict.items(): #更简单的方式
    print(k)
    print(v)

#demo (交换两个变量的值)
a = 4
b = 5

#1

c=0
c=a
a=b
b=c

#2

a=a+b
b=a-b
a=a-b

#3
# 如果有要给=表达式 =11,22 可以认为是一个元组(11,22)
#a,b = (11,22) 即拆包

a,b = b,a

print("a=%d" %a)
print("b=%d" %b)





