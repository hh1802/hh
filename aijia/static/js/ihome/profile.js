function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    $('#form-avatar').submit(function () {
        $(this).ajaxSubmit({
            url:'/user/profile/',
            type:'PATCH',
            dataType:'json',
            success:function (data) {
                if(data.code == 200){
                    $('#user-avatar').attr('src', '/static/' + data.image_url)
                }
            },
            error:function (data) {
                alert('请求失败')
            },
        });
        return false
    });
    $('#form-name').submit(function () {
        var nam = $('#user-name').val();
        alert(nam);
        $.ajax({
            url:'/user/proname/',
            type:'PATCH',
            dataType:'json',
            data:{'name':nam},
            success: function (msg) {
                if(msg.code == 1010){
                    $('.error-msg').html('<i class="fa fa-exclamation-circle">' + msg.msg +'</i>')
                    $('.error-msg').show()
                }
            },
            error:function () {
                alert('请求失败')
            }
        })
        return false;
    })
});
