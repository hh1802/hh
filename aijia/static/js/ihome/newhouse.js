
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');
});

$(document).ready(function () {
    $('#form-house-info').submit(function () {
        $(this).serialize();
        $.post('/house/newhouses/', $(this).serialize(), function (data) {
            alert(data)
            console.log(data)
            if (data.code == 200) {
                $('#form-house-info').hide();
                $('#form-house-image').show();
                $('#house-id').val(data.house_id)
            }
        });
        return false;

    });

});
$(document).ready(function() {
   $('#form-house-image').submit(function(){

        $(this).ajaxSubmit({
            url:'/house/house_images/',
            type:'POST',
            dataType:'json',
            success:function(msg){
                if(msg.code == '200'){
                    var img_html = '<img src="/static/' + msg.image_url + '">'
                    $('.house-image-cons').append(img_html)
                }
            },
            error:function(msg){
                alert('请求失败')
            }
        });
        return false
    });
});




