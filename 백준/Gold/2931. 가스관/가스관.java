import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호 풀이 Z,M 각각에서 출발해서 끝나는 지점이 같으면 그 지점에 블럭을 놓아야한다. 거기에 들어갈 수 있는 블록을
 *         유추할 수 있는데 양쪽 방향을 모두 수용할 수 있는 것이 오면 유추가능하다.
 * 
 *         그리고 후보가 되는 블럭을 전부 넣어보고 방문 배열의 true의 개수와 dfs으로 순회한 cnt개수가 같으면 답이된다.
 * 
 *
 */
public class Main {
	// direction
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	// 배열 크기, 시작과 끝 위치, m,z의 진행방향 | ti,tj 바꿀땅이 어딘지 알려줌
	static int R, C, mx, my, zx, zy, mdir, zdir, ti, tj;
	static char map[][];
	static boolean v[][], copy[][],flagT=true;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		// map 입력.
		map = new char[R][];
		for (int i = 0; i < R; i++) {
			map[i] = bf.readLine().toCharArray();
		}
		v = new boolean[R][C];

		// m,z위치를 받아오고 '.'이 아닌 것의 개수를 세어준다.
		int cnt = 0; // 나중에 dfs으로 길을 전부 돌아봤을 때의 수와 같으면 답이되게 할 때 사용.
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (map[i][j] != '.') {
					if(map[i][j]=='+') {
						cnt+=2;
					}else {
						cnt++;
					}
					v[i][j] = true; // 길이 아닌 곳 막아버리기.
				}
				// 시작 끝 위치.
				if (map[i][j] == 'M') {
					mx = i;
					my = j;
					mdir = getDir(mx, my);
				}
				if (map[i][j] == 'Z') {
					zx = i;
					zy = j;
					zdir = getDir(zx, zy);
				}
			}
		}
//		System.out.println(cnt);
		// 원본은 나중에 써야하니까 일단 복사함.
		dfs(mx, my, mdir);
		v[ti][tj]=true; // 
		
//		System.out.println(ti + " " + tj);
		// ti,tj 찾아 왔고 이제 이 위치에 가능한 7가지 블럭을 전부 넣어본다.
		char block[] = { '|', '-', '+', '1', '2', '3', '4' };
		for (int i = 0; i < 7; i++) {
			copy = new boolean[R][C];
			for (int k = 0; k < R; k++) {
				copy[k] = v[k].clone();
			}
			map[ti][tj] = block[i];
			sol(mx, my, mdir, cnt);
//
		}

	}

	private static void sol(int si, int sj, int dir, int cnt) {
//		System.out.println(si+" "+sj);
		if(dir==-1)return;
		copy[si][sj]=false;
		if(map[si][sj]=='Z') {
//			System.out.println((ti+1)+" "+(tj+1)+" "+map[ti][tj]);
			if(isAns()) {
				System.out.print((ti+1)+ " "+(tj+1)+" "+map[ti][tj]+"\n");
				System.exit(0);
			}
			return;
		}
		int ni,nj;
		ni = si+dx[dir];
		nj = sj+dy[dir];
		if(!isIn(ni,nj)) return;
		if(isIn(ni,nj)) {
			sol(ni,nj,getDir(map[ni][nj], dir),cnt-1);
		} 
		
	}
	/// 답 갱신.
	private static boolean isAns() {
//		System.out.println("==============");
//		for (int i = 0; i < R; i++) {
//			for (int j = 0; j < C; j++) {
//				System.out.print(v[i][j]+" ");
//			}
//			System.out.println();
//		}
		int ni,nj;
		for (int i = 0; i < 4; i++) {
			ni = ti+dx[i];
			nj = tj+dy[i];
			if(isIn(ni,nj)) {
				if(copy[ni][nj]==true)return false; // 미방문한 도로가 있으면 취소.
			}
		}
		return true;
	}

	// 현재 땅에 표시된 방향대로만 가야하니까 방문체크는 필요없다.
	private static void dfs(int si, int sj, int dir) {
		// 범위를 벗어나거나 '.'을 밟으면 멈춘다.
		if ((map[si][sj] == '.'||dir==-1)&&flagT) {
			flagT=false;
			ti = si;
			tj = sj;
			return;
		}
		int ni, nj;
		// 시작위치면 그냥 dir방향으로 가고 시작위치가 아니면 현재 밟은 땅을 기준으로 방향을 정한다.
		// 현재 dir대로 다음 위치를 찾고 dfs넘기기전에 다음 위치정보 바탕으로 방향을 찾아서 넘겨준다.

		ni = si + dx[dir];
		nj = sj + dy[dir];
		if (isIn(ni, nj)) { // 범위에 있을때 넘김.
			dfs(ni, nj, getDir(map[ni][nj], dir));
		}

	}

	// 상 하 좌 우
	private static int getDir(char d, int dir) {
		if(d=='Z')return 0;
//		System.out.println(d+" "+dir);
		if (d == '+') { // 3개는 가던 방향 그대로 가라고 준다.
			return dir;
		}

		if (d == '1') {
			if (dir == 2) { // 왼쪽으로 들어오면 아래로 나가.
				return 1;
			}
			if (dir == 0)return 3; // 아래에서 위방향으로 들어오면 오른쪽으로 나가.
				
		} else if (d == '2') {
			if (dir == 1)
				return 3; // 아래로오면 오른쪽으로
			if (dir == 2)
				return 0; // 왼쪽으로 오면 위로
		} else if (d == '3') {
			if (dir == 3)
				return 0;
			if (dir == 1)
				return 2;
		} else if (d == '4') {
			if (dir == 3)
				return 1;
			if (dir == 0)
				return 2;
		} else if (d == '|') {
			if (dir == 0)
				return 0;
			if (dir == 1)
				return 1;
		} else if (d == '-') {
			if (dir == 2)
				return 2;
			if (dir == 3)
				return 3;

		}
		return -1;

	}

	private static int getDir(int x, int y) {
		int ni, nj;
		for (int i = 0; i < 4; i++) {
			ni = x + dx[i];
			nj = y + dy[i];
			if (isIn(ni, nj) && map[ni][nj] != '.' && map[ni][nj] != 'M'&&map[ni][nj] != 'Z') {// 다음 위치가 길이면 그게 방향임.
				return i;
			}
		}

		return 0;
	}

	private static boolean isIn(int ni, int nj) {
		return 0 <= ni && ni < R && 0 <= nj && nj < C;
	}
}
