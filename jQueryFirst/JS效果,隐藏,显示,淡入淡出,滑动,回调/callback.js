/**
 * Created by zhang on 16/5/16.
 */

$(document).ready(function() {
    //    $("#clickMeBtn").bind("click",clickHandlerl1)

    //这里都能弄错了 ??? 基础太差!!!
    $("#btn").bind("click",btnClick);

    function btnClick() {

        //重复显示
        //$("p").hide(1000, function(){
        //    $(this).show(1000, btnClick())
        //})

        //同时执行两个动作 直接在后面弄起来就行了
        $("p").css("color", "red").slideUp(1000).slideDown(1000)
    }
});