
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 
 * @author 박태호 bfs문제 map 2중배열 생성. map 2중 배열과 같은 크기의 방문배열 생성
 * 
 *         2중 for -> if 방문이 안되어있고 map[i][j]==1인 곳의 위치를 bfs(i,j,cnt) 매개변수로 보내준다.
 *         bfs에서 연결된 모든 것을 방문하고 개수를 찾아온다.
 * 
 *
 */
public class Main {
	static int n, m, map[][];
	static boolean v[][];

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] inp = bf.readLine().split(" ");
		n = Integer.parseInt(inp[0]);
		m = Integer.parseInt(inp[1]);
		map = new int[n][m];
		v = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			inp = bf.readLine().split(" ");
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(inp[j]);
			}
		}
//		if(n==1&&m==1) {
//			System.out.println(0);
//			System.out.println(0);
//			return;
//		}
		
		int cnt = 0, ans = 0,C=0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {

				if (map[i][j] == 1 && !v[i][j]) {
					C++;
					cnt = bfs(i, j, 0);
//					System.out.println(cnt);
					ans = Math.max(ans, cnt);
				}
			}
		}
		System.out.println(C);
		System.out.println(ans);
	}

	private static int bfs(int i, int j, int cnt) {
		Queue<int[]> que = new LinkedList<int[]>();
		int[] dx = { -1, 1, 0, 0 };
		int[] dy = { 0, 0, -1, 1 };
		que.offer(new int[] { i, j });
		v[i][j] = true; // 방문.

		int ci, cj, ni, nj, cur[];
		while (!que.isEmpty()) {
			cnt++;
			cur = que.poll();
			ci = cur[0];
			cj = cur[1];

			for (int di = 0; di < 4; di++) {
				
				ni = ci + dx[di];
				nj = cj + dy[di];
				// 범위내, 값이 1 , 방문 x
				if (isIn(ni, nj) && map[ni][nj] == 1 && !v[ni][nj]) {
					que.offer(new int[] { ni, nj });
					v[ni][nj] = true;

				}
			}
			}
		return cnt;
	}

	private static boolean isIn(int ni, int nj) {
		// TODO Auto-generated method stub
		return 0 <= ni && ni < n && 0 <= nj && nj < m;
	}
}
