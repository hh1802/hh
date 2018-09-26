function add_cart(goods_id) {
    // $.post('/axf/addCart/?goods_id=' + goods_id, function (msg) {
    //     if(msg.code == 200){
    //         $('##num_'+ goods_id).text(msg.c_num)
    //     }else{
    //         alert(msg.msg)
    //     }
    // });
    var csrf =$('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url:'/axf/addcart/',
        type:'POST',
        dataType:'json',
        data:{'goods_id':goods_id},
        headers:{'X-CSRFToken': csrf},
        success: function (msg) {
            if(msg.code == 200){
                $('#num_'+ goods_id).text(msg.c_num)
            }else{
                alert(msg.msg)
            }
        },
        error: function (msg) {

            alert('请求失败')
        },
    })
}



function subshop(goods_id) {
    var csrf =$('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/subcart/',
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        data: {'goods_id':goods_id},
        success: function (msg) {
            if(msg.code == 200){
                $('#num_'+ goods_id).text(msg.c_num)
            }else{
                alert(msg.msg)
            }
        },
        error: function (msg){
            alert('请求失败')
        }
    })
}




function ChangeSelectStatus(cart_id) {
    // $.post('/axf/change_select_status/',function (data) {
    //     alert(data)
    //     alert(data.is_isselect)
    // })
    var csrf =$('input[name="csrfmiddlewaretoken"]').val();
    $.ajax({
        url: '/axf/change_select_status/',
        type: 'POST',
        data: {'cart_id':cart_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (data) {
           if(data.code == 200){
               if(data.is_select){
                   $('#cart_id_'+cart_id).html('√')
               }else{
                   $('#card_id' +cart_id).html('x')
               }
           }
        },
        error: function (data) {
            alert('请求失败')
        }
    })
}