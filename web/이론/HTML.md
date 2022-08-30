# HTML

> 웹 페이지를 작성(구조화)하기 위한 언어

<img src="HTML.assets/1200px-HTML5_logo_and_wordmark.svg.png" alt="1200px-HTML5_logo_and_wordmark.svg" style="zoom:25%;" />

Hyper Text Markup Language

- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트



### Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  - HTML, Markdown

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hello, HTML</title>
</head>
<body>
</body>
</html>
```

**기본 구조**

- html : 문서의 최상위 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

**head 예시**

- \<title> : 브라우저 상단 타이틀
- \<meta> : 문서 레벨 메타데이터 요소
- \<link> : 외부 리소스 연결 요소 (CSS 파일, favicon 등)

- \<script> : 스크립트 요소 (JavaScript 파일/코드)
- \<style> : CSS 직접 작성

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <title>HTML study</title>
  <meta charset="UTF-8">
  <link href="style.css" rel="stylesheet">
  <script src="javascript.js"></script>
  <style>
    p {
        color:black;
    }
  </style>
</head>
<body>
</body>
</html>
<!-- <h1>열기 태그, </h1> 닫기 태그 -->
```

**Open Graph Protocol**

- 메타 데이터를 표현하는 새로운 규약
  -  html 문서의 메타 데이터를 통해 문서의 정보를 전달 
  - 메타정보에 해당하는 제목, 성명 등을 쓸 수 있도록 정의

### 요소

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
  - 내용이 없는 태그들도 존재(닫는 태그가 없음)
    - br, hr, img, input, link, meta
- 요소는 중첩될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환하는 거이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에 디버깅이 힘들어 질 수 있음

### 속성

```html
<a href="https://google.com"></a>
<!-- href: 속성명, https://google.com : 속성값-->

```

태그별로 사용할 수 있는 속성은 다르다.

**속성 작성 방식 통일!!** : 공백X, 따옴표 쌍따옴표 사용

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성들도 있다.

**HTML Global Attribute**

모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음)

| 속성     | 기능                                                         |
| -------- | ------------------------------------------------------------ |
| id       | 문서 전체에서 유일한 고유 식별자 지정                        |
| class    | 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근) |
| data-*   | 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용        |
| style    | inline 스타일                                                |
| title    | 요소에 대한 추가 정보 지정                                   |
| tabindex | 요소의 탭 순서                                               |



**렌더링**: 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정



### DOM(Document Object Model) 트리

텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

- HTML  문서에 대한 모델을 구성
- HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

<img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA1MDZfMjI2%2FMDAxNTg4NzE2NTc1OTA0.Nzq_W58YFGeSxANUcOmMBqIVXeZBT3dHIThu2iAHQ5Mg.sv8Q2EMaIVDpbShc4J3lRlcNDuGmz-IyW9Xulur4An8g.PNG.drv98%2Fimage.png&type=sc960_832" alt="img" style="zoom: 80%;" />

## 인라인 / 블록 요소

- HTML 요소는 크게 인라인 / 블록 요소로 나움

- 인라인 요소는 글자처럼 취급
- 블록 요소는 한 줄 모두 사용



## 텍스트 요소

| 태그                                | 설명                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| \<a>\</a>                           | href 속성을 활용하려 다른 URL로 연결하는 하이퍼링크 생성     |
| \<b>\</b><br /> \<strong>\</strong> | 굵은 글씨, <br />요소 중요한 강조하고자 하는 요소(보통 굵은 글로 표현) |
| \<i>\</i><br /> \<em>\</em>         | 기울임 글씨 요소 <br />중요한 강조하고자 하는 요소 (보통 기울임 글로 표현) |
| \<br>                               | 텍스트 내에 줄 바꿈 생성                                     |
| \<img>                              | src 속성을 활용하여 이미지 표현 <br />alt 속성을 활용하여 대체 텍스트 |
| \<span>\</span>                     | 의미 없는 인라인 컨테이너                                    |



## 그룹 컨텐츠

| 태그                         | 설명                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| \<p>\</p>                    | 하나의 문단(paragraph)                                       |
| \<hr>                        | 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현된다. (A Horizontal Rule) |
| \<ol>\</ol><br />\<ul>\</ul> | 순서가 있는 리스트<br />순서가 없는 리스트                   |
| \<pre>\</pre>                | HTML에 작성한 내용을 그대로 표현.<br />보통 고정폭 글꼴이 사용되고 공백 문자를 유지 |
| \<blockquote>\</blockquote>  | 텍스트가 긴 인용문<br />주로 들여쓰기를 한 것으로 표현됨     |
| \<div>\</div>                | 의미없는 블록 래밸 컨테이너                                  |

