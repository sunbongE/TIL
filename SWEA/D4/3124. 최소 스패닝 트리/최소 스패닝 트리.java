import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Solution {
	static class Edge implements Comparable<Edge>{
		int from;
		int to;
		int val;
		public Edge(int from, int to, int val) {
			this.from = from;
			this.to = to;
			this.val = val;
		}
		@Override
		public int compareTo(Edge o) {
			// 오름차순 정렬.
			return Integer.compare(this.val, o.val);
		}
		
	}
	
	static int V,E;
	static Edge[] edgeArr;
	static int[] parents;
	public static void make() {
		parents = new int[V+1];
		for (int i = 1; i <= V; i++) {
			parents[i]=i;
		}
	}
	
	public static int find(int a) {
	    if (parents[a ] == a) return a;
	    return parents[a ] = find(parents[a ]);
	}

	
	public static boolean union(int a, int b) {
		int aRoot = find(a);
		int bRoot = find(b);
		if(aRoot==bRoot)return false;
		
		parents[bRoot] = aRoot;
		return true;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(bf.readLine());
		StringTokenizer st ;
		int from,to,val;
		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(bf.readLine()," ");
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			
			// 엣지 배열 선언
			edgeArr = new Edge[E];
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(bf.readLine()," ");
				from = Integer.parseInt(st.nextToken());
				to = Integer.parseInt(st.nextToken());
				val = Integer.parseInt(st.nextToken());
				edgeArr[i] = new Edge(from,to,val);
			}
			
			// 간선 리스트 정렬
			Arrays.sort(edgeArr);
			
			// 정점 만들기
			make();
			
			// 비용이 작은 순으로 꺼내며 서로소 집합 관계라면 연결하는 방식으로 풀이한다.
			long result = 0;
			int cnt=0;
			for (Edge edge : edgeArr) {
				if(union(edge.from,edge.to)) {
					cnt ++;
					result += edge.val;
					if(cnt == V-1)break;
				}
			}
			sb.append("#"+tc+" "+result+"\n");
		}
		System.out.println(sb);
	}

}
