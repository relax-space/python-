import os
import xlwt

# 读写txt文件
with open (r'\project\test2.txt','r',encoding='utf-8') as f:
    content1 = f.readlines()
    content2 = f.read()
    print(content1)
    print(content2)

with open (r'\project\test2.txt','w',encoding='utf-8') as f:
    for line in content1:
        if line in content1:
            f.write('__________。\n')
        else:
            f.write(line)

with open (r'\project\test2.txt','a',encoding='utf-8') as f:
    f.write("在文章的末尾加一行数据。\n")

# 读写Excel文件
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font
    return style 

def write_excel():
    f = xlwt.Workbook()
    sheet1 =f.add_sheet('学生',cell_overwrite_ok=True)
    row0 = ["姓名","年龄","出生日期","爱好"]
    column0 = ["张三","李四","王五","周六","小七"]
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',200,True))
    for i in range(0,len(column0)):
        sheet1.write(i+1,0,column0[i],set_style('Times New Roman',200,True))
    
    sheet1.write(1,2,"2016/12/12")
    sheet1.write(1,1,"10")
    sheet1.write_merge(2,5,2,2,'未知')
    sheet1.write_merge(3,4,3,3,'打游戏')
    sheet1.write_merge(5,5,3,3,'看书')

    f.save('test.xls')


if __name__ == '__main__':
    write_excel()