import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int n, arr[][], ans = Integer.MAX_VALUE;
	static boolean v[];

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(bf.readLine());

		arr = new int[n][n];
		StringTokenizer st;
		int inp;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j = 0; j < n; j++) {
				inp = Integer.parseInt(st.nextToken());
				arr[i][j] = inp;
			}
		}
		v = new boolean[n];
		v[0] = true;
		dfs(0, 0); // 위치, sum

		System.out.println(ans);
	}

	private static void dfs(int cur, int sm) {
		if (isAllVisited()) {// 모두 방문처리 되어있는 경우.
			// 길이 연결되어 있는지 확인한다.
			if(arr[cur][0]!=0) {
				ans = Math.min(ans, sm+arr[cur][0]);
			}
			return;
		}
		
		for (int i = 1; i < n; i++) {
			// 방문이 안되어있고 0이 아닌경우
			if(!v[i] && arr[cur][i]!=0) {
				v[i] = true;
				dfs(i,sm+arr[cur][i]);// 이동 위치로 시작, 이동거리 합.
				v[i] = false;
				
			}
		}
		

	}
	
	// 모든 위치를 방문했는지 확인한다.
	private static boolean isAllVisited() {
		for (int i = 0; i < v.length; i++) {
			if(!v[i]) return false;
		}
		return true;
	}

}
