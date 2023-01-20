#学生管理系统
import time
import os

# 定一个列表，用来存储所有的学生信息(每个学生是一个字典)
info_list = []
#或者info_list = list()


def print_menu():# 虽然为界面，但是放在主函数的话会非常冗长
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")
#位置放置：被调用的函数一般放在调用的函数的前面

def add_new_info():
    """
    添加学生信息
    :return:
    """
    global info_list

    #获取信息
    new_name = input("请输入姓名:")
    new_tel = input("请输入手机号:")
    new_qq = input("请输入QQ:")
    #局部变量(不够)————global info_list

    for temp_info in info_list:
        if temp_info['name'] == new_name:
            print("此用户名已经被占用,请重新输入")
            return  # 如果一个函数只有return就相当于让函数结束，没有返回值
    
    #将数据添加到列表中


        #info_list.append(new_name)
        #info_list.append(new_tel)
        #info_list.append(new_qq)
        #纯粹的加入会带来问题，列表数据挤在一起，不好区分

    # 定义一个字典，用来存储用户的学生信息
    info = {} #或者info = dict()

    # 向字典中添加数据
    info["name"] = new_name
    info["tel"] = new_tel
    info["qq"] = new_qq

    # 向列表中添加这个字典
    info_list.append(info)


def del_info():
    """
    删除学生信息
    :return:
    """
    global info_list
    #获取要删除的学生的序号
    del_num = int(input("请输入要删除的序号:"))
    
    #从列表中将对应字典删除

        #del info_list[del_num] 
        # 不够完善（有误？/序号怎么知道？）

    #判断是否为纯数字
    if del_num.isdigit() == True:
        del_num = int(del_num)
    else:
        #结束函数
        return

    #判断序号是否存在
    if 0 <= del_num < len(info_list): #不是<=噢
        del_flag = input("你确定要删除么?yes or no")
        if del_flag == "yes":
            del info_list[del_num]
    else:
        print("输入序号有误,请重新输入")


def modify_info():
    """
    修改学生信息
    :return:
    """
    global info_list
    #获取要修改的学生的序号
    modify_num = int(input("请输入要修改的序号:"))
    
    #判断是否纯数字 仅仅是之前函数的一部分，不要调用
    if modify_info.isdigit() == True:
        modify_num = int(modify_num)
    else:
        return

    #修改
    if 0 <= modify_num < len(info_list):
        print("你要修改的信息是:")
        print("name:%s, tel:%s, QQ:%s" % (info_list[modify_num]['name'],
            info_list[modify_num]['tel'],info_list[modify_num]['qq']))
        info_list[modify_num]['name'] = input("请输入新的姓名:")
        info_list[modify_num]['tel'] = input("请输入新的手机号:")
        info_list[modify_num]['qq'] = input("请输入新QQ:")
    else:
        print("输入序号有误,请重新输入")


def search_info():
    """
    查询学生信息
    :return:
    """
    #获取要查询的学生的姓名
    search_name = input("请输入要查询的学生姓名:")
    #遍历列表，查询是否存在
    for temp_info in info_list:
        #temp_info是一个字典,此时['name']就是提取这个字典中的姓名
        if temp_info['name'] == search_name:
            print("查询到的信息如下:")
            print("name:%s, tel:%s, QQ:%s" % (temp_info['name'],
                temp_info['tel'], temp_info['qq']))
            break
    else:
        print("没有您要找的信息....")


def print_all_info():
    """
    遍历学生信息
    :return:
    """
    # 打印表头
    print("序号\t姓名\t\t手机号\t\tQQ")

    i = 0
    for temp in info_list:
        # temp是一个字典
        print("%d\t%s\t\t%s\t\t%s" % (i, temp['name'], temp['tel'], temp['qq']))
        # temp.get('name')也可以,可以安全查找
        i += 1


def main(): #一般为第一步，实现对程序的整体控制
    """
    用来控制整个流程
    """
    while True: #没有明确循环次数建议用while
        # 1. 打印功能
        print_menu()

        # 2. 获取用户的选择
        num = input("请输入要进行的操作(数字)")

        # 3. 根据用户选择,做相应的事情
        if num == "1":
            # 添加学生
            add_new_info()
        elif num == "2":
            # 删除学生
            del_info()
        elif num == "3":
            # 修改学生
            modify_info()
        elif num == "4":
            # 查询学生
            search_info()
        elif num == "5":
            # 遍历所有的信息
            print_all_info()
        elif num == "6":
            # 退出系统
            exit_flag = input("亲,你确定要退出么?~~~~(>_<)~~~~(yes or no) ")
            if exit_flag.low() == "yes": #low()将字符串转换为小写
                break
                #或者exit() 程序结束————break循环结束，return函数结束
        else:
            print("输入有误,请重新输入......")


        input("\n\n\n按回车键继续....")
        #os.system("clear")  # 调用Linux命令clear完成清屏
        os.system("cls")  # 调用Windows命令cls完成清屏


# 程序的开始
main()

