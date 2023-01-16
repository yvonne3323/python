#Ctrl + Backspace 删除单词
#字符串

name1="hello"
print(name1)

name2='hello' 
#单独存储h(name2[0]/name2[-5]) e l l o(name2[4]/name2[-1])
print(name2)
print(name2[0])

name3='''hello'''
print(name3)

name4="""hello"""
print(name4)

#字符串切片

#获取文件名(后缀 .txt .mp3 .mp4)如果是.png,可以上传到网站，否则不支持

file_name = input("请输入文件名：")
if file_name.endswith(".txt"):
    print("文件名正确")
else:
    print("文件名错误")

file_name = input("请输入文件名：")
if file_name[-4:] ==".png":
    print("文件名正确")
else:
    print("文件名错误")

#demo1
name = "hello"
print(name[0:3]) #下标为3之前

namea = "abcde"
print(namea[:3]) #左边不写默认从0开始

nameb = "abcde"
print(nameb[2:]) #右边不写默认到最后

namec = "abcde"
print(namec[1:4:2]) #步长为2

named = "abcdef"
print(named[5:1:-1]) 

namee = "abcdef"
print(namee[::1]) #从一侧取到另一侧

namef = "abcdef"
print(namef[::])
#== namef[::1]
#== namef[:]

# find  顺的位置 rfind 逆的位置 返回一个
file_name = input("请输入文件名：")
find_dot_index = file_name.rfind(".")
file_houzhui = file_name[find_dot_index:]
print("测试文件后缀名：%s" % file_houzhui)
if file_houzhui == ".png":
    print("文件名正确")
else:
    print("文件名错误")
   
test_str = "my.name.is.yvonne"

print(test_str.find("."))
#3
print(test_str.rfind("."))
#11
print(test_str.count("."))
#3
print(test_str.replace(".","*"))
#替换
print(test_str.split("."))
#分割
test_str.endswith(".png")
#判断是否以.png结尾
test_str.startswith("my")
#判断是否以my开头


test_str.upper()
#转换为大写
test_str.lower()
#转换为小写

#循环用户信息，如果用户输入no，退出循环
while True:#不确定循环次数，死循环
    user_op=input("hello(yes/no)")
    if user_op.lower()== "no":
        break

my_str = "     hello world     "
print(my_str.strip())
#去掉空格
print(my_str.partition("lo"))
#分割 第一次出现的位置

you_str ="""hello 
world"""
print(you_str)
print(you_str.splitlines())
#分割成列表(去掉换行符)

print(you_str.isalpha())
#判断是否是字母(False)

print(you_str.isdigit())
#判断是否是数字

print(my_str.isalnum())
#判断是否是字母或数字

it_str ="-"
words = ["hello","world","yvonne"]
print(it_str.join(words))
#连接
