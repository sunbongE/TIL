# CSS

>스타일을 지정하기 위한 언어

![src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTBfODgg%2FMDAxNjUyMTYzNzU3NzQw.Jyrg5j-b9Na_rX3c4PSi69WTqw-hxRktt-RHNFYFFvEg.-7fJlmj_KR28sw4J4qxawbO4kQlqFfVh1c8fkG4gvZkg.PNG.lsh99590%2Fimage](css.assets/src=http%253A%252F%252Fblogfiles.naver.net%252FMjAyMjA1MTBfODgg%252FMDAxNjUyMTYzNzU3NzQw.Jyrg5j-b9Na_rX3c4PSi69WTqw-hxRktt-RHNFYFFvEg.-7fJlmj_KR28sw4J4qxawbO4kQlqFfVh1c8fkG4gvZkg.PNG.lsh99590%252Fimage.jpeg)



CSS구문

```html
h1 {
	color: blue; 
	font-size: 15px;
}
<!--  
h1 : 선택자
color: blue; 선언
font-size: 15px; 
속성      : 값
-->
```

- css 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 : 어떤 스타일 기능을 변경할지 결정
  - 값 : 어떻게 스타일 기능을 변경할지 결정



## CSS 정의 방법

- 인라인
- 내부 참조 - \<style>
- 외부 참조 - 분리된 CSS파일

```html
<body>
  <!-- 방법 1 -->
  <h1 style="color:blue; font-size: 100px">Hello there</h1>
    
  <!-- 방법 2 -->
  <style>
    h2 {
        color:blueviolet;
        font-size: 100px;
    }
      
</body>
```



## CSS with 개발자 도구

styles : 해당 요소에 선언된 모든 CSS

computed : 해당 요소에 최종 계산된 CSS



## CSS 기초 선택자

- 요소 선택자

  - HTML 태그를 직접 선택

- 클래스 선택자

  - 마침표 문자로 시작하며, 해당 클래스가 적용된 항목을 선택

- 아이디 선택자

  - \# 문자로 시작, 해당 아이디가 적용된 항목을 선택

  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장