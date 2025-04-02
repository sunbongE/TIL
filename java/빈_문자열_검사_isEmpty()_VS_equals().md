# 빈 문자열 검사 isEmpty() vs equals()


개발하다보면 사용자에게 입력받은 값이 유효한지 혹은 비었는지 확인하는 경우가 있는데 

``` java
if(string != null && "".equals(string.replaceAll(" ","")))
```

이런식으로 빈 문자열을 확인해왔다 근데 String에는 isEmpty()라는 메서드가 있고, 회사에서는 왜 이걸 사용하지 않는 것인지 의문이었다.
그래서 직접 알아보았다.

### 차이 

isEmpty()
- 문자열 길이가 0인지 확인.

equals()
- 같은 객체면 리턴 true 
- 길이가 같은 경우
	- while문으로 문자하나씩 비교하다 다르면 false
	- while문 통과(모든 문자가 같다)하면 true
- 위 과정에서 반환하지 못했다면 false 


---
상황에 따라 다르지만 단순히 입력 받은 문자열이 공백으로만 채워진 경우나 비어있는 경우를 확인할 때는 isEmpty()를 사용하는 것이 가독성도 좋아 보인다.

``` java
if(string != null && string.replaceAll(" ","").isEmpty())
```

근데 사실 replaceAll()함수와 같이 쓰니까 가독성은 두 코드 전부 좋진 않다.

그냥 공백 문자열을 확인해주는 메소드를 하나 만들어서 사용하는 것이 좋을 것 같다.

``` java
public boolean isNullOrEmpty(String input){
	if(string != null && string.replaceAll(" ","").isEmpty()) return true;
	return false;
}
```
