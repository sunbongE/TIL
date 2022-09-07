# Bootstrap 정리



### **input과 button**

\<input> 요소는 오직 일반 텍스트만 서버에 보낸다.

\<button> 요소는 전체 HTML 콘텐츠를 서버에 보낸다.

---



### HTTP요청

GET요청 시 사용자는 URL 을 볼 수 있지만 POST 요청 시 표시되지 않음

1. 암호를 보내야 하는 경우(민감한 데이터) 이 GET 방법을 사용하지 마십시오. 그렇지 않으면 매우 안전하지 않은 URL 표시 중에 암호가 표시될 위험이 있음
2. 많은 양의 데이터를 보내야 하는 경우 POST일부 브라우저에서는 URL의 크기를 제한하므로 이 방법을 사용하는 것이 좋습니다. 또한 많은 서버에서 허용하는 URL의 길이를 제한합니다.



## 레이아웃 breakpoint

> 부트스트랩의 장치 또는 뷰포트 크기에서 반응형 레이아웃이 작동하는 방식을 결정하는 사용자 지정 가능한 너비입니다.

**핵집개념**

- 반응형 디자인의 빌딩블록이다.
- 미디어 쿼리를 사용하여 중단점으로 CSS를 설계한다.
- 모바일 우선, 반응형 디자인이 목표다



## Grid sys

요소들의 디자인과 배치에 도움을 주는 시스템

기본요소

- Column : 실제 컨텐츠를 포함하는 부분
- Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
- container : Column들을 담고 있는 공간



###  Bootstrap grid System

Bootstrap grid System은 flexbox로 제작함

container, rows, column으로 컨텐츠를 배치하고 정렬

row : 기본 값이 12 만큼 있음

breakpoint : 6개 

![image-20220907133947909](Bootstrap%20%EC%A0%95%EB%A6%AC.assets/image-20220907133947909-16625255912531.png)

```html
<div class="container">
    <h2 class="text-center">column</h2>
    <div class="row">
        <div class="col-3 box">3칸</div>
        <div class="col-6 box">6칸</div>
        <div class="col-3 box">3칸</div>
    </div>
</div>
<-->0907연습.thml</-->
```

