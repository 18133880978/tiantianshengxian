from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from df_user.models import *

# Create your views here.


# 返回首页
def index(request):
    newfruit = TypeInfo.objects.get(pk='1').goodsinfo_set.order_by('-id')[0:4]
    hotfruit = TypeInfo.objects.get(pk='1').goodsinfo_set.order_by('-gclick')[0:4]

    hotseafood = TypeInfo.objects.get(pk='2').goodsinfo_set.order_by('-gclick')[0:4]
    advseafood = GoodsInfo.objects.filter(gadv='True').filter(gtype_id='2')

    context = {'newfruit': newfruit, 'hotfruit': hotfruit, 'hotseafood': hotseafood,
               'advseafood': advseafood}

    return render(request, 'index.html', context)


def detail(request):
    goods_id = request.GET.get('goods_id')
    goods = GoodsInfo.objects.get(pk=goods_id)
    other_goods = TypeInfo.objects.get(pk=goods.gtype_id).goodsinfo_set.exclude(pk=goods_id).order_by('-id')[0:4]
    context = {'goods': goods, 'other_goods': other_goods}
    return render(request, 'df_goods/detail.html', context)


def goods_num(request):
    num = int(request.GET.get('num'))
    type = request.GET.get('type')

    if type == 'add':
        newnum = num+1
    else:
        newnum = num-1

    return JsonResponse({'newnum': newnum})



