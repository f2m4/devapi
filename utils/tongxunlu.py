from django.contrib.auth.models import User
from openpyxl import load_workbook
from humanres import models

def godb():
    wb2 = load_workbook('/home/huiu/mycode/qhj/devapi/ziliao/通讯录.xlsx')
    sheet_ranges = wb2['new']
    idnum_list=[]

    for row in sheet_ranges.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        idnum_list.append(cell_list)

    print(idnum_list)


    def db_create_personnel(uid,numid, nickname,phonenum):
        try:
            models.PersonnelModel.objects.create(uid=uid, numid=numid, nickname=nickname,phonenum=phonenum)
        except:
            return -1   # 已经创建，无法重复创建
        else:
            return 1    # 创建成功

    def add_list_personnel(uid,numid, nickname,phonenum):
        createResult = db_create_personnel(uid,numid, nickname,phonenum)
        if createResult == 1:
            return "{}->创建成功".format(nickname)
        elif createResult == -1:
            return "{}->创建失败".format(nickname)

    for user in idnum_list:
        try:
            uid=User.objects.get(first_name=user[0])
        except User.DoesNotExist:
            print(user[0])
        numid=uid.username
        nickname=user[0]
        phonenum=user[1]
        issuccess=add_list_personnel(uid,numid, nickname,phonenum)
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