
import datetime
import django.utils.timezone as timezone
wb2 = load_workbook('ziliao/11111.xlsx')
sheet_ranges = wb2['2018年检修工作明细']
xl_list=[]

for row in sheet_ranges.rows:
    cell_list = []
    for cell in row:
        cell_list.append(cell.value)
    xl_list.append(cell_list)

print(xl_list[0])

row=xl_list[2]
row=xl_list[98]
# 提取行的15,16列时间,并转换成日期
def col1516todatetime(row):
    time_list=[]
    col15_list=row[15].split('.')
    col16_list=row[16].split('-')
    for i in col16_list:
        li=i.split(':')
        if len(li)!=2:
            li = i.split('：')
        time_list.append(col15_list + li)
    #字符串转时间
    bg_time=timezone.datetime.strptime('-'.join(time_list[0]), "%Y-%m-%d-%H-%M")
    ed_time=timezone.datetime.strptime('-'.join(time_list[1]), "%Y-%m-%d-%H-%M")
    return bg_time,ed_time