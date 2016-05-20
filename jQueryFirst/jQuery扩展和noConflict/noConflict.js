/**
 * Created by zhang on 16/5/19.
 */

var mjQ =  $.noConflict(); //消除 $对jQuery的缩写

//mjQ 也可以用来代替这里面的 jQuery
jQuery(document).ready(function () {
    jQuery("#btn").on("click",  function(){
        jQuery("div").text("new hello")
    })
});

//$(document).ready(function () {
//    $("#btn").on("click",  function(){
//        $("div").text("new hello")
//    })
//});