/**
 * Created by zhang on 16/5/16.
 */

$(document).ready(function(){

    $("#flipshow").click(function(){
        $("#content").slideDown(500)
    });

    $("#fliphide").click(function(){
        $("#content").slideUp(200)
    });

    $("#fliptoggle").click(function(){
        $("#content").slideToggle(100)
    })

});