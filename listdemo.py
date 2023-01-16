#一个学校，3个办公室，8位老师随机分配到办公室

#1：一个列表，嵌套3个空列表
#2：另一个列表，8位老师
#3：

import random
offices = [[],[],[]]
teacher_names = ["A","B","C","D","E","F","G","H"]
#遍历
for name in teacher_names:
    #随机分配
    index = random.randint(0,2)
    #将老师分配到办公室
    offices[index].append(name)

#print(offices)

#遍历所有办公室的所有人
i=1
for temp in offices:
    print("%d号办公室,有%d人" % (i,len(temp)))
    for name in temp:
        print(name)
    i+=1