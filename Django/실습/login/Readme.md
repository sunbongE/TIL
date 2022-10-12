## 목표

Django Auth를 활용한 회원관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)가 가능한 서비스를 개발합니다.

## 요구사항

### 모델 Model

- 모델 이름 : User

  Django **AbstractUser** 모델 상속

### **폼 Form**

회원가입

- Django 내장 회원가입 폼 UserCreationForm을 상속받아서 **CustomUserCreationForm** 생성

  해당 폼은 아래 필드만 출력

  - username
  - email
  - password1
  - password2

로그인

- Django 내장 로그인 폼 **AuthenticationForm** 활용

### 기능  View

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- **CustomUserCreationForm**을 활용해서 회원가입 구현

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

### 화면 Template

메인 페이지

- `GET` http://127.0.0.1:8000/
- 회원가입 페이지 이동 버튼
- 회원 목록 페이지 이동 버튼
- 로그인 상태에 따라 다른 화면 출력
  - 로그인 상태
    - 로그인 한 사용자의 username 출력
      - username 클릭 시 해당 회원 조회 페이지(프로필 페이지)로 이동
    - 로그아웃 버튼
  - 비 로그인 상태
    - 로그인 페이지 이동 버튼
    - 회원가입 페이지 이동 버튼

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 테이블
- 회원 아이디를 클릭하면 해당 회원 조회 페이지(프로필 페이지)로 이동

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼



![로그인](Readme.assets/%EB%A1%9C%EA%B7%B8%EC%9D%B8-16655638313735.gif)