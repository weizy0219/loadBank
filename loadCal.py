from openpyxl import Workbook,load_workbook
from itertools import product,chain

'''
从Excel文件中载入阻抗列表，经过计划并格式化
'''


def loadfromexcel ( excelfilename ):

    """
    从指定的Excel文件中读取所有有效行并返回所有行组成的元组
    :param excelfilename
    :return:allrows
    """
    wb=load_workbook( filename= excelfilename )
    ws=wb.active
    allrows=tuple(ws.rows) #读取所有有效单元
    return allrows


def decoderows(allrows):
    head=[cell.value for cell in allrows[0]]
    valuelist=