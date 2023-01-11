//필터
function _filter(list, predi) {
    var new_list = [];
    _each(list, function (val) {
        if (predi(val)) {
            new_list.push(val)
        }
    });

    return new_list
}
//맵
function _map(list, mapper) {
    var new_li = []
    _each(list, function (val) {
        new_li.push(mapper(list[j]))
    })
    return new_li
};

// _map,_filter 함수의 중복 제거

function _each(list, iter) {
    for (var j = 0; j < list.length; j++) {
        iter(list[j])
    }
    return list;
}

//커리
function _curry(fn) {
    return function (a) {
        return arguments.length == 2 ? fn(a, b) : function (b) { return fn(a, b); };
    }
}

function _curryr(fn) {
    return function (a, b) {
        return arguments.length == 2 ? fn(a, b) : function (b) { return fn(b, a); };
    }
}

//_get 
var _get = _curryr(function (obj, key) {
    return obj == null ? undefined : obj[key];
});








