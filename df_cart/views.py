from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from .models import *
from df_user import user_decorator


# Create your views here.
@user_decorator.login
def cart(request):
    user_id = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=user_id)
    context = {'page_name': 1, 'carts': carts}
    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
def add(request):
    gid = int(request.GET.get('goods_id'))
    count = int(request.GET.get('count'))
    uid = request.session['user_id']

    carts = CartInfo.objects.filter(user_id=uid).filter(goods_id=gid) #查询购物车中是否有该用户购买该商品的信息

    if len(carts) >= 1:
        cart = carts[0]
        cart.count += count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count

    cart.save()

    carts = CartInfo.objects.filter(user_id=uid)
    count = 0
    for cart in carts:
        count += cart.count

    # 如果是ajax请求，则返回该用户所有购物车中的商品总和,否则直接跳转到购物车页面 分别对应从详细列表页加入购物车和从列表页加入购物车
    if request.is_ajax():

        return JsonResponse({'count': count})
    else:
        return redirect('/cart/')


@user_decorator.login
def cart_del(request):
    cart_id = request.GET.get('cart_id')
    cart = CartInfo.objects.get(pk=cart_id)

    cart.delete()

    return JsonResponse({'status': 1})


def edit(request):
    try:
        cart_id = int(request.GET.get('cart_id'))
        count = int(request.GET.get('count'))

        cart = CartInfo.objects.get(pk=cart_id)
        cart.count = count
        cart.save()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': count}

    return JsonResponse(data)


def cart_num(request):
    uid = request.session.get('user_id', 0)
    carts = CartInfo.objects.filter(user_id=uid)
    count = 0

    for cart in carts:
        count += cart.count

    return JsonResponse({'count': count})


