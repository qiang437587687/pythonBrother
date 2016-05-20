/**
 * Created by zhang on 16/5/19.
 */
$(document).ready(function(){
   $(window).on("load",function(){
       imageLocation();
       //监听滚动
       var dataImg = {
           "data":[{"src":"1.jpg"},{"src":"2.jpg"},{"src":"3.jpg"},{"src":"4.jpg"},{"src":"5.jpg"},{"src":"6.jpg"}]
       };

       window.onscroll = function (){
            if (scrollside()) {
                $.each(dataImg.data, function(index,value){
                    var box = $('<div>').addClass("box").appendTo($("#container"))
                    var content = $('<div>').addClass("content").appendTo($(box))
                    $("<img>").attr("src","./img/"+$(value).attr("src")).appendTo(content);
                });
                imageLocation();
            }
       }
   })
});

function scrollside(){
    var box = $(".box")

    //get(0) 这个是通过jQuery的对象获得可以操作的 DOM对象
    var lastboxHeight = box.last().get(0).offsetTop + Math.floor(box.last().height()/2);
    console.log(box.last().offsetTop)
    var doucmentWidth = $(document).width();
    var scrollHeight = $(window).scrollTop();
    return (lastboxHeight<scrollHeight+doucmentWidth)?true:false;
}

function imageLocation(){

    var box = $(".box");
    var boxWidth = box.eq(0).width();
    var num = Math.floor($(window).width()/boxWidth);
    var boxArr = [];

    box.each(function(index, value) {
      //console.log(index+"---"+value)
        var boxHeight = box.eq(index).height();
        if(index<num) {
            boxArr[index] = boxHeight;
        } else {
            var minboxHeight = Math.min.apply(null,boxArr);
            var minboxIndex = $.inArray(minboxHeight,boxArr);
            $(value).css({
                "position":"absolute",
                "top":minboxHeight,
                "left":box.eq(minboxIndex).position().left
            });

            boxArr[minboxIndex]+=box.eq(index).height();
        }
    });

}