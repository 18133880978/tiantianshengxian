from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from hashlib import *
from .models import *
from . import user_decorator
import json
from df_goods.models import *
from df_cart.models import *


# Create your views here.

# 返回登陆页面
def login(request):
    username = request.COOKIES.get('username', '')
    context = {'username': username}
    return render(request, 'df_user/login.html', context)


# 登陆处理逻辑
def login_handle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        upwd = request.POST.get('pwd')

        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        remember = request.POST.get('remember', 0)
        pwd = s1.hexdigest()

        user = User.usermanager.filter(username=username)
        if len(user) == 0:
            context = {'userinfo': '用户名错误', 'username': username, 'pwd': upwd}
            return render(request, 'df_user/login.html', context)
        else:
            if pwd == user[0].passwd:
                url = request.COOKIES.get('url', '/user/info')
                red = HttpResponseRedirect(url)
                if remember != 0:
                    red.set_cookie('username', username)
                else:
                    red.set_cookie('username', '', max_age=-1)
                request.session['user_id'] = user[0].pk
                request.session['username'] = user[0].username
                return red
            else:
                context = {'pwdinfo': '密码错误', 'username': username, 'pwd': upwd}
                return render(request, 'df_user/login.html', context)
    else:
        return render(request, 'df_user/login.html')


# 返回注册页面
def register(request):
    return render(request, 'df_user/register.html')


# 判断用户名是否存在
def register_exist(request):
    username = request.GET.get('username')
    count = User.usermanager.filter(username=username).count()
    return JsonResponse({'count': count})


# 处理注册逻辑
def register_handle(request):
    s1 = sha1()
    s1.update(request.POST.get('pwd').encode('utf-8'))
    userpasswd = s1.hexdigest()

    user = User()
    user.username = request.POST.get('user_name')
    user.passwd = userpasswd
    user.email = request.POST.get('email')
    user.save()
    Dict = {'info': '注册成功'}
    # return render(request, 'user/register.html', {'Dist': json.dumps(Dict)})
    context = {'Dist': json.dumps(Dict), 'info': '注册成功,5秒后跳转到登陆页面'}

    return render(request, 'df_user/register.html', context)


# 退出登陆
def logout(request):
    request.session.flush()
    red = HttpResponseRedirect('/')
    red.set_cookie('url', '', max_age=-1)
    return red


# 返回用户个人信息页面及需要的数据
@user_decorator.login
def user_info(request):
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_ids1 = goods_ids.split(',')
    goods_list = []

    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    user = User.usermanager.get(id=request.session['user_id'])
    context = {'mobile': user.mobile, 'address': user.address, 'goods_list': goods_list}
    return render(request, 'df_user/user_center_info.html', context)


# 返回用户订单页面及需要的数据
@user_decorator.login
def user_order(request):
    return render(request, 'df_user/user_center_order.html')


# 返回用户收货地址页面及需要的数据
@user_decorator.login
def user_site(request):
    user = User.usermanager.get(id=request.session['user_id'])

    if request.method == 'POST':
        pro = request.POST.get('pro')
        city = request.POST.get('city')
        dis = request.POST.get('dis')
        print(pro)
        user.receiver = request.POST.get('receiver')
        user.address = request.POST.get('address')
        user.postcodes = request.POST.get('postcodes')
        user.mobile = request.POST.get('mobile')
        user.save()

    address_str = "%s  (%s 收)  %s" % (user.address, user.receiver, user.mobile)

    context = {'address_str': address_str, 'receiver': user.receiver, 'address': user.address,
               'postcodes': user.postcodes, 'mobile': user.mobile, 'username': user.username}
    return render(request, 'df_user/user_center_site.html', context)


# 省市区数据
def areas(request):
    area_id = request.GET.get('area_id')
    if area_id == '':
        data = Areas.objects.filter(parea_id__isnull=True)
    else:
        data = Areas.objects.filter(parea_id=area_id)

    list = []

    for area in data:
        list.append({'area_id': area.id, 'title': area.title})

    return JsonResponse({'data': list})
