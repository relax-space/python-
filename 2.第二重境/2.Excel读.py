# coding=utf-8
import xlrd
import sys
import traceback
from datetime import datetime
from xlrd import xldate_as_tuple
from importlib import reload


   

def read_excel(filename, sheetname):
    rbook = xlrd.open_workbook(filename)
    sheet = rbook.sheet_by_name(sheetname)
    rows = sheet.nrows
    cols = sheet.ncols
    all_content = []
    for i in range(rows):
        row_content = []
        for j in range(cols):
            ctype = sheet.cell(i, j).ctype  # 表格的数据类型
            cell = sheet.cell_value(i, j)
            if (cell is None or cell == ''):
                cell = (get_merged_cells_value(sheet, i, j))
            if ctype == 2 and cell % 1 == 0:  # 如果是整形
                cell = int(cell)
            elif ctype == 3:
                # 转成datetime对象
                date = datetime(*xldate_as_tuple(cell, 0))
                cell = date.strftime('%Y/%d/%m')
            elif ctype == 4:
                cell = True if cell == 1 else False
            row_content.append(cell)
        all_content.append(row_content)
        print ('[' + ','.join("'" + str(element) + "'" for element in row_content) + ']')


    
def get_merged_cells(sheet):
    """
    获取所有的合并单元格，格式如下：
    [(4, 5, 2, 4), (5, 6, 2, 4), (1, 4, 3, 4)]
    (4, 5, 2, 4) 的含义为：行 从下标4开始，到下标5（不包含）  列 从下标2开始，到下标4（不包含），为合并单元格
    :param sheet:
    :return:
    """
    return sheet.merged_cells


def get_merged_cells_value(sheet, row_index, col_index):
    """-
    先判断给定的单元格，是否属于合并单元格；
    如果是合并单元格，就返回合并单元格的内容
    :return:
    """
    merged = get_merged_cells(sheet)
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell = sheet.cell_value(rlow, clow)
                # print('该单元格[%d,%d]属于合并单元格，值为[%s]' % (row_index, col_index, cell_value))
                ctype = sheet.cell(rlow, clow).ctype
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                return cell
                break
    return None


if __name__ == '__main__':
    filename = (r'd:\project\test1.xlsx')
    sheetname = '文件'
    read_excel(filename, sheetname)