/**
 * Created by lianght on 2017/8/25.
 */

$(function () {
    //每次刷新页面重新去请求购物车里商品的数量
    $.get('/cart/cart_num', function (data) {
        $('.goods_count').html(data.count)
    })

    var username = $('.login_info em').html()
    if (username != ''){
        $('.login_info').css({'display': 'block'})
        $('.logout').css({'display':'block'})
        $('.login_btn').css({'display': 'none'})
    }else {
        $('.logout').css({'display':'none'})
    }



})
