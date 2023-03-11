# PHP에서 사용하는 MySQL 관련 함수

| 함수명                 | 설명                                                   |
| ---------------------- | ------------------------------------------------------ |
| mysqli_connect()       | MySQL 서버에 연결한다.                                 |
| mysqli_connect_error() | MySQL 서버에 연결 오류가 발생 시에 그 원인을 알려준다. |
| mysqli_close()         | MySQL 서버에 연결된 것을 종료한다.                     |
| mysqli_select_db()     | 사용할 데이터베이스를 지정한다.                        |
| mysqli_query()         | SQL문을 서버에 실행한다.                               |
| mysqli_error()         | SQL문이 서버에서 실패한 경우 그 원인을 알려준다.       |
| mysqli_num_rows()      | SELECT문의 결과가 몇 개의 행인지 알려준다.             |
| mysqli__fetch_array()  | SELECT문의 실행 결과에서 결과 행을 추출한다.           |



# PHP 기본 프로그래밍(아주 간단히)

> 기본 틀 안에서 코드를 작성해야한다.
>
> 데이터 형식은 파이썬과 동일
>
> 

```php
<?php
    // 주석
    /*
    여러
    줄
    주석*/
    
    // 출력은 print or echo 
    /*변수는 재할당이 가능하고 타입을 따로 선언하지 않는다.
    변수 이름은 당연히 숫자로 시작못함*/
    $a = 100
    print $a // 100
    $a = 'any'
    echo $a // any
    
    ?>
```



### 조건문

```php
<?php
if (조건) {
    coding...
} elseif (조건) {
    coding...
} else {
    coding....
}

// case마다 break 필수
switch(변수){
    case 값1:
        coding,,, break;

    case 값2:
            coding,,, break;
	default:
        coding..;
?>
```



### 반복문

```php
for(초기값; 조건문; 증감식) {
    coding......
}

초기값;
while(조건식){
    coding..
    증감식
}
```



### 배열

```php
$arr = array(val1, val2, val3);

$arr= range(start,end, {plus|minus});

$arr[0]=val1;
$arr[1]=val2;
$arr[2]=val3;
```



### 내장함수

| 함수명             | 사용법                        | 설명                                                        |
| ------------------ | ----------------------------- | ----------------------------------------------------------- |
| date()             | date('Y-m-j')                 | 지정한 형식으로 날짜를 반환한다. Y-연도, m-월,  j-일,  h-시 |
| max(), min()       | max(배열이나 숫자)            | 최대, 최소 값 반환                                          |
| pi()               | pi()                          | 파이값을 반환한다.M_PI 상수와 동일하다.                     |
| round().ceil()     | round(숫자), ceil(숫자)       | 반올림, 올림                                                |
| trim()             | trim(문자열)                  | 양쪽 공백제거                                               |
| strlen()           |                               | 문자 길이 반환                                              |
| str_repeat()       | str_repeat(문자열, 횟수)      | 문자열을 횟수만큼 반복                                      |
| str_replace()      | str_replace(old, new, target) | target에서 old를 new로 바꿈                                 |
| str_split()        | str_split(문자열, 길이)       | 문자열을 길이만큼 잘라서 배열로 분리, 길이 생략하면 1임     |
| explode()          | explode(구분자,문자열)        | 문자열을 구분자로 분리해서 배열로 저장                      |
| implode()          | implode(배열, 구분자)         | 배열 중간에 구분자를 넣어서, 하나의 문자열로 이어준다.      |
| htmlspecialchars() | htmlspecialchars(HTML코드)    | HTML코드를 해석하지 않고 그냥 웹브라우저에 넘겨준다.        |

