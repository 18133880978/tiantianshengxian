from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20)
    gclick = models.IntegerField()
    gintroduce = models.CharField(max_length=200)
    gstk = models.IntegerField()
    gadv = models.BooleanField(default=False)
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo)
