/**
 * Created by zhang on 16/5/18.
 */

$(document).ready(function(){

    $("body").text("wait.....");
    alert("hello");


    //加载box.htm文件
   $("body").load("box.htm", function(a, status, c) {
       console.log(status);
       if (status=="error") {
           $("body").text("加载失败")
       }
   });


    //加载js文件
    $.getScript("HelloJs.js").complete(function(){
       this.sayHello();
    });

});