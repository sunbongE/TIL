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
 * 
 * 조합을 구하고 연결된지 확인하는 방식.
 * 1. 조합을 먼저 구한다.
 * 2. true 그룹이랑 false 그룹을 나눠서 두 그룹이 연결되어 잇는지 확이한다.
 * 
 *
 */

public class Main {
	static int p[], minVal=Integer.MAX_VALUE,total, result[],N;
	static ArrayList<Integer>[] adjList;
	static boolean v[],  A[],B[];
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(bf.readLine());
		StringTokenizer st;
		
		p = new int[N + 1];
		st = new StringTokenizer(bf.readLine()," ");
		for (int i = 1; i <= N; i++) {
			p[i] = Integer.parseInt(st.nextToken());
		}
//		System.out.println(Arrays.toString(p));
		adjList = new ArrayList[N+1];
		
		for (int i = 0; i < N+1; i++) {
			adjList[i] = new ArrayList<Integer>();
		}

		// 인접리스트 생성
		int c;
		for (int i = 1; i <= N; i++) {
			 st = new StringTokenizer(bf.readLine(), " ");
			c = Integer.parseInt(st.nextToken());
			for (int j = 0; j < c; j++) {
				adjList[i].add(Integer.parseInt(st.nextToken()));
			}
		} 

		// 방문배열 생성.
		
		// 조합을 구하는데 1 ~ n의 반절만 구한다.
		for (int i = 1; i <= N/2; i++) {
			v = new boolean[N+1];
			v[0] = true;
			result = new int[i];
			combi(0,1,i);
		}
		if(minVal==Integer.MAX_VALUE)System.out.println(-1);
		else System.out.println(minVal);
		
	}
	
	private static void combi(int n, int start, int target) {
		if(n==target) { // 1,2,3 ... N/2
			// v배열에 true인것과 true가 아닌 그룹으로 나눈 후 각 그룹이 연결되어 있는지 확인한다.
			// 그룹을 나눠주는 함수.
//			System.out.println(Arrays.toString(v));
			if(groupSplit()) {// 둘이 연결돼있어서 답 유추해도 되는 상황.
				// v배열에 true인 인덱스의 인구수와 false인 인덱스 인구수의 차이를 구하는 메서드.
				int sub = getSub();
//				System.out.println(Arrays.toString(result) + "sub: "+sub);
				minVal = Math.min(sub, minVal);
			}
			return ;
		}
		
		for (int i = start; i <= N; i++) {
			if(v[i])continue;
			v[i] = true;
			result[n]=i;
			combi(n+1,i+1,target);
			v[i] = false;
			
		}
		
	}
	private static int getSub() {
//		System.out.println("========");
//		System.out.println(Arrays.toString(p));
		int a=0;
		int b=0;
		for (int i = 1; i < v.length; i++) {
			if(v[i]) {
				a+=p[i];
			}else {
				b+=p[i];
			}
		}
//		System.out.println("a, b = "+a+", "+b);
		return Math.abs(a-b);
	}

	private static boolean groupSplit() {
		
		A = new boolean[N+1];// 선택된그룹
		B = new boolean[N+1];// 반대 그룹
		
		// 그룹을 나누고 각 그룹을 bfs으로 보내서 연결되어 있는지 확인한다.
		for (int i = 1; i < v.length; i++) {
			if(v[i]) A[i] = true;
			else B[i] = true;
		}
		boolean[] copy = new boolean[N+1]; 
//		System.out.println("=========================");
//		System.out.println("A-> "+Arrays.toString(A));
		bfs(A,copy,B);
//		System.out.println("copy-> "+Arrays.toString(copy));
		// A그룹이 전부 연결되었는지 확인 (copy에 A가 true인 인덱스가 true면 연결)
		
		for (int i = 1; i < A.length; i++) {
			if(A[i]&&!copy[i]) {// 두 값이 다른 상황.
				return false;
			}
		}
		// B그룹 연결여부확인.
//		System.out.println("B-> "+Arrays.toString(B));
		copy = new boolean[N+1]; 
		bfs(B,copy,A);
		// A그룹이 전부 연결되었는지 확인 (copy에 A가 true인 인덱스가 true면 연결)
		for (int i = 1; i < B.length; i++) {
			if(B[i]&&!copy[i]) {// 두 값이 다른 상황.
				return false;
			}
		}
		return true;
	}

	private static void bfs(boolean[] group, boolean[] copy,boolean[] group2) {
		int root=-1;
		for (int i = 1; i < group.length; i++) {
			if(group[i]) {
				root = i;
				break;
			}
		}
		if(root==-1) {
			return;
		}
//		System.out.println("Root : "+root);
		Queue<Integer> que = new LinkedList<Integer>();
		que.offer(root);
		copy[root]=true;
		int cur ; 
//		System.out.println("root: "+root);
		while(!que.isEmpty()) {
			cur = que.poll();
			for (Integer p : adjList[cur]) {
				if(!copy[p]&&!group2[p]) { //방문안됐고, 상대팀이 아닌거
					copy[p] = true; // 방문처리
					que.offer(p);
				}
			}
		}
	}

}