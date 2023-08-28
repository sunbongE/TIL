import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.concurrent.PriorityBlockingQueue;

/**
 * 
 * @author 박태호
 * 
 * 
 *         - 4방향으로 움직일 수 있다. - 처음 상어 크기 : 2 ( 상어 크기만큼 물고기를 먹으면 1 성장함)
 * 
 *         - 자신보다 큰 물고기는 못 먹는다. - 자신과 같은 크기는 물고기는 지나갈 수 있다. - 자신보다 작은 물고기는 먹는다.
 * 
 *         먹을 때 - 가까운게 1마리면 걍 먹는다. - 가까운게 많으면 가장 위에 물고기를 먹는다. - 이것도 여러마리면 가장 왼쪽을
 *         먹는다.
 *
 *         - 먹을게 없으면 엄마상어 호출 == 답을 호출
 * 
 *         풀이 상어 클래스로 관리하면서 위치정보, 크기, cnt, d(이동 횟수==시간)를 기록한다. 상어 위치를 찾아서 상어
 *         객체생성. 상어를 맵에서 지운다.
 * 
 *         상어를 기준으로 너비우선탐색으로 최단경로에서 먹을 수 있는 물고기를 찾아본다.
 * 
 *         bfs를 상어 위치가 변할 때 마다 해야하고 언제까지 할지 모르니까 타입 boolean으로 하여 while문에 넣고 계속
 *         돌린다?
 * 
 */
public class Main {
	static class Fish implements Comparable<Fish> {
		int x, y, s, dis; // 위치 크기 거리

		public Fish(int x, int y, int s, int dis) {
			super();
			this.x = x;
			this.y = y;
			this.s = s;
			this.dis = dis;
		}

		@Override
		public int compareTo(Fish o) {
			if (this.dis == o.dis) {// 거리가 같은 경우.
				if (this.x == o.x) {

					return Integer.compare(this.y, o.y);
				} else {

					return Integer.compare(this.x, o.x);
				}

			} else {

				return Integer.compare(this.dis, o.dis);
			}
		}

	}

	static class Shark {
		int x, y, s, cnt, dis;

		public Shark(int x, int y, int s, int cnt, int dis) {
			super();
			this.x = x;
			this.y = y;
			this.s = s;
			this.cnt = cnt;
			this.dis = dis;
		}

		@Override
		public String toString() {
			return String.format("%s| %s| %s| %s| %s", x, y, s, cnt, dis);
		}

	}

	// direction
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int map[][], N, v[][];
//	static Stack<Shark> sharkLog = new Stack<>();
	static Shark shark;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(bf.readLine());
		StringTokenizer st;
		// 맵 입력.
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j = 0; j < N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				if (map[i][j] == 9) {
//					sharkLog.add(new Shark(i, j, 2, 0, 0)); // 상어 만들기.
					shark=new Shark(i, j, 2, 0, 0); // 상어 만들기.
					map[i][j] = 0; // 맵에서 상어 지움.
				}
			}
		}

		while (true) {
			// 방문 배열.
			v = new int[N][N];
//			Shark cur = sharkLog.peek();
			if (!bfs())
				break;
		}
//		System.out.println(sharkLog.peek().toString());
		System.out.println(shark.dis);

	}

	private static boolean bfs() {

		// 상어 현재 위치.
		int x, y;
		x = shark.x;
		y = shark.y;
		PriorityBlockingQueue<Fish> fishes = new PriorityBlockingQueue<>();
		Queue<int[]> que = new LinkedList<>();
		que.offer(new int[] { x, y });
		v[x][y] = 1;
		List<int[]> target = new ArrayList<>();
		int cur[], nx, ny;
		nx = x;
		ny = y;
		while (!que.isEmpty()) {
			cur = que.poll();
			x = cur[0];
			y = cur[1];
			// 4방향으로 퍼지며 이동 할 수 있는 칸을 기록해서
			// 그중에 먹을 수 있는 물고기 있으면 먹기.
			for (int dir = 0; dir < 4; dir++) {
				nx = x + dx[dir];
				ny = y + dy[dir];
				// 범위내, 미방문
				if (isIn(nx, ny) && v[nx][ny] == 0) {
					// 나보다 크면 넘어가야함.
					if (map[nx][ny] > shark.s) {
						continue;
					}
					que.offer(new int[] { nx, ny });
					v[nx][ny] = v[x][y] + 1; // 너비 기록. 이게 떨어진 거리
					// 먹이 후보저장.
					if (map[nx][ny] > 0 && map[nx][ny] < shark.s) {
						fishes.offer(new Fish(nx, ny, map[nx][ny], v[nx][ny]));
					}
				}

			}

//			System.out.println("==========================");
//			System.out.println(shark.toString());
//			for (int i = 0; i < N; i++) {
//				for (int j = 0; j < N; j++) {
//					System.out.print(v[i][j] + " ");
//				}
//				System.out.println();
//			}
//			System.out.println("map");
//			for (int i = 0; i < N; i++) {
//				for (int j = 0; j < N; j++) {
//					System.out.print(map[i][j] + " ");
//				}
//				System.out.println();
//			}
			}
		Fish tg=null;
		if (!fishes.isEmpty()) {
			tg = fishes.poll(); // 우선순위가 높은거 가져와서 먹음.
			shark.x = tg.x;
			shark.y = tg.y;
			if(++shark.cnt==shark.s) {
				shark.s++;
				shark.cnt=0;
			}
			shark.dis += tg.dis-1;
			map[tg.x][tg.y]=0;
			return true;
		}
		return false;
	}

	private static boolean isIn(int x, int y) {
		return 0 <= x && x < N && 0 <= y && y < N;
	}

}
