# Django ModelForm

모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정됨

사용자가 입력한 값이 DB의 데이터 형식과 일치하는지를 확인하는 유효성 검증이 반드시 필요하며 이는 거버 사이드에서 반드시 처리해야함.



---

ModelForm Class

- 모델을 통해 폼 클래스를 만들 수 있는 helper class 
- 모델 폼은 폼과 같은 방식으로 뷰 함수에서 사용



----

모델 폼 선언

- forms 라이브러리의 ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

```python
from django import forms
from .models import Article

class ArticleForm(form,ModelForm):
    
    class Meta:
        # 모달폼의 정보를 작성하는 곳 
        # 모달폼을 사용할 경우 참조할 모델이 있어야함, Meta class의 모델 속성이 이를 구성함
        # 참조하는 모델에 정의된 field 정보를 Form에 적용함
        model = Article
        fields = '__all__'

```

-----

Form rendering options 

| 코드       | 내용                                                         |
| ---------- | ------------------------------------------------------------ |
| as_p()     | 각 필드가 p태그로 감싸져서 렌더링                            |
| as_ul()    | 각 필드가 li으로 감싸 렌더링 , ul태그는 따로 직접 작성해야함 |
| as_table() | tr태그로 감싸져서 렌더링                                     |

