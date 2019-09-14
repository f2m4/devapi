from openpyxl import load_workbook
from humanres.models import GroupModel
from devs.models import WorklineModel
from spmanage.models import FactoryModel,InfoModel,TypeModel,TagModel




def godb():
    wb2 = load_workbook('ziliao/ck/轻合金液压件台帐2017.12.11.xlsx')
    sheet_ranges = wb2['滤芯台帐']
    rows_iter= (row for row in sheet_ranges.rows)
    next(rows_iter)


    def create_obj(rowdb):
        obj_group = GroupModel.objects.get_or_create(name=rowdb[0])[0]
        obj_workline = WorklineModel.objects.get_or_create(name=rowdb[1], groupid=obj_group)[0]
        worklineid=obj_workline
        name = rowdb[2]
        typenum_1 = rowdb[3] if rowdb[3] is not None else '未知'
        typenum_2 = rowdb[4] if rowdb[4] is not None else '未知'
        typenum ="过滤器:{}||滤芯:{}".format(typenum_1,typenum_2)
        obj_factory = FactoryModel.objects.get_or_create(name=rowdb[5])[0] if rowdb[5] is not None else FactoryModel.objects.get_or_create(name="未知")[0]
        factoryid = obj_factory
        description =rowdb[4] if rowdb[4] is not None else '未知'
        typeid=TypeModel.objects.get_or_create(name='滤芯')[0]
        try:
            obj = InfoModel.objects.create(worklineid=worklineid,name=name,description=description,typenum=typenum,
                                           factoryid=factoryid,typeid=typeid)
        except Exception as e:
            print(e)
            print("{}->创建失败".format(name))  # 失败
        else:
            print("{}->创建成功".format(name))
            # 创建后添加参与者
            tagid_1 = TagModel.objects.get_or_create(name='滤芯')[0]
            tagid_2 = TagModel.objects.get_or_create(name='过滤器')[0]
            obj.tagid.add(*[tagid_1,tagid_2])

    i=2
    for row in rows_iter:
        cell_list=[i.value for i in row]
        print('开始导入第 {} 行,编号{}'.format(i,cell_list[0]))
        print(cell_list)
        if cell_list[2] is None:
            print('!!!!!!!!!!!!!!!!!!!跳过此行!!!!!!!!!')
            i+=1
            continue
        i+=1
        create_obj(cell_list)
        print('导入完毕~~~~~~~~~~~~~~~~~~')

    print('任务结束')
