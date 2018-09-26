function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){
    var mySwiper = new Swiper ('.swiper-container', {
        loop: true,
        autoplay: 2000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',
        paginationType: 'fraction'
    })
    $(".book-house").show();
});
alert(location.search)
var id =location.search.split('=')[1]
$.get('/house/details/' + id +'/', function (msg) {
    if(msg.code == 200){
        $('.house-title').html(msg.house_info.title)
        $('.landlord-name').html('用户名' + msg.house_info.user_name)
        $('.text-center').html(msg.house_info.address)
        $('.room').html('出租'+msg.house_info.room_count+'间')
        $('.area').html('房屋面积:'+msg.house_info.acreage +'平米')
        $('.unit').html('房屋户型:'+msg.house_info.unit)

        $('.book-house').attr('href', '/house/booking/?house_id=' +msg.house_info.id )
    }
})
