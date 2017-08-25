/**
 * Created by lianght on 2017/8/25.
 */

//获取省市区的信息
$(function () {
    pro = $('#pro')
    $.get('/user/areas?area_id='+$('#pro').val(), function (list) {
        $.each(list.data, function (index, item) {
            pro.append('<option value="'+item.area_id+'">'+item.title+'</option>')
        })
    })

    $('#pro').change(function () {
        $('#city').empty().append('<option value="">请选择市</option>')
        $.get('/user/areas?area_id='+$(this).val(), function (list) {
            $.each(list.data, function (index, item) {
                $('#city').append('<option value="'+item.area_id+'">'+item.title+'</option>')

            })
        })
    })

    $('#city').change(function () {
        $.get('/user/areas?area_id='+$(this).val(), function (list) {
            $('#dis').empty().append('<option value="">请选择(区)县</option>')
            $.each(list.data, function (index, item) {
                $('#dis').append('<option value="'+item.area_id+'">'+item.title+'</option>')
            })
        })
    })



})