/**
 * Created by zhang on 16/5/10.
 */

//var person={
//    name : "zhang",
//    age : 25,
//    eat : function() {
//        alert("有点胖")
//    }
//}
//alert(person.name)



function Person() {

}
//通过这货来添加 属性和方法
Person.prototype = {
    name: 'zhangxianqiang',
    age : 25,
    eat: function(){
        alert("我在这里")
    }
}

var P = new Person()
alert(P.name)
P.eat()





