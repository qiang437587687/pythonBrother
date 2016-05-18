/**
 * Created by zhang on 16/5/17.
 */
/*
*  append 后面加
*  ppend 前面添加
* */

$(document).ready(function(){
    $("#btn1").click(function(){
        //$("#p1").append("加油张宪强")
        $("#p1").prepend("加油张宪强")
    });

    $("#btn2").click(function(){
        //这个和上面的比较起来是换行添加了
        $("#p2").before("handabao");
        $("#p2").before("handabao");
    })
});

function appendText() {

    var text1 = "<p>张宪强</p>";
    var text2 = $("<p></p>").text("韩大宝");
    var text3 = document.createElement("p");
    text3.innerHTML = "熊宝";

    $("body").append(text1,text2,text3)
}






