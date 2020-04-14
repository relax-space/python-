'''＃二级

问题6
编写一个程序，根据给定的公式计算并打印值：Q = [（2 * C * D）/ H]的平方根
以下是C和H的固定值：C为50。H为30。D是变量，其值应以逗号分隔的顺序输入到程序中。
例
让我们假设以下逗号分隔的输入序列已赋予程序：100,150,180
该程序的输出应为：18,22,24

提示：
如果收到的输出为十进制格式，则应四舍五入至最接近的值（例如，如果收到的输出为26.0，
则应将其打印为26）。
如果将输入数据提供给问题，则应先前它是控制台输入。 '''
# import math
# c = 50
# h = 30
# q = []
# item1 = [x for x in input('请输入数字:').split(',')]
# for d in item1:
#     q.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# print(','.join(q))

'''问题7

编写一个程序，该程序接受以逗号分隔的单词序列作为输入，
并在按字母顺序对单词进行排序后以逗号分隔的顺序打印这些单词。
假设将以下输入提供给程序：没有，你好，袋，世界
然后，输出应为：袋。没有，你好，世界

提示：
如果将输入数据提供给问题，则应先前它是控制台输入。'''

# list1 = [x for x in input("请输入词语：").split(',')]
# list1.sort()
# print(','.join(list1))

'''问题8
编写一个接受行序列作为输入的程序，并在将句子中的所有字符都排序之后打印行。
假设将以下输入提供给程序：
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

提示：
如果将输入数据提供给问题，则应假定它是控制台输入。'''

#这道题和上面第7题的的区别是什么，“在将句子中的所有字符都排序之后打印行”是什么意思呢

'''问题9
编写一个程序，该程序接受由空格分隔的单词序列作为输入，
并在删除所有重复的单词并将其按字母数字顺序排序后打印这些单词。
假设将以下输入提供给程序：
Hello world world Practice makes perfect
Then, the output should be:
HELLO WORLD PRACTICE MAKES PERFECT

提示：
如果将输入数据提供给问题，则应假定它是控制台输入。
我们使用set容器自动删除重复的数据，然后使用sorted（）对数据进行排序。'''

s = [x for x in  input("请输入一句话：").split()]

s.upper()
print(s)

# 这道题我不会啊

'''问题10
编写一个接受句子并计算字母和数字数量的程序。
假设将以下输入提供给程序：
你好，世界！123
然后，输出应为：
字母10
数字3
提示：
如果将输入数据提供给问题，则应先前它是控制台输入。'''

# a = input("请输入一句话：")
# b = {"letter":0,"number":0}
# for c in a:
#     if c.isalpha():
#         b["letter"] +=1
#     if c.isdigit():
#         b["number"] +=1
#     else:
#         pass
# print("字母：",b["letter"])
# print("数字：",b["number"])

'''问题11
编写一个程序，以给定的数字作为a的值来计算a + aa + aaa + aaaa的值。
假设将以下输入提供给程序：
9
然后，输出应为：
11106

提示：
如果将输入数据提供给问题，则应先前它是控制台输入。'''

# n = input("请输入一个数字：")

# n1 = int("%s"%n)
# n2 = int("%s%s"%(n,n))
# n3 = int("%s%s%s"%(n,n,n))
# n4 = int("%s%s%s%s"%(n,n,n,n))

# print(n1+n2+n3+n4)