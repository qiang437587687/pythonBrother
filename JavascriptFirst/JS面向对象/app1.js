/**
 * Created by zhang on 16/5/10.
 */



//数据的封装
(function() {

    var  n = "xianqiang" //这个外部是不能引用的

    //函数当做类使用
    function People(name) {
        this._name = name;
    }

//添加方法
    People.prototype.say = function() {
        alert("p-hello" + this._name)
    };

    window.People = People;

}()); // 这个地方执行了!!!



(function(){

    //就是这么来继承的 这只是其中一个方法
    function Student(name) {
        this._name = name;
    }

// 这个地方原来写成了 Student() 这是不能用括号的. 然而还没有提示 (ˉ▽￣～) 切~~
    Student.prototype = new People();
    var superSay = Student.prototype.say;

    Student.prototype.say = function() { //重写方法

        superSay.call(this)
        alert("stu-hello" + this._name)

    };
    window.Student = Student;


}());


var s = new Student('zhangxianqiang');
//var p = new People('handabao')
s.say();




























































