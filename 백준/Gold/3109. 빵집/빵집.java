import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[][] v;
	static int R, C, ni, nj, ans = 0;
	static String[][] map;
	// 대각선 위, 오른쪽, 대각 아래
	static int[] dx = { -1, 0, 1 };
	static int[] dy = { 1, 1, 1 };

	static boolean flag;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String inp[] = bf.readLine().split(" ");

		R = Integer.parseInt(inp[0]);
		C = Integer.parseInt(inp[1]);
		map = new String[R][C];
		v = new int[R][C];
		String[] tmp;

		for (int i = 0; i < R; i++) {
			map[i] = bf.readLine().split("");
		}
		// 입력 끝
		// 각 행마다 돌아봐야한다.
		for (int row = 0; row < R; row++) {
			flag=false;
			dfs(row, 0);

		}
		System.out.println(ans);
	}

	private static void dfs(int row, int col) {
		// 대각선 위 -> 오른쪽 -> 대각 아래 순으로 이동하면서 끝에 도달하면 return하고 
		// 다음 행으로 가야하니까 flag를 하나 만들어
		// 도달 했을 때 flag =true해서 완전 dfs를 탈출 할 수 있게 한다.
		if(flag)return; // 답을 찾은 경우
		
		if(col==C-1) {
			ans ++;
			flag = true;
			return;
		}
		// 방문한 장소는 값을 변경한다.
		map[row][col] = "X";
		// 다음 위치가 .이면 보내고 아니면 다음 방향을 돌 수 있어야한다.
		for (int i = 0; i < 3; i++) {
			ni = row+dx[i];
			nj = col+dy[i];
			if(isIn(ni,nj) && map[ni][nj].equals(".")) {
				dfs(ni,nj); // 다음 위치를 넘겨준다.
			}
			if(flag)break;
		}
	}

	private static boolean isIn(int i, int j) {
		return 0<=i&& i < R && 0<= j && j < C;
	}
}