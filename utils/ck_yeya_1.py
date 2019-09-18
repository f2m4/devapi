from openpyxl import load_workbook
from humanres.models import GroupModel
from devs.models import WorklineModel
from spmanage.models import FactoryModel,InfoModel,TypeModel,TagModel




def godb():
    wb2 = load_workbook('ziliao/ck/轻合金液压件台帐2017.12.11.xlsx')
    sheet_ranges = wb2['液压泵台帐']
    # 生成器
    rows_iter= (row for row in sheet_ranges.rows)
    # 跳过前两行数据
    next(rows_iter)
    next(rows_iter)


    def create_obj(rowdb):
        obj_group = GroupModel.objects.get_or_create(name=rowdb[1])[0]
        obj_workline = WorklineModel.objects.get_or_create(name=rowdb[2], groupid=obj_group)[0]
        worklineid=obj_workline
        name = rowdb[3]
        typenum = rowdb[4] if rowdb[4] is not None else '未知'
        obj_factory = FactoryModel.objects.get_or_create(name=rowdb[5])[0] if rowdb[5] is not None else FactoryModel.objects.get_or_create(name="未知")[0]
        factoryid = obj_factory
        description = rowdb[6] if rowdb[6] is not None else '未知'
        typeid=TypeModel.objects.get_or_create(name='液压泵')[0]
        try:
            obj = InfoModel.objects.create(worklineid=worklineid,name=name,description=description,typenum=typenum,
                                           factoryid=factoryid,typeid=typeid)
        except Exception as e:
            print(e)
            print("{}->创建失败".format(name))  # 失败
        else:
            print("{}->创建成功".format(name))
            # 创建后添加参与者
            tagid = TagModel.objects.get_or_create(name='液压泵')[0]
            obj.tagid.add(tagid)

    i=1
    # 循环生成器
    for row in rows_iter:
        # 每行的值,组成列表
        cell_list=[i.value for i in row]
        print('开始导入第 {} 行,编号{}'.format(i,cell_list[0]))
        print(cell_list)
        i+=1
        create_obj(cell_list)
        print('导入完毕~~~~~~~~~~~~~~~~~~')

    print('任务结束')
