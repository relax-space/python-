'''
问题18
网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。
以下是检查密码的标准：
1. [a-z]之间至少1个字母
2. [0-9]之间至少1个数字
1. [A-Z]之间至少1个字母
3. [$＃@]中的至少1个字符
4.最小交易密码长度：6
5.交易密码的最大长度：12
您的程序应接受逗号分隔的密码序列，并将根据上述条件进行检查。符合条件的密码将被打印，每个密码之间用逗号分隔。
例
如果输入以下密码作为程序输入：
ABd1234@1,a F1＃,2w3E*,2We3345,d1234@1,ABd1234@%1
然后，程序的输出应为：
ABd1234@1
ABd1234@1,a F1ABd123#,ABd123$,2We3345*,d1234@1,ABd1234@^,ABd1234@%,Ad134@?,Ad134@:,Ad134@!
提示：
如果将输入数据提供给问题，则应假定它是控制台输入。
'''

import re 
list1 = []
password1 = [x for x in input("请输入密码：").split(",")]

for p in password1:
    if not re.findall("[a-z]",p):
        continue
    elif not re.findall("[0-9]",p):
        continue
    elif not re.findall("[A-Z]",p):
        continue
    elif not re.findall("[$#@]",p):
        continue
    elif re.findall("[/%~!/:?\\|<>^/\"+-=/]",p):
        continue
    elif len(p)<6 and len(p)>12:
        continue
    else :
        pass
    list1.append(p)

print(','.join(list1))

