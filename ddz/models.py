from django.db import models

from user.models import User


# Create your models here.


class Group(models.Model):
    """游戏团队，按团队进行管理"""
    name = models.CharField(max_length=64, help_text="团队名称", unique=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, help_text='团队管理者')
    diamond = models.IntegerField(default=100000, help_text='管理者钻石数，用于发放给用户使用')


class GroupMember(models.Model):
    """
    团队成员及其得分
    """
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, max_length=64, help_text="所属团队")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, help_text="团队成员")
    score = models.IntegerField()



