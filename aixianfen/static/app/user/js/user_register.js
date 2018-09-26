$(function () {


    $("#password_confirm").change(function () {

        var password = $("#password").val();
        var password_confirm = $(this).val();

        if (password == password_confirm){
            $("#password_confirm_info").html("两次一致").css("color","green");
        }else{
            $("#password_confirm_info").html("两次输入不一致").css("color","red");
        }
    });

    $("#username").change(function () {

    //
        var username = $("#username").val();
        $.getJSON("/axf/checkuser/",{"username":username},function (data) {

            console.log(data);

            if(data["status"] == "200"){
                $("#username_info").html(data["desc"]).css("color","green");
            }else if(data["status"] == "900"){
                $("#username_info").html(data["desc"]).css("color","red");
            }


        })


    })






})




}
