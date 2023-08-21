
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * 
 * @author 박태호
 * bfs(verson); 1번은 색약, 2번은 안색약.탐색으로간다.
 * 
 *
 */
public class Main {
	static char map[][];
	static boolean v[][];
	static int N;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(bf.readLine());
		map = new char[N][];
		for (int i = 0; i < N; i++) {
			map[i] = bf.readLine().toCharArray();
		}
		int cnt;
		for (int verson = 1; verson <= 2; verson++) {
			cnt=0;
			v = new boolean[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if(!v[i][j]) {
						cnt++;
						bfs(verson,map[i][j],i,j);
					}
				}
			}
			System.out.print(cnt+" ");
			
		}
	}
	
	
	private static void bfs(int verson, char b,int i, int j) {
		int[] dx = {-1,1,0,0};
		int[] dy = {0,0,-1,1};
		
		Queue<int[]> que = new LinkedList<int[]>();
		que.offer(new int[] {i,j});// 큐추가
		v[i][j]=true;//방문
		int[] cur;
		int ci,cj,ni,nj;
		while(!que.isEmpty()) {
			cur = que.poll();
			//현재 위치 입력
			ci = cur[0];
			cj = cur[1];
			for (int di = 0; di < 4; di++) {
				ni = ci+dx[di];
				nj = cj+dy[di];
				// 버전 1일때 
				if(verson==1) {
					// 범위내, 방문x, 색이 같으면.
					if (isIn(ni,nj)&&map[ni][nj]==b&&!v[ni][nj]) {
						que.offer(new int[] {ni,nj});
						v[ni][nj]=true;
					}
				}
				// 버전 2일때
				else if(verson==2) {
					if (isIn(ni,nj) ) {//범위내
						// 파랑색인경우,방문x, 다음 위치의 색이 같으면.
						if (b=='B' &&map[ni][nj]==b&&!v[ni][nj]) {
							que.offer(new int[] {ni,nj});
							v[ni][nj]=true;
						}else if(b!='B' &&(map[ni][nj]=='G'||map[ni][nj]=='R')&&!v[ni][nj]) { 
							// 파란색아니고 다음 위치가 초록이나 빨강이면 그리고 방문처리가 안되어 있다면.
							que.offer(new int[] {ni,nj});
							v[ni][nj]=true;
						}
					}
				}
			}
		}
	}


	private static boolean isIn(int ni, int nj) {
		return 0<=ni && ni < N && 0<= nj && nj < N;
	}

}
