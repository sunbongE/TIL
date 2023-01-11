# 함수형 프로그래밍

애플리케이션, 함수의 구성 요소, 더 나아가서 언어 자체를 함수처럼 여기도록 만들고 

이러한 함수 개념을 가장 우선순위로 한다.



순수 함수로 만드는 것이 다형성면에서 좋다.

메서드를 순수 함수로 만들면 그 틀에 맞는 값만 넣어도 작동을 하기 때문에 다형성 면에서 더 좋다는 것 같음.(메서드는 리스트형만 사용 가능한 메서드 등이 있지만 순수 함수는 입력이 틀에 맞기만 하다면 실행이 되니까......)





### 순수 함수

- **부수 효과가 없는 함수** 즉, 어떤 함수에 동일한 인자를 주었을 때 항상 같은 값을 리턴하고 외부의 상태를 변경하지 않는 함수

부수 효과란?

외부 상태를 변경하는 것 또는 함수로 들어온 인자의 상태를 직접 변경하는 것



### 일급 함수

특징

- 변수에 함수가 담길 수 있다.
- 함수는 Object 유형의 인스턴스이다.
- 함수를 다른 함수에 매개변수로 전달 가능
- 함수에서 함수가 반환될 수 있다.
- List, Hash Table 같은 데이터 구조에 저장할 수 있다.





## 커링

함수를 실행하면 바로 다른 함수를 리턴하여 실행하는 함수..

```javascript
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


var add = _curry(function (a, b) {
    return a + b;
});
var add10 = add(10); 

console.log(add10(4)) // 14
console.log(add(5)(3)) // 8
```



## reduce 만들기

[1,2,3,4] 이 리스트 안에 숫자들을 모두 더한 값을 나타내는 함수.



```javascript
// _reduce 만들기
        var slice = Array.prototype.slice;
        function _rest(list, num) {
            return slice.call(list, num || 1);
        }
        function _reduce(list, iter, memo) {
            if (arguments.length == 2) { // memo를 입력 안했을 때
                memo = list[0];
                list = _rest(list);
            }
            _each(list, function (val) {
                memo = iter(memo, val);
            });
            return memo;
        }
        //동작
        // momo = add(0,1);
        // momo = add(memo,2);
        // momo = add(memo,3);
        // return memo
        console.log(_reduce([1, 2, 3, 4], add, 0));
        console.log(_reduce([1, 2, 3], add));
```

