function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.ajax({
        url:'/user/user/',
        type:'GET',
        dataType:'json',
        success:function (data) {
            if(data.code == 200){
                $('#user-avatar').attr('src','/static/' + data.data.avatar)
                $('#user-name').html(data.data.name);
                $('#user-mobile').html(data.data.phone);

            }
        },
        error:function (data) {
            alert('请求失败')
        }
    })
});