from django.contrib.auth.models import User
from openpyxl import load_workbook
from humanres import models

def godb():
    wb2 = load_workbook('ziliao/new讯录.xlsx')
    sheet_ranges = wb2['new']
    idnum_list=[]

    for row in sheet_ranges.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        idnum_list.append(cell_list)

    print(idnum_list)

#创建用户
    def db_create_personnel(uid,numid, nickname,phonenum,phoneoffice,groupid,classid):
        try:
            models.PersonnelModel.objects.create(uid=uid, numid=numid, nickname=nickname,phonenum=phonenum,
                                                 phoneoffice=phoneoffice,groupid=groupid,classid=classid)
        except:
            return "{}--已经存在,继续导入!".format(nickname)   # 已经创建，无法重复创建
        else:
            return "{}~~创建成功".format(nickname)  # 创建成功

    for user in idnum_list:
        try:
            uid=User.objects.get(first_name=user[2])
        except User.DoesNotExist:
            print(user[2],"用户不存在,正在创建....")
            # 用户不再User里,以手机号码来创建用户!
            uid=User.objects.create_user(username=user[3], password='88888888', is_active=True,first_name=user[2])
            print(user[2], "用户创建成功,继续导入操作!")
        finally:
            uid=User.objects.get(first_name=user[2])
            numid=uid.username
            nickname=user[2]
            phonenum=user[3]
            phoneoffice='' if user[4] is None else user[4]
            groupid=models.GroupModel.objects.get_or_create(name=user[0])[0]
            classid=models.ClassModel.objects.get_or_create(name=user[1],group=groupid)[0]
            msg=db_create_personnel(uid,numid, nickname,phonenum,phoneoffice,groupid,classid)
            print(msg)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('添加完成')
