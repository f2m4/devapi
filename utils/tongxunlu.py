from django.contrib.auth.models import User
from openpyxl import load_workbook
from humanres import models

def godb():
    wb2 = load_workbook('ziliao/new讯录.xlsx')
    sheet_ranges = wb2['new']
    rows_iter= (row for row in sheet_ranges.rows)

#创建用户
    def db_create_personnel(uid,numid, nickname,phonenum,phoneoffice,groupid,classid):
        try:
            models.PersonnelModel.objects.create(uid=uid, numid=numid, nickname=nickname,phonenum=phonenum,
                                                 phoneoffice=phoneoffice,groupid=groupid,classid=classid)
        except:
            return "{}--已经存在,继续导入!".format(nickname)   # 已经创建，无法重复创建
        else:
            return "{}~~创建成功".format(nickname)  # 创建成功

    i = 1
    for row in rows_iter:
        cell_list = [i.value for i in row]
        print('开始导入第 {} 行,编号{}'.format(i, cell_list[0]))
        i += 1
        print(cell_list)
        if cell_list[0] is None:
            print('!!!!!!!!!!!!!!!!!!!跳过此行!!!!!!!!!')
            i += 1
            continue

        try:
            uid=User.objects.get(first_name=cell_list[2])
        except User.DoesNotExist:
            print(cell_list[2],"用户不存在,正在创建....")
            # 用户不再User里,以手机号码来创建用户!
            uid=User.objects.create_user(username=cell_list[3], password='88888888', is_active=True,first_name=cell_list[2])
            print(cell_list[2], "用户创建成功,继续导入操作!")
        finally:
            uid=User.objects.get(first_name=cell_list[2])
            numid=uid.username
            nickname=cell_list[2]
            phonenum=cell_list[3]
            phoneoffice='' if cell_list[4] is None else cell_list[4]
            groupid=models.GroupModel.objects.get_or_create(name=cell_list[0])[0]
            classid=models.ClassModel.objects.get_or_create(name=cell_list[1],group=groupid)[0]
            msg=db_create_personnel(uid,numid, nickname,phonenum,phoneoffice,groupid,classid)
            print(msg)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('添加完成')
