function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

$(document).ready(function () {
    $('#form-auth').submit(function (e) {
        var real_name = $('#real-name').val();
        var id_card = $('#id-card').val();
        alert(real_name);
        $.ajax({
            url:'/user/auth/',
            type:'PATCH',
            dataType:'json',
            data:{'real_name':real_name,'id_card':id_card},
            success:function (msg) {
                if(msg.code == 200){
                    $('.btn-success').hide()
                }
            },
            error:function (msg) {
                alert('请求失败')
            }

        })
    })
});


$.get('/user/auths/', function (data) {
    if (data.data == 200){
        if(data.data.id_name){
            $('#real-name').val(data.data.id_name);
            $('#id-card').val(data.data.id_card);
            $('.btn-success').hide();
        }
    }
});