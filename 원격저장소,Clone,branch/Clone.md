# 원격 저장소 Clone





## Clone ? 

> 다른 사람의 원격 저장소에 있는 정보를 받아오는 것

**주의!! 원격 저장소이름의 폴더가 생성된다. 즉, 생성된 폴더에 들어가서 작업해야한다.**

---



### 사용법



```bash 
 $ git clone <url>
```

주소는 당연히 받아 올 저장소 주인 주소겠지!

---



### clone, 압축으로 다운 차이

압축으로 다운 :  최신버전의 파일/폴더 가져옴 (.git이 없음)

clone : git저장소를 가져온 것 즉, 전 버전을 볼 수 있다는 의미~!



이후에 최신화된 정보를 받아오려면 pull 사용

pull : 변경된 커밋을 받아오는 것이다. 협업할 때 작업 시작 전에는 pull하고 해야한다고 함..  



## 흐름

1.  사용자가 로컬에 저장소를 만들어 깃으로 관리하게 설정( git init)
2. 원격 저장소에 커밋!
3. 다른 사용자가` $ git clone `으로 저장소를 받아옴
4. 받아온 저장소는 이미 깃으로 관리가 되어있어 `$ git init`은 필요없다.
5. 원격 저장소에 초대된 협업자는 pull과 push 가능



## 도식화

![image-20220707193334156](Clone.assets/image-20220707193334156-16571900172701.png)
