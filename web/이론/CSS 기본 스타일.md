# CSS 기본 스타일



## 크기 단위

### px 픽셀

- 모니터 해상도의 한 화소인 픽셀 기준
- 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

### %

- 백준율 단위
- 가변적인 레이아웃에서 자주 사용

### em

- (바로 위, 부모 요소에 대한) 상속의 영향을 받음
- 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

### rem

- (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
- 최상위 요소의 사이즈를 기준으로 배수 단위를 가짐



웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)

디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨 (예시- vw, vh, vmin, vmax )



## 색상 단위

**a : 투명도**

### 색상 키워드 (background-color: red)

- 대소문자 구분 X 
- red, blue, black 과 같은 특정 색을 직접 글자로 나타냄

### RGB ( background-color: rgb(0,255,0); )

- 16진 표기법이나 함수형 표기법을 사용해서 특정 색을 나타냄
  - '#' + 16진
  - rgb() 함수형 

### HSL ( background-color: hsl(0,100%,50%); )

- 색상, 채도, 명도를 통해 특정 색을 표현하는 방식



## CSS 문서 표현

**텍스트**

- 서체(font-family), 서체 스타일(font-style, font-weight 등)
- 자간(letter-spacing), 단어간격(word-spacing), 행간(line-height)

**컬러(color), 배경(background-image, background-color)**

**기타 HTML 태그별 스타일링**

- 목록, 표



## 선택자 유형

**기본 선택자**

- 전체 선택자, 요소 선택자, 클래스 선택자, 아이디 선택자, 속성 선택자

**결합자(Combinators)**

- 자손 결합자, 자식 결합자
- 일반 형제 결합자, 인접 형제 결합자

**의사 클래스/요소**

- 링크, 동적 의사 클래스
- 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자



## 선택자 정리

**요소 선택자**

- HTML 태그를 직접 선택

**클래스 선택자**

- 마침표 문자로 시작, 해당 클래스가 적용된 항목을 선택



**아이디 선택자**

- \# 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
- 일반적으로 하나의 문서에 한번만 사용
- 여러 번 사용해도 되지만 단일 id 사용을 권장함



## 적용 우선순위

1. 중요도(Importance) : 사용시 주의
   1. !importance 정해져있던 순서가 꼬일 수 있음

2. 우선 순위
   - 인라인 > id > class,속성,pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서



## 상속

CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

- 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.
- 상속이 되는 것 예시
  - TEXT 관련요소(font, color, text-align), opacity, visibility
- 상속 되지 않는 것 
  - box model 관련 요소(width,height, margin, padding, border, box-sizing, display)
  - position 관련 요소(position, top/right/bottom/left, z-index)



## Box model

모든 HTML요소는 box형으로 되어있음

하나의 박스는 네 부분으로 이루어짐

- margin - 배경색을 지정할 수 없다.

-  border - 테두리

-  padding - 요소에 적용된 배경색, 이지미는 padding 까지 적용

-  content -  글이나 이미지 

  ![box model을 구성하는 요소](https://images.velog.io/images/gil0127/post/1b3fcbde-3863-4a5c-909a-8b58e74f73ac/%EB%B0%95%EC%8A%A4%EB%A5%BC%20%EA%B5%AC%EC%84%B1%ED%95%98%EB%8A%94%20%EC%9A%94%EC%86%8C.png)

  

### box-sizing

기본적으로 모든 요소의 box-sizing은 content-box

- padding을 제외한 순수 contents 영역만들 box로 지정

영역을 볼 때 border 까지의 너비를 100px 보는 것을 원하면 box-sizing을 border-box로 설정



## display

**block**

- 줄 바꿈 O
- 화면 크기 전체의 가로 폭을 차지
- 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

요소 : div, ul, ol, li, p, hr, form 등

**inline**

- 줄 바꿈이 일어나지 않는 행의 일부 요소
- contents 너비 만큼 가로 폭을 차지
- width, height, margin-top, margin-bottom을 지정할 수 없다.
- 상하 여백은 line-height로 지정한다.

요소 : span, a, img, input, label, b, em, i, strong 등