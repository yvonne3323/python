#自定义函数 先定义，再调用
# def 函数名():
#     代码

def print_myself():
    print("我是一个函数")
    print("我要完成一个功能")
    print("我结束了")
#定义好的函数不会自动执行，需要调用
print_myself()
print_myself() #同一个函数可以调用多次

# 输出1遍 佛祖镇楼

def print_fozuzhenlou():
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")


for i in range(3):
    print_fozuzhenlou()

#一些函数的使用(内置函数)

len("abc") #返回字符串长度
max(1,2,3) #返回最大值
del() #删除变量,或del+空格

#第三方函数

import random
random.randint(1,10) #返回1-10之间的随机整数

import time
current_time = time.time() #返回当前时间戳
print(current_time)

#函数的说明文档
def add_2_nums(num1,num2): #(形参)当函数调用的时候，用来接受数据的
    """
    作用：加法操作
    注意：纯数字
    """
    print(int(num1)+int(num2))

a= input("请输入第一个数字：")
b= input("请输入第二个数字：")
add_2_nums(a,b) #(实参)当函数调用的时候，用来传递数据的
