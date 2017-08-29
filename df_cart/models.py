from django.db import models


# Create your models here.
class CartInfo(models.Model):
    count = models.IntegerField()
    user = models.ForeignKey('df_user.User')
    goods = models.ForeignKey('df_goods.GoodsInfo')
