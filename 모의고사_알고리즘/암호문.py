import sys
sys.stdin = open('암호문.txt','r')
# 첫 암호
# 449047 400905 139831 408347 512816 992679 693002 835918 768525 949227
#[449047, '400905', '139831', '822798', '835918', '768525', '949227', '628969', '521945', '839380', '479976']
# 처음 입력 받는 암호들을 10개만 어느 리스트에 넣어둠


for a in range(1,11):
    
    N = int(input())
    f_nums = list(map(int, input().split()))
    ten_num = f_nums # 10개만 따로 저장 이거 기준으로 업데이트 해야한다

    comm_cnt = int(input())
    comm = list(map(str, input().split('I '))) # 길이는 8인 상태 -1 해야함
    # print(ten_num[1])

    for i in range(1,len(comm)): # 0번째를 빼고 실행하면댐 -1 ㄴㄴ
        # comm[i] : 1 5 400905 139831 966064 336948 119288 이게 처음값 공백을 없애야할거임
        n_comm = list(map(str,comm[i].split())) #이제 공백을 구분으로 입력받아야함 ['1', '5', '400905', '139831', '966064', '336948', '119288']
        # print(n_comm) 
        end_num = int(n_comm[1]) # 5 int
        if int(n_comm[0]) <= 10:
            start_ =  int(n_comm[0])# 1

    for s in range(start_, end_num+1): # 1 2 3 4 \ 5 
        
        ten_num[s] = n_comm[s+1] # 1번부터 5번까지 n_comm에 있는 인댁스 2부터 5개의 숫자 
            
    print(f'{a} {ten_num}')



        # print(comm[i][j]) # 1 부터 119288이 될거임