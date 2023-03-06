
for i in range(10):
    print("hello")


nums = [11, 22, 33, 44, 55, 66, 77, 88, 99]
#依次取出

#while(人为控制循环次数)
i=0
while i <= 8:
    print(nums[i])
    i += 1

# for(对于对象一次性)
for i in nums:
    print(i)



#for 格式
# for 变量 in 对象:
#     代码

for i in range(3):
    print("i") # 0 1 2



#计算1-100的和

sum = 0
for i in range(101):
#    print("i = %d" % i)
    sum += i
print("sum = %d" % sum)

