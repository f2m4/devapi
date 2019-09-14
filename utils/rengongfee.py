from openpyxl import load_workbook
from internalmarket import models

def godb():
    wb2 = load_workbook('ziliao/定额表.xlsx')
    sheet_ranges = wb2['3']
    xl_list=[]

    for row in sheet_ranges.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        xl_list.append(cell_list)

    print(xl_list[0])


    def db_create_go(name,workingHours, fee,remark):
        try:
            obj=models.QingGongModel.objects.create(name=name, workingHours=workingHours, fee=fee,remark=remark)
        except Exception as e:
            print("{}->失败原因".format(e))
            return "{}->创建失败".format(name)
        else:
            tag = models.TagModel.objects.get_or_create(name=remark)[0]
            obj.tag.add(tag)
            return "{}->创建成功".format(name)   # 创建成功


    for row in xl_list:
        name=row[1]
        workingHours= row[4] if row[4] is not None else ''
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