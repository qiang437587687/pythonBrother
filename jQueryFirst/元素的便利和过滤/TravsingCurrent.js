/**
 * Created by zhang on 16/5/17.
 */

/*
* sibings()
* next()
* nextAll()
*
* */

$(document).ready(function(){

    //$("h4").siblings().css({border:"3px solid red"});
    //$("h4").next().css({border:"3px solid red"});
    //$("h4").nextAll().css({border:"3px solid red"});
    //$("p").nextUntil("h6").css({border:"3px solid red"});

    $("p").prev("h6").css({border:"3px solid red"});
    $("p").prevAll("h6").css({border:"3px solid red"});
    $("p").prevUntil("h6").css({border:"3px solid red"});


});