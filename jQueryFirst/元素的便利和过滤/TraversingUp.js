/**
 * Created by zhang on 16/5/17.
 */

/*
* parent()
* parents()
* parentUntil()
* */

$(document).ready(function() {

    //$("a").parent().css({border:"3px solid red"}) //一层向上遍历

    //$("a").parents().css({border:"3px solid red"}) //这个以上的所有边框 可以添加参数 这个和向下差不多

    $("a").parentsUntil("#div1").css({border:"3px solid red"})

});