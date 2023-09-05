import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호
 * <pre>
 * 
 * 알고리즘 이름은 기억 안나지만
 * make();
 * find();
 * union();
 * 세개의 메서드로 끝장 낼 수 있다.
 * 
 * 
 * - 부모를 기록하는 배열하나. 1~N까지
 * - 
 * </pre>
 *
 */
public class Main {
	static int parents[],N,M,a,b;
	public static void main(String[] args) throws IOException {
		StringBuilder sb = new StringBuilder();
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		make();
		for (int i = 0; i < M; i++) {
			st= new StringTokenizer(bf.readLine());
			if(st.nextToken().equals("0")) {// union()호출
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				union(a,b);
			}else {// find() 호출
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				if(find(a)==find(b)) {
					sb.append("YES"+"\n");
				}else{
					sb.append("NO"+"\n");
				};
			}
			
		}
		System.out.println(sb);
		
	}
	// 부모를 리턴한다.
	private static int find(int cur) {
		int parent = parents[cur];
		if(parent==cur) return cur; // 최상위면 그 값을 리턴한다.
		return parents[cur]=find(parents[cur]);
	}
	
	
	private static void make() {
		parents = new int[N+1];
		for (int i = 0; i < parents.length; i++) {
			parents[i]=i;
		}
//		System.out.println(Arrays.toString(parents));
		
	}
	private static boolean union(int a , int b ) {
		int rootA = find(a);
		int rootB = find(b);
		
		if(rootA==rootB) return false;
		parents[rootB] = rootA;
		return true;
	}
}
