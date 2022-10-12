import sys
sys.stdin = open('1240.txt')
# 문제에서 보여준 0~9까지의 암호화된 수를 딕셔너리로 입력해주고
# 입력받은 전체 배열을 거꾸로 순회하면서 최초의 1을 만났을 때 7개 씩 끊어서
# 딕셔너리의 키와 비교해서 값을 알아내고 어떤 리스트에 포함해둔다. #
dct = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

def solve():
    for st in arr: # arr 순회
        if '1' in st: # 순회하는 문자열 리스트안에 1이 있다면\
            
            e = len(st)-1 # 마지막 인덱스 값
            while st[e] == '0':
                e -= 1 # 리스트 마지막부터 앞으로 가면서 1을 찾는 코드
            # 7개씩 암호 읽어오기
            ans = []
            for i in range(e-55,e+1,7):
             # e-55: 암호코드 시작 인덱스 번호 찾음
             # e+1: 마지막 암호코드
                ans.append(dct[st[i:i+7]])
            #정상인 암호라면 값 리턴, 아니면 0
            if (sum(ans[0:8:2])*3 + sum(ans[1:8:2])) % 10 == 0:
                return (sum(ans[0:8:2]) + sum(ans[1:8:2]))
            else:
                return 0


for case in range(1,int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans=solve()
    print(f'#{case} {ans}')