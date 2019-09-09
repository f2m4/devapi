from openpyxl import load_workbook
from devs import models
from humanres.models import GroupModel,ClassModel
from django.contrib.auth.models import User

def godb():
    wb2 = load_workbook('/home/huiu/mycode/qhj/devapi/ziliao/11111.xlsx')
    sheet_ranges = wb2['2018年检修工作明细']
    xl_list=[]

    for row in sheet_ranges.rows:
        cell_list = []
        for cell in row:
            cell_list.append(cell.value)
        xl_list.append(cell_list)

    print(xl_list[0])

    # 新建生产线信息
    def create_Workline(name,groupid):
        try:
            models.WorklineModel.objects.create(name=name, groupid=groupid)
        except:
            return "{}->创建失败".format(name)   # 已经创建，无法重复创建
        else:
            return "{}->创建成功".format(name)    # 创建成功

    # 创建设备信息
    def create_Devs(name,worklineid):
        try:
            models.WorklineModel.objects.create(name=name, worklineid=worklineid)
        except:
            return "{}->创建失败".format(name)   # 已经创建，无法重复创建
        else:
            return "{}->创建成功".format(name)    # 创建成功

    def create_WorkRec(classId,devName, devPart,faultDescription,repairContent,workType,faultType,spareName,
                       spareType,spareUnit,spareQuantity):
        try:
            models.WorkRecModel.objects.create(classId=classId, devName=devName, devPart=devPart,
                                               faultDescription=faultDescription,repairContent=repairContent,
                                               workType=workType,faultType=faultType,spareName=spareName,
                                               spareType=spareType,spareUnit=spareUnit,spareQuantity=spareQuantity)
        except:
            return "{}->创建失败".format(devName)   # 已经创建，无法重复创建
        else:
            return "{}->创建成功".format(devName)    # 创建成功

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
    participants_list=onedb[14].split()
    participants_list=[User.objects.get(first_name=i) for i in participants_list]
    try:
        obj_workrec=models.WorkRecModel.objects.create(classId=classId, devName=devName, devPart=devPart,
                                           faultDescription=faultDescription, repairContent=repairContent,
                                           workType=workType, faultType=faultType, spareName=spareName,
                                           spareType=spareType, spareUnit=spareUnit, spareQuantity=spareQuantity)
    except:
        print("{}->创建失败".format(devName))  # 已经创建，无法重复创建
    else:
        print("{}->创建成功".format(devName))
        obj_workrec.participants.add(*participants_list)
        # 创建成功

    # for row in xl_list:
    #     name=row[1]
    #     workingHours=row[4]
    #     fee=row[5]
    #     remark=row[6]
    #     issuccess=create_WorkRec(name,workingHours, fee,remark)
    #     print(issuccess)
    print('添加完成')
