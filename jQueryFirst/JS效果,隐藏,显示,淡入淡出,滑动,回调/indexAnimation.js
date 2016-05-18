/**
 * Created by zhang on 16/5/16.
 */

$(document).ready(function() {
    var btn =  $("#hide");
    var showBtn = $("#show")
    var toggleBtn = $("#toggle")

    btn.click(function() {
       $("p").hide(1000); //1000毫秒的动画隐藏时间.
   });

    showBtn.click(function() {
        $("p").show(1000);
    });

    toggleBtn.click(function(){
        $("p").toggle(1000);
    });

});