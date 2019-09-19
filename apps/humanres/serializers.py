from rest_framework import serializers

# 部门
class GroupSerializer(serializers.Serializer):
    # 名称
    name = serializers.CharField(max_length=30,label ='名称')
    # 描述
    description = serializers.CharField(label ='描述')
    # 创建时间
    crtime = serializers.DateTimeField(label ='创建时间')
    # 修改时间
    uptime = serializers.DateTimeField(label ='修改时间')
