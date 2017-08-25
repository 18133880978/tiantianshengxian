/**
 * Created by lianght on 2017/8/25.
 */

$(function () {
    var username = $('.login_info em').html()
    if (username != ''){
        $('.login_info').css({'display': 'block'})
        $('.logout').css({'display':'block'})
        $('.login_btn').css({'display': 'none'})
    }else {
        $('.logout').css({'display':'none'})
    }



})
