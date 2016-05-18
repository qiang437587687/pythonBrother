/**
 * Created by zhang on 16/5/13.
 */

var clickmebutton;

$(document).ready(function() {
    clickmebutton = $("#ClickMebtn");

    //先绑定一个事件
    clickmebutton.bind("MyEvent",function(event) {
        console.log(event);
    });

    //然后在添加上一个触发事件.
    clickmebutton.click(function(){
        //添加一个事件
        var e =  jQuery.Event("MyEvent");
        clickmebutton.trigger(e)
    });

});

