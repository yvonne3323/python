#九九乘法表

#先实现矩形打印
i = 1
while i <= 9:
#    print(f"i={i}")
    j = 1
    while j <= 9:
#        print(f"{j}*{i}={j*i}", end="\t")
        print("*", end="")#end=""表示不换行
        j += 1
    print()
    i += 1

#实现三角形打印
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}", end="\t")#end="\t"表示制表符(对齐)
        j += 1
    print()
    i += 1
