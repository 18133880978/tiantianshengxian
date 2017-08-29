from datetime import datetime

from decimal import Decimal
from django.shortcuts import render,redirect
from df_cart.models import *
from df_user.models import *
from .models import *
from django.db import transaction

# Create your views here.


def place_order(request):
    cart_ids = request.GET.get('cart_ids').split()

    cart_list = []

    for cart_id in cart_ids:
        cart_list.append(CartInfo.objects.get(id=int(cart_id)))

    user_id = request.session['user_id']
    user = User.usermanager.get(pk=user_id)

    address_str = "%s  (%s 收)  %s" % (user.address, user.receiver, user.mobile)

    context = {'cart_list': cart_list, 'address': address_str}
    return render(request, 'df_order/place_order.html', context)


def order_handle(request):
    tran_id = transaction.savepoint()   # 创建回滚点

    cart_ids = request.POST.get('cart_ids').split()

    total = Decimal(request.POST.get('total'))

    oaddress = request.POST.get('oaddress')
    print(oaddress)

    try:
        # 创建订单对象
        order = OrderInfo()
        now = datetime.now()
        uid = request.session['user_id']
        order.oid = "%s%d" % (now.strftime('%Y%m%d%H%M%S'), uid)
        order.user_id = uid
        order.odate = now
        order.ototal = total
        order.oaddress = oaddress
        order.save()

        #创建详单对象
        for cart_id in cart_ids:
            detail = OrderDetailInfo()
            detail.order = order

            # 查询购物车信息
            cart = CartInfo.objects.get(pk=cart_id)

            # 判断库存
            goods = cart.goods
            if goods.gstk >= cart.count:
                #减少库存
                goods.gstk = cart.goods.gstk - cart.count
                goods.save()

                #完善详单信息
                detail.goods_id = goods.id
                detail.price = goods.gprice
                detail.count = cart.count
                detail.save()

                #删除购物车数据
                cart.delete()
            else:   #库存小于购买数量
                transaction.savepoint_rollback(tran_id)
                return redirect('/cart')

        transaction.savepoint_commit(tran_id)
    except BaseException as e:
        print('====================%s' %e)
        transaction.savepoint_rollback(tran_id)

    return redirect('/user/order')
