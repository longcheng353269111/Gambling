# conding:utf-8

import re
# import uuid

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from user.models import User
from utils.utils import return_json_data, set_password


class EmployeeSerializer(serializers.ModelSerializer):
    account = serializers.CharField(max_length=64, help_text="工号", label='工号',
                                    validators=[UniqueValidator(queryset=User.objects.all(), message="该账户已经存在")])
    password = serializers.CharField(style={'input_type': 'password'}, max_length=64, help_text="密码", label='密码',
                                     write_only=True)

    class Meta:
        model = User
        fields = "__all__"  # 返回全部的字段
        read_only_fields = ('id', 'account')

    # def to_internal_value(self, data):
    #     """如果不重写 会把data中和数据库不相关的数据剔除掉"""
    #     return data

    # @staticmethod
    # def pre_validated(raw_data):
    #     post_id = raw_data.get('post_id')
    #     if not post_id:
    #         raise ValidationError(return_json_data("", is_fail=True, msg_text="请传入员工的岗位信息"))
    #     post = Post.objects.filter(id=post_id).first()
    #     if not post:
    #         raise ValidationError(return_json_data("", is_fail=True, msg_text="传入的岗位信息不正常"))
    #     if post.group.style != Group.Style.DEPARTMENT:
    #         raise ValidationError(return_json_data("", is_fail=True, msg_text="传入的岗位信息不正常"))

    # 校验传入数据的字段
    def validate(self, attrs: dict):
        if attrs.get('account') and len(attrs['account']) > 18:
            raise ValidationError(return_json_data("", is_fail=True, msg_text='工号长度不正确，应为0-18位'))
        if attrs.get('password'):
            pwd = attrs['password']
            if len(pwd) > 64 or len(pwd) < 6:
                raise ValidationError(return_json_data("", is_fail=True, msg_text='密码长度不正确，应为6-64位'))
            if "".join(sorted(pwd)) == pwd:
                raise ValidationError(
                    return_json_data("", is_fail=True, msg_text='密码复杂度不够，不能是按序排列的字符'))
        return attrs

    def create(self, validated_data: dict):
        validated_data['password'] = set_password(validated_data.get('password'))
        # validated_data = super().to_internal_value(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("password"):
            instance.password = set_password(validated_data.pop("password"))
        return super().update(instance, validated_data)
