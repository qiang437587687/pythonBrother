/**
 * Created by zhang on 16/5/20.
 */

$(document).ready(function () {
    $(".main>a").click(function() {
        var ulNode = $(this).next("ul");
        //if(ulNode.css("display")=="none") {
        //    ulNode.css("display","block");
        //} else  {
        //    ulNode.css("display","none");
        //}

        // show hide
        //ulNode.show();
        //ulNode.toggle(400);// 数字 slow normal fast
        //ulNode.slideDown();
        //ulNode.slideUp();

        ulNode.slideToggle();
        changeIcon($(this))

    });

    $(".hmain").hover(function(){
        $(this).children("ul").slideDown();
        changeIcon($(this).children("a"));
    },function (){
       $(this).children("ul").slideUp();
        changeIcon($(this).children("a"))

    });

});

function changeIcon(mainNode) {
    if (mainNode) {
        if (mainNode.css("background-image").indexOf("IMG_1299.png")>=0) {
            mainNode.css("background-image","url('image/IMG_1277.png')");
        } else {
            mainNode.css("background-image","url('image/IMG_1299.png')");
        }
    }
}
