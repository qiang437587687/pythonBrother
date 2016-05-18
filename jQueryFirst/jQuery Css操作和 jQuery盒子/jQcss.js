/**
 * Created by zhang on 16/5/17.
 */
$(document).ready(function () {

     //$("#div").css("width","100px");
     //$("#div").css("height","100px");
     //$("#div").css("background","red");

    //设置多种颜色神马的.
    //$("#div").css({
    //    width:"100px",
    //    height:"100px",
    //    backgroundColor:"yellow"
    //});

    //js 引入 css 的 class
    $("#div").addClass("style1")

    $("#div").click(function() {

        //换一个style
        //$(this).addClass("style2")

        //移除一个style
        //$(this).removeClass("style1")

        $(this).toggleClass("style2")
    })



});