#石头剪刀布

#我的代码

hand = input("请输入：剪刀(0) 石头(1) 布(2):")
if hand == "0":
    print("输了，不要走，洗洗手接着来，决战到天亮")
elif hand == "1":
    print("平局，要不再来一盘")
elif hand == "2":
    print("获胜，哈哈，你太厉害了")
else:
    print("输入有误")

#老师代码
import random
player = int(input("请输入：剪刀(0) 石头(1) 布(2):"))
computer = random.randint(0,2)

if(player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("获胜，哈哈，你太厉害了")
elif player == computer:
    print("平局，要不再来一盘")
else:
    print("输了，不要走，洗洗手接着来，决战到天亮")