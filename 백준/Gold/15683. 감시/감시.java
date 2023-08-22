import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 
 * @author 박태호 풀이
 * 
 *         모든 카메라의 방향을 구하는 중복 순열을 만들어야한다. nPn; 카메라 개수만큼 배열크기 지정.
 * 
 * 
 * 
 *
 */
public class Main {
	static int[][] map, copy;
	// 위치랑,, 종류 들어가야해
	static List<int[]> cameraList = new ArrayList<>();
	static int N, M, cameraDir[], cameraCnt, ans = 100;
	// direction 우 상 좌 하
	static int[] dx = { 0, -1, 0, 1 };
	static int[] dy = { 1, 0, -1, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] inp = bf.readLine().split(" ");
		N = Integer.parseInt(inp[0]);
		M = Integer.parseInt(inp[1]);
		map = new int[N][M];
		int idx = 0;
		for (int i = 0; i < N; i++) {
			inp = bf.readLine().split(" ");
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(inp[j]);

				if (0 < map[i][j] && map[i][j] < 6) {
					cameraList.add(new int[] { i, j, map[i][j] });
					cameraCnt++; // 카메라 개수

				}
			}
		}
		// 카메라 개수만큼 방향 설정할 배열.
		cameraDir = new int[cameraCnt];
		// 중복순열을 구한다.(값은 0~4)
		per(0);
		// 중복 순열을 구하면 그것은 각 카메라가 감시하는 방향이다.
		// 근데 5번 카메라는 항상 4방향을 전부 보니까 5번 카메라 위치를 먼저 도는것이 좋을 듯 하다.

		// 5번 위치 돌린 후, 맵 변경됨.

		// 각 방향으로 호출할 건데
		System.out.println(ans);
	}

	private static void per(int n) {
		if (n == cameraCnt) {
			// 넘겨줄 복사 배열을 만들어준다.
			copy = copy();
			for (int i = 0; i < cameraCnt; i++) {
				// 카메라의 종류와 방향을 줘서 상황에 맞게 움직이면서 이상황에 사각지대가 얼마나 있는지 확인한다.
				moveCamera(cameraList.get(i), cameraDir[i]);
				// 여기서 구해진 순열대로 카메라 방향돌려보기.
			}
			// 복사한 맵이 변경되면 0의 개수를 파악해서 최소인지 알아야한다.
//			System.out.println(cameraDir);
			check();
			return;
		}
		for (int i = 0; i < 4; i++) {
			cameraDir[n] = i;
			per(n + 1);
		}

	}

	private static void check() {
//		 System.out.println("========================");
		int curCnt = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
//				System.out.print(copy[i][j]+" ");
				if (copy[i][j] == 0)
					curCnt++;
			}
//			System.out.println();
		}
		ans = Math.min(ans, curCnt);
	}

//	[x,y,camera] 
	private static void moveCamera(int[] camera, int dir) {
//		System.out.println(Arrays.toString(camera)+" "+dir);
		// 카메라별로 구분지어서 어디를 볼지 정해 줘야해
		if (camera[2] == 1) {
			cctv(camera[0], camera[1], dir);
		} else if (camera[2] == 2) {
			if (dir % 2 == 0) {// 짝수면 가로
				cctv(camera[0], camera[1], 0); // 오른쪽
				cctv(camera[0], camera[1], 2); // 왼쪽 보내줌
			} else {// 세로.
				cctv(camera[0], camera[1], 1); // 위
				cctv(camera[0], camera[1], 3); // 아래
			}

		} else if (camera[2] == 3) {// 0 -> 0,1 | 1 -> 1,2 | 2-> 2,3 | 3-> 3,0
			for (int i = dir; i <= (dir + 1); i++) {
				cctv(camera[0], camera[1], i % 4);
			}

		} else if (camera[2] == 4) {

			for (int i = dir; i <= (dir + 2); i++) {
				cctv(camera[0], camera[1], i % 4);
			}

		} else if (camera[2] == 5) {
			for (int i = 0; i < 4; i++) { // 4방향
				cctv(camera[0], camera[1], i % 4);
			}
		}

	}

	private static void cctv(int i, int j, int dir) {
//		System.out.println(i+" "+j);
		// 벽을 만나거나 범위를 나가면 끝내자
		if (!isIn(i, j) || map[i][j] == 6) {
			return;
		}
		// 복사한 지도 변경.
		if (copy[i][j] == 0)
			copy[i][j] = 7;
		cctv(i + dx[dir], j + dy[dir], dir);
	}


	private static int[][] copy() {
		int[][] tmp = new int[N][];
		for (int i = 0; i < N; i++) {
			tmp[i] = map[i].clone();
		}

//		for (int i = 0; i < tmp.length; i++) {
//			for (int j = 0; j < tmp[i].length; j++) {
//				System.out.print(tmp[i][j]+" ");
//			}
//			System.out.println();
//		}

		return tmp;
	}

	private static boolean isIn(int ni, int nj) {
		return 0 <= ni && ni < N && 0 <= nj && nj < M;
	}

}
