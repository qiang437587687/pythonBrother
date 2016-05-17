/**
 * Created by zhang on 16/5/10.
 */


(function () {
    var zhang = "zhang"

    function Person(name) {
        var _this = {};
        _this._name = name;
        _this.sayHello = function () {
            alert("P = = Hello" + _this._name + zhang)
        };
        return _this;
    }

    window.Person = Person;

}());


function Teacher(name) {
    var _this = Person(name);
    var superSay = _this.sayHello;
    _this.sayHello = function () {

        superSay.call(this);
        alert("t hello" + _this._name)
    };
    return _this;
}

var T = Teacher('dabao');
T.sayHello();


