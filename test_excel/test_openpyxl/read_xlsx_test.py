# coding=utf-8

"""
读取excel测试
"""
from openpyxl import load_workbook

file_path = 'D:\\工作\\联系人.xlsx'


# 测试读取excel文件的方法
def test_read_excel():
    # 打开excel文件
    wb = load_workbook(file_path)
    # 获取工作表
    sheet = wb.active
    a_columns =  sheet['1']
    for a in a_columns:
        print(a.value)
    for b in range(ord('A'),ord('M')):
        sheet[chr(b)+'7'].value = '岳庆'
    wb.save('D:\\工作\\联系人.xlsx')


test_read_excel()