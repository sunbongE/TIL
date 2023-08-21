import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Main {
	static int N,M,indegree[];
	static ArrayList<Integer>[] list;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] inp = bf.readLine().split(" ");
		N = Integer.parseInt(inp[0]);
		M = Integer.parseInt(inp[1]);

		list = new ArrayList[N+1];
		for (int i = 0; i < N+1; i++) {
			list[i] = new ArrayList<Integer>();
		}
		// 진입 차수, 간선정보 모두 파악해둠.
		indegree = new int[N+1];
		int from,to;
		for (int i = 0; i < M; i++) {
			inp = bf.readLine().split(" ");
			from = Integer.parseInt(inp[0]);
			to = Integer.parseInt(inp[1]);
			indegree[to]++;
			list[from].add(to); // 어디를 보고있는지 저장해둠.
		}
		bfs();
		
		
	}
	private static void bfs() {
		// 진입차수가 0인것은 모두 que에 저장
		Queue<Integer> que = new LinkedList<>();
		for (int i = 1; i <= N; i++) {//1~N까지.
			if(indegree[i]==0) {
				que.offer(i);
			}
		}
		int tmp;
		while(!que.isEmpty()) {
			tmp=que.poll();
			System.out.print(tmp+" ");
			for (Integer cur : list[tmp]) {
				indegree[cur]--;
				if(indegree[cur]==0) que.offer(cur);
			}
			
		}
		
		
	}

}
