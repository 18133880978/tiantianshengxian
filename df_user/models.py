from django.db import models

# Create your models here.
from django.db import models


class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(isDelete=False)    # 过滤原始查询集中被逻辑删除的数据


class User(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    receiver = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    postcodes = models.CharField(max_length=6, default='')
    mobile = models.CharField(max_length=11, default='')
    isDelete = models.BooleanField(default=False)
    usermanager = UserManager()

    class Meta:
        db_table = 'user'


class Areas(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', null=True, blank=True)

    class Meta:
        db_table = 'areas'