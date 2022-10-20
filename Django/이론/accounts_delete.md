# accounts_delete

1. urls.py

   1. ```python
      path('delete/',views.delete, name='delete'),
      ```

2. views.py

   1. ```python
      def delete(request):
          request.user.delete() # 1. 요청한 사용자를 삭제한다는 것
          auth_logout(request) #  2. 로그아웃 / 순서가 바뀌면 안된다고 함 
          return redirect('accounts:index')
      
      ```

3. 끝 👍