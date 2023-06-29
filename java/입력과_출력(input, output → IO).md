# 입력과 출력(input, output → IO)

> 입력과 출력을 메소드에서만 할 수 있는 것이 아니다. 입력 값을 애플리케이션에 전달하여 생동감있는 애플리케이션을 만들어보자.

------

### 경로

run → Run Configurations → arguments → Program arguments에 입력.

![io1](C:/Users/qkrxo/Downloads/io1.png)

Name에서 이름을 지정할 수 있다.

![io2](C:/Users/qkrxo/Downloads/io2.png)

Arguments에 인자를 직접 입력하면 main코드에 args의 매개변수로 전달된다.

![io3](C:/Users/qkrxo/Downloads/io3.png)

결과는 3이 된다.

------

여기서 좋은 것은 이렇게 이름을 정하고 실행했던 기록이 여기에 그대로 남아있어서 같은 입력으로 또 실행할 수 있다는 것이다. 이러면 알고리즘 문제를 풀 때 편리할 것으로 예상된다.

![io4](C:/Users/qkrxo/Downloads/io4.png)

------

## String[] args

> String[] args → 문자열[배열] 변수명

## void

> 출력값이 존재하지 않는다. return이 없다는 뜻.

------

## 사용자의 입력 받기.

> scanner 라이브러리

```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 사용자가 입력한 값을 sc에 담아 객체로 만듬.
		int i = sc.nextInt();
		System.out.println(i*1000);
		sc.close();
	}
}
```

### [System.in](http://System.in)

> 사용자가 입력한 값을 담는다.

### nextInt

> 입력할 값이 int형 이라는 것. 입력 후 엔터를 치면 i 에 입력 값이 할당된다.

### 연속으로 입력받기.

```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextInt()) { // 정수값인 동안 반복.
			System.out.println(sc.nextInt()*1000);
		}
		sc.close(); // 입력 받기 종료..
	}
}
```

### sc.hasNextInt()

> 숫자인 경우 True 숫자가 아닌 경우 False

------

## 파일 안에 있는 값 받기.

> 파일의 위치는 src와 같은 깊이의 위치이다.

```java
import java.util.Scanner;
import java.io.*;
public class Main {
	public static void main(String[] args) {
		try {
			File file = new File("out.txt"); // out.txt파일 불러옴
			Scanner sc = new Scanner(file);  // 파일을 스캔함
			while(sc.hasNextInt()) {         // 파일내용이 int형이면 실행.
				System.out.println(sc.nextInt()*1000);
			}
			sc.close();
		} catch(FileNotFoundException e) {// 예외 처리
			e.printStackTrace(); // 에러의 내용을 화면에 출력.
			
		}
	}
}
```