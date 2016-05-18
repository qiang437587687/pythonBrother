/**
 * Created by zhang on 16/5/17.
 */
$(document).ready( function() {
    $("#btn1").click(function(){
       $("#p1").text("杰科学院");
    });

    //直接替换
    $("#btn2").click(function(){
        $("#p2").html("<a href='http://www.handabao.com'>这是一个a标签</a>")
    });

    $("#btn3").click(function(){
        $("#i3").val("张宪强")
    });

    //$("#btn4").click(function(){
    //    $("#aid").attr("href","http://www.handabao.com")
    //})

    //如果同时修改多个属性
    $("#btn4").click(function(){
        $("#aid").attr({
            "href":"http://www.handabao.com",
            "title":"张宪强"
        })
    })

    //回调
    $("#btn5").click(function(){
        $("#p5").text(function(i, ot){
           return "old       " + ot + "   new:" + "你妹啊这也行" + (i)
        });
    })

});