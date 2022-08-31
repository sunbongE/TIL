# CSS Position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative : 상대 위치
    - 자기 자신의 static위치를 기준으로 이동(nornal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(nomal position 대비 offset) 
  - absolute : 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(nornal flow 벗어남)
    - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)
  - fixed : 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    - 부모 요소와 관계없이 viewport 기준으로 이동
      - 스크롤 시에도 항상 같은 곳에 위치함
  - sticky : 스크롤에 따라 static 에서 fixed로 변함
    - 속성을 적용한 박스는 평소에 문서 안에서 position : static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position : fixed와 같이 박스를 화면에 고정할 수 있는 속성
    - 일반적으로 navigation bar에서 사용됨



## CSS  원칙

### 원칙 1,2 : normal flow

모든 요소는 네모, 좌측 상단에 배치

display에 따라 크기와 배치가 달라짐

### 원칙 3

- position으로 위치의 기준을 변경

  - relation : 본인의 원래 위치
  - absolute : 특정 부모의 위치
  - fixed : 화면의 위치
  - sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경

  

## Float

박스를 왼쪽, 오른쪽으로 이동시켜 텍스트를 포함 inline 요소들이 주변을 wrapping 하도록 함

요소가 Normal flow를 벗어나도록 함 

```css
.이름짓기 {
    float:left;
}
```



## Flexbox

행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

축: 메인 축(main axis), 교차 축(cross axis)

**구성 요소** 

- Flex Container(부모 요소)
  - flexbox 레이아웃을 형성하는 가장 기본 모델
  - flex item 들이 놓여있는 영역
  - display 속성을 flex or  inline-flex로 지정

- Flex Item(자식 요소)
  - 컨테이너에 속해 있는 컨텐츠(박스)



## Flex 속성

**배치 설정**

- flex-direction
  - 메인 축 방향을 설정
- flex-wrap
  - 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
    - nowrap (기본 값) - 한 줄 배치
    - wrap - 크기 넘치면 다음 줄에 배치



**공간 나누기**

- justify-content (main axis)
- align-content (cross axis)



**정렬**

- align-items (모든 아이템을 교차 축 기준 정렬)
- align-self (개별 아이템)