/**
 * Created by zhang on 16/5/13.
 */

$(document).ready(function(){
    $("body").bind("click",bodyHandler);
    $("div").bind("click",divHnadler1);
    $("div").bind("click",divHnadler2);
});


function bodyHandler(event){
    conlog(event)
}


function divHnadler1(event){
    conlog(event);
    //event.stopPropagation(); //添加一个事件阻止. 阻止父级的
    event.stopImmediatePropagation();  //阻止所有的事件
}


function divHnadler2(event){
    conlog(event);

}

// IE 可能不支持 那么生产环境可以直接注销.
function conlog(event){
    console.log(event);
}
