from django.contrib.auth.models import User
from openpyxl import load_workbook

def godb():
    wb2 = load_workbook('/home/huiu/mycode/qhj/devapi/ziliao/生产保障中心人员职工编号.xlsx')
    sheet_ranges = wb2['中秋节']
    idnum_list=[]

    for row in sheet_ranges.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        idnum_list.append(cell_list)

    print(idnum_list)


    def db_create_user(username,first_name, password, is_active):
        if is_active == '0':
            is_active = False
        elif is_active == '1':
            is_active = True
        try:
            User.objects.create_user(username=username, password=password, is_active=is_active,first_name=first_name,)
        except:
            return -1   # 已经创建，无法重复创建
        else:
            return 1    # 创建成功

    def add_list_user(username,first_name, password, is_active):
        createResult = db_create_user(username, first_name,password, is_active)
        if createResult == 1:
            return "{}->创建成功".format(username)
        elif createResult == -1:
            return "{}->创建失败".format(username)

    for user in idnum_list:
        add_list_user(user[1],user[0],"88888888",'1')
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