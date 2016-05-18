/**
 * Created by zhang on 16/5/16.
 */
$(document).ready(function(){


   // 注意 这两个的区别 html 能获取到 子标签 text 只能获取具体的内容
   //$("#btn1").click(function() {
   //    alert("text:" + $("#text").text())
   //});

    //$("#btn1").click(function() {
    //    alert("text:" + $("#text").html())
    //})

    //这个是获取 value
    //$("#btn1").click(function() {
    //    alert("text:" + $("#it").val())
    //})

    $("#btn2").click(function() {
        alert("text:" + $("#aid").attr("href") + "  id:" + $("#aid").attr("id") )
    })


});