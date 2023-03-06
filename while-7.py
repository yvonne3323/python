i = 1
while i <= 10:
    print("hello")
    i += 1

# while 格式
# while 条件:
#     要重复执行的代码1
#     要重复执行的代码2
#     ...

i = 1
while i <= 10:
    # print("i=%d" % i)  # 若无下一行死循环
    i += 1  # 若与前一行互换则输出不同
    print(f"i={i}")#更高级的格式
j = 10
while j >= 1:
    print("j=%d" % j)
    j -= 1

# 计算1-100之间所有数字的累计求和结果

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("1-100之间所有数字的累计求和结果为: %d" % sum)

# 计算1-100之间所有偶数的累计求和结果
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print("1-100之间所有偶数的累计求和结果为: %d" % sum)

# 计算1~100之间能被3整除且被7整除的数字的累计求和结果
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0 and i % 7 == 0:
        sum += i
    i += 1
print("1~100之间能被3整除且被7整除的数字的累计求和结果为: %d" % sum)

# 1--->1
# 2--->4
# 3--->9

i = 1
while i <= 3:
    print("%d--->%d" % (i, i**2))
    i += 1

#while循环的嵌套(减少重复代码)
i = 1
while i <= 3:
    print("hh")
    j = 1
    while j <= 3:
        print("hello")
        j += 1
    i += 1