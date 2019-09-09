from openpyxl import load_workbook
from internalmarket import models

def godb():
    wb2 = load_workbook('/home/huiu/mycode/qhj/devapi/ziliao/定额表.xlsx')
    sheet_ranges = wb2['1']
    xl_list=[]

    for row in sheet_ranges.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        xl_list.append(cell_list)

    print(xl_list[0])


    def db_create_go(name,workingHours, fee,remark):
        try:
            models.QingGongModel.objects.create(name=name, workingHours=workingHours, fee=fee,remark=remark)
        except:
            return "{}->创建失败".format(name)   # 已经创建，无法重复创建
        else:
            return "{}->创建成功".format(name)    # 创建成功


    for row in xl_list:
        name=row[1]
        workingHours=row[4]
        fee=row[5]
        remark=row[6]
        issuccess=db_create_go(name,workingHours, fee,remark)
        print(issuccess)
    print('添加完成')
# from openpyxl import Workbook
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()
# ws.append([1, 2, 3])
# # Save the file
# wb.save("sample.xlsx")