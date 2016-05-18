/**
 * Created by zhang on 16/5/13.
 */
$(document).ready(function(){
   //$("#clickMeBtn").click(function(){
   //     alert("hello")
   //});


    // 事件的绑定 这种比上面的方法要 省内存.

    //绑定事件
    $("#clickMeBtn").bind("click",clickHandlerl1)
    //$("#clickMeBtn").bind("click",clickHandlerl2)

    //bind 方法可以替换成on方法 bind 和上面的click方法底层都是调用的on方法.
    $("#clickMeBtn").on("click",clickHandlerl2)

    //解除绑定
    //$("#clickMeBtn").unbind("click") //全部解除 click事件
    //$("#clickMeBtn").unbind("click",clickHandlerl2)

    //和上面对应的on方法的解除方法
    $("#clickMeBtn").off("click",clickHandlerl2)

    // 对应好了   bind 和 unbind    on 和off 对应
    function clickHandlerl1(e) {
        console.log("clickHander1")
    }

    function clickHandlerl2(e) {
        console.log("clickHander2")
    }

});