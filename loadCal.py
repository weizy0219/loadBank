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

def writetoexcel( excelfilename ):
    """
    将文件写入excel表格中
    :param excelfilename:
    :return:
    """

def decoderows(allrows):
    """
    从读取到的excel二维列表中解析出阻抗值列表
    :param allrows:
    :return rowhead,rowcontent:
    """
    colname=[cell.value for cell in allrows[0][1:]]
    rowhead=[]
    rowcontent=[]
    for onerow in allrows[1:]:
       rowhead.append(onerow[0])
       rowcontent.append(onerow[1:])
    return rowhead,rowcontent

