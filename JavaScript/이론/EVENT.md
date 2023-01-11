# EVENT

> 역할 : ~하면 ~한다.

특정 이벤트가 발생하면 함수를 등록한다.

----

개념: 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

이벤트 발생

- 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
- 특정 메서드를 호출(Element.click()) 하여 프로그래밍적으로도 만들어 낼 수 있음

----

**EventTarget.addEventListener(type, listener[,options])**

- 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 성정
- 이벤트를 지원하는 모든 객체(Element, Document, Window)를 대상으로 지정 가능

- type : 반응 할 이벤트 유형 (대 소문 구분 문자열)
- listener : 지정된 타입의 이벤트가 발생할 때 알림을 받는 객체, EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함

----

## Event 취소

event.preventDefault() : 현재 이벤트의 기본 동작을 중단

HTML 요소의 기본 동작을 작동하지 않게 막음

이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

(취소할 수 없는 이벤트도 존재함. event.cancleable 으로 확인 가능)