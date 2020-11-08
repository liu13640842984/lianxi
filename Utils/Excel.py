# coding=UTF-8
import xlrd
from Common.var import *

#获取Excel表格数据
class ReadExcel():
    def __init__(self, excelPath, sheetName=excel_sheet_name_Sheet1):
        self.excelPath = excelPath
        self.data = xlrd.open_workbook(self.excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols


    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
        try:
            return r
        except UnboundLocalError as e:
            print('ReadExcel__dict_data方法错误：%s'%(format(e)))


    @classmethod
    def get_request_data(self, **kwargs):
        request_data_dict = {}
        data = ReadExcel(file_path + '/data/data.xlsx', **kwargs)
        for dictData in data.dict_data():
            request_data_dict.update({dictData['用例编号']: {
                '打开方式': dictData['打开方式'],
                '被测网址': dictData['被测网址'],
                '输入数据': dictData['输入数据'],
                '发生事件': dictData['发生事件'],
                '实际结果': dictData['实际结果'],
                '预期结果': dictData['预期结果'],
            }})
        return request_data_dict



if __name__ == '__main__':
    excel = ReadExcel.get_request_data(sheetName=excel_sheet_name_Sheet1)
    print(excel)