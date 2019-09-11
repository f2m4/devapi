from openpyxl import load_workbook
from devs import models
from humanres.models import GroupModel,ClassModel
from django.contrib.auth.models import User
import pytz,datetime
from django.utils import timezone
def godb():
    wb2 = load_workbook('ziliao/11111.xlsx')
    sheet_ranges = wb2['2018年检修工作明细']
    xl_list=[]
    # 读入表格的所有行,并保存到列表
    for row in sheet_ranges.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        xl_list.append(cell_list)

    print(xl_list[0])

    # 提取行的15,16列时间,并转换成日期
    def col1516todatetime(row):
        time_list = []
        col15_list = row[15].split('.')
        col16_list = row[16].split('-')
        for i in col16_list:
            li = i.split(':')
            if len(li) != 2:
                li = i.split('：')
            time_list.append(col15_list + li)
        # 字符串转时间
        bg_time = datetime.datetime.strptime('-'.join(time_list[0]), "%Y-%m-%d-%H-%M")
        ed_time = datetime.datetime.strptime('-'.join(time_list[1]), "%Y-%m-%d-%H-%M")
        return bg_time, ed_time


    onedb=xl_list[2]
    obj_group=GroupModel.objects.get_or_create(name=onedb[2])
    obj_class=ClassModel.objects.get_or_create(name=onedb[1],group=obj_group[0])
    obj_workline=models.WorklineModel.objects.get_or_create(name=onedb[3],groupid=obj_group[0])
    obj_dev=models.DevsModel.objects.get_or_create(name=onedb[4],worklineid=obj_workline[0])
    classId=obj_class[0]
    devName=obj_dev[0]
    devPart=onedb[5]
    faultDescription=onedb[6]
    repairContent=onedb[7]
    workType=onedb[8]
    faultType=onedb[9]
    spareName=onedb[10]
    spareType=onedb[11]
    spareUnit=onedb[12]
    spareQuantity=onedb[13]
    # 添加参与者
    participants_list=onedb[14].split()
    participants_list_all=[]
    for i in participants_list:
        try:
            who=User.objects.get(first_name=i)
        except:
            print(i,'用户不存在,请联系管理员添加用户后,修改记录.')
        else:
            participants_list_all.append(who)
    bgTime,edTime=col1516todatetime(onedb)
    print(bgTime, edTime)
    bgTime=bgTime.replace(tzinfo=(pytz.timezone('Asia/Shanghai')))
    edTime=edTime.replace(tzinfo=(pytz.timezone('Asia/Shanghai')))
    print(bgTime,edTime)

    try:
        obj_workrec=models.WorkRecModel.objects.create(classId=classId, devName=devName, devPart=devPart,
                                           faultDescription=faultDescription, repairContent=repairContent,
                                           workType=workType, faultType=faultType, spareName=spareName,
                                           spareType=spareType, spareUnit=spareUnit, spareQuantity=spareQuantity,
                                                       bgTime=bgTime,edTime=edTime)
    except Exception as e:
        print(e)
        print("{}->创建失败".format(devName))  # 失败
    else:
        print("{}->创建成功".format(devName))
        # 创建后添加参与者
        obj_workrec.participants.add(*participants_list_all)

    print('任务结束')
