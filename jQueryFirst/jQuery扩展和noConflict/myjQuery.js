/**
 * Created by zhang on 16/5/19.
 */

$.myjq = function () {
    alert("hello my jQuery")
};

//js的扩展
$.fn.myjq=function(){
    $(this).text("hello")
};