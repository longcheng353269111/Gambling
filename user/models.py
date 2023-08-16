from django.db import models

"""
# 后期考虑通过微信授权登陆
"""


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64, help_text='昵称')
    account = models.CharField(unique=True, max_length=64, help_text='账号')
    password = models.CharField(max_length=64, help_text='密码')
    role = models.SmallIntegerField(default=1, help_text='用户角色，目前默认为，后续再定义')
