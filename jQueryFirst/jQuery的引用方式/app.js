/**
 * Created by zhang on 16/5/13.
 */


$(document).ready(function() {
    //alert("加载完成了会显示执行这个函数")

    //$("p").click(function() {
    //    $(this).hide();
    //})

    //  我并不知道为什么这个还是不行!!! 答案 jquery 里面貌似是用text 属性来修改的.

    $("p").click(function () {
        // $(this).text = "韩大宝是猪"
        //是这个样子的!!!! 并不是等于号啊
        $(this).text("韩大宝是猪");

    })

});




