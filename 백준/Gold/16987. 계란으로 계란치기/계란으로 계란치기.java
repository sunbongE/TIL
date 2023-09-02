import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호
 * 
 *         <pre>
 * 백트레킹 문제인데
 * 
 * 계란을 깨기를 시도해서 최대한 많이 깬 경우 몇개깰 수 있는지 구하는 문제이다.
 * 
 * 풀이. dfs풀이
 * 
 * 1. 각 계란의 내구도와 무게를 따로 1차원 배열에 저장한다. 
 * 2. 가장 외쪽 부터 시작이니까 dfs(start=0,cnt=0, cur)으로 호출한다. 
 * 3. 친 계란 방문처리..
 * 
 * base condition -> 1. 모든 계란이 깨진경우 return 2. start==N인경우return 3. 
 * 현재들고있는 계란이 깨진경우 return;
 * 이러면 현재 계란의 idx값을 가지고 있어야하니까 매개변수로 넘긴다.
 * 
 * 
 * 가지치기
 * 현재 남아있는 모든 계란을 2번씩 깼다고 쳐도 최대값이 못되는 경우는 더이상 할 필요가 없다.
 * (남은거 다 깨도 max안되는 경우 -> (N-n)*2 < max)
 *         </pre>
 * 
 *
 */
public class Main {
	static int N, S[], W[], max;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(bf.readLine());
		S = new int[N];
		W = new int[N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(bf.readLine());
			S[i] = Integer.parseInt(st.nextToken());
			W[i] = Integer.parseInt(st.nextToken());
		}
		dfs(0, 0);// 계란 인덱스와 깨진 개수.
		System.out.println(max);

	}

	private static void dfs(int n, int cnt) {
		//가지치기 
		if(max>(cnt+(N-n)*2)) return;
		// 모든 계란 돌아본 경우 답갱신.
		if (n == N) {
			max = Math.max(max, cnt);
			return;
		}
		
		if (S[n] <= 0) {  	// 만약 내 계란이 깨진경우면 그냥 넘어가야한다.
			dfs(n + 1, cnt);
		} else {			// 아직 내 계란이 안깨진 경우.
			boolean flag = false;// 모든 계란이 깨졌는지 확인용도.
			for (int i = 0; i < N; i++) {
				// 상대 계란이 깨진경우, 나랑 같은경우, 이미 한번 친 경우는 무시한다.
				
				
				if (S[i] <= 0 || i == n )
					continue;
							
				
				flag = true; // 한번이라도 계란을 친경우.
				S[n] -= W[i];
				S[i] -= W[n];
				if (S[n] <= 0 && S[i] <= 0) {// 두개 깨진경우
					dfs(n + 1, cnt + 2);
				} else if (S[n] <= 0 || S[i] <= 0) {// 하나 깨진경우.
					dfs(n + 1, cnt + 1);
				}else {
					dfs(n + 1, cnt);
					
				}
				S[n] += W[i];
				S[i] += W[n];
			}
			if(!flag) dfs(n+1,cnt); // 더이상 칠 계란이 없으면 다음으로 넘겨준다.
		}

	}

}
