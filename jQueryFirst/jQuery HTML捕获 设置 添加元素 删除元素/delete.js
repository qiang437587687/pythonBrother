/**
 * Created by zhang on 16/5/17.
 */


/*
* 删除的方法
* 1. remove
* 2. empty
* */

$(document).ready(function(){
    $("#btn").click(function(){
        //$("p").remove();
        //$("p").empty();

        //注意二者的区别
        //$("#div").remove() //删除子元素
        $("#div").empty()

    });
});