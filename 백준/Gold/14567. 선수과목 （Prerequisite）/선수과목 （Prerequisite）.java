import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호
 * <pre>
 * 위상 정렬 문제
 * 최소 몇학기에 이수할 수 있는지 구하는 문제
 * 
 * 풀이
 *  
 * </pre>
 *
 */
public class Main {
	static int N,M,indegree[],ans[];
	static List<Integer>[] adjList;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		adjList = new ArrayList[N+1];
		for (int i = 0; i < N+1; i++) {
			adjList[i] = new ArrayList();
		}
		
		int a,b;
		indegree = new int[N+1];
		ans = new int[N+1];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(bf.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			adjList[a].add(b); // 유향으로 선수과목을 기록한것.
			// 진입 차수 기록
			indegree[b]++;
		}
		// que생성
		Queue<Integer> que = new LinkedList<Integer>();
		
		// 진입 차수중에서 0인 것은 que에 넣고 ans 배열에 1으로 초기화한다.
		for (int i = 1; i < indegree.length; i++) {
			if(indegree[i]==0) {
				// que삽입
				que.offer(i);
				// ans 1으로 초기화
				ans[i]=1;
			}
		}
		int cur,c;
		// while 큐가 빌때까지
		while(!que.isEmpty()) {
			// 진입 차수 0인거 뽑아서 선수과목의 진입 차수를 줄여나갈것
			cur = que.poll();
			for (int i = 0; i < adjList[cur].size(); i++) {
				c = adjList[cur].get(i);
				indegree[c]--;
				if(indegree[c]<=0) { // 진입차수가 0이 되면 넣어야함.
					que.offer(c);
					ans[c] = ans[cur]+1;
				}
			}
		}
//		System.out.println(Arrays.toString(ans));
		for (int i = 1; i < ans.length; i++) {
			System.out.print(ans[i]+" ");
		}
		
	}

}
