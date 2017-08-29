from django.shortcuts import render,render_to_response
from django.core.paginator import *
from django.http import JsonResponse
from .models import *

# Create your views here.


# 返回首页
def index(request):
    newfruit = TypeInfo.objects.get(pk='1').goodsinfo_set.order_by('-id')[0:4]
    hotfruit = TypeInfo.objects.get(pk='1').goodsinfo_set.order_by('-gclick')[0:4]

    hotseafood = TypeInfo.objects.get(pk='2').goodsinfo_set.order_by('-gclick')[0:4]
    advseafood = GoodsInfo.objects.filter(gadv='True').filter(gtype_id='2')

    username = request.session.get('username', '')

    context = {'newfruit': newfruit, 'hotfruit': hotfruit, 'hotseafood': hotseafood,
               'advseafood': advseafood, 'username': username,}

    return render(request, 'index.html', context)


def detail(request):
    username = request.session.get('username', '')
    goods_id = request.GET.get('goods_id')
    goods = GoodsInfo.objects.get(pk=goods_id)
    goods.gclick = goods.gclick + 1
    goods.save()

    other_goods = TypeInfo.objects.get(pk=goods.gtype_id).goodsinfo_set.exclude(pk=goods_id).order_by('-id')[0:4]

    context = {'goods': goods, 'other_goods': other_goods, 'username': username}

    response = render(request, 'df_goods/detail.html', context)

    goods_ids = request.COOKIES.get('goods_ids', '')

    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(goods_id) >= 1:
            goods_ids1.remove(goods_id)

        goods_ids1.insert(0, goods_id)

        if len(goods_ids1) >= 6:
            del goods_ids1[5]

        goods_ids = ','.join(goods_ids1)
    else:
        goods_ids = goods_id

    response.set_cookie('goods_ids', goods_ids)
    return response


def goods_num(request):
    num = int(request.GET.get('num'))
    type = request.GET.get('type')

    if type == 'add':
        newnum = num+1
    else:
        newnum = num-1

    return JsonResponse({'newnum': newnum})


def list(request):
    username = request.session.get('username', '')
    type_id = request.GET.get('type_id')
    sort_id = request.GET.get('sort_id')
    page_id = request.GET.get('page_id')

    typeinfo = TypeInfo.objects.get(pk=int(type_id))

    new_goods = goods = GoodsInfo.objects.filter(gtype_id=int(type_id)).order_by('-id')[0:2]
    if sort_id == "1":  # 默认排序,最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(type_id)).order_by('-id')
    elif sort_id == "2":  # 按价格排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(type_id)).order_by('-gprice')
    elif sort_id == "3":
        goods_list = GoodsInfo.objects.filter(gtype_id=int(type_id)).order_by('-gclick')

    paginator = Paginator(goods_list, 5)

    page = paginator.page(int(page_id))

    context = {'username': username,
               'new_goods': new_goods,
               'paginator': paginator,
               'page': page,
               'sort_id': sort_id,
               'typeinfo': typeinfo}
    return render(request, 'df_goods/list.html', context)



