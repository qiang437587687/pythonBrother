/**
 * Created by zhang on 16/5/20.
 */

$(document).ready(function (){
   $("#tabfirst li").each(function(index) {
       //value == this
       var liNode = $(this)
       liNode.mouseover(function(){
           $("div.content").removeClass("content")
           $("#tabfirst li.tabin").removeClass("tabin");
           $("div").eq(index).addClass("content");
           liNode.addClass("tabin")
       })
   });


    $("#realcontent").load("mytab.html");

    $("#tabsecond li").each(function(index){
        $(this).click(function () {

            $("#tabsecond li.tabin").removeClass("tabin");
            $(this).addClass("tabin");

            if (index == 0) {
                $("#realcontent").load("mytab.html");

            } else if(index == 1) {
                $("#realcontent").load("mytab.html");

            } else if (index == 2) {
                $("#realcontent").load("mytab.html");

            }
        })
    })
});