import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호
 * 
 *         <pre>
 * 1. 땅이랑 가장 가까운 상어를 잡는다. 
 * 2. 상어가 이동한다. 
 * 2-1. 상어가 이동하다 벽을 만나면 반대로 방향을 바꿔서 이동한다.
 *          
 * 2-2. 한칸에 여러 상어가 있을 수 있다. 
 * 3. 이동이 끝나고 한 칸에 상어가 여러마리면 그 상어중 가장 큰 상어가 다 잡아먹는다.
 * 
 * 낚시왕이 잡은 상어의 크기 합을 구하라.
 * 
 * 상어는 크기와 번호로 구분가능하다.
 *         </pre>
 */
public class Main {
	static class Shark {
		int idx;
		// 위치
		int x;
		int y;
		/// 속도
		int s;
		// 방향
		int d;
		// 크기.
		int z;

		public Shark(int idx,int x, int y, int s, int d, int z) {
			this.idx = idx;
			this.x = x;
			this.y = y;
			this.s = s;
			this.d = d;
			this.z = z;
		}
		/* (non-Javadoc)
		 * @see java.lang.Object#toString()
		 */
		@Override
		public String toString() {
			return String.format("Shark [idx=%s, x=%s, y=%s, s=%s, d=%s, z=%s]", idx, x, y, s, d, z);
		}

	}

	// direction 1~4 : 상 하 우 좌
	static int[] dx = { 0, -1, 1, 0, 0 };
	static int[] dy = { 0, 0, 0, 1, -1 };
	static Shark map[][] ;
	static ArrayList<Shark> sharkList = new ArrayList<>();
	static int  R, C, M, sum;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		map = new Shark[R+1][C+1];

//		상어 정보 입력.
		int tx, ty, ts, td, tz;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(bf.readLine());
			tx = Integer.parseInt(st.nextToken());
			ty = Integer.parseInt(st.nextToken());
			ts = Integer.parseInt(st.nextToken());
			td = Integer.parseInt(st.nextToken());
			tz = Integer.parseInt(st.nextToken());
			sharkList.add(new Shark(i,tx, ty, ts, td, tz));
			// 상어를 맵에 넣어보자..
			map[tx][ty] = sharkList.get(i);
//			System.out.println(sharkList.get(i).toString());
		}
		// 사람이 1~M까지 가면 끝나야함.
		for (int i = 1; i <= C; i++) {
			// step 1. 낚시왕이 이동한다.
			
			// step 2. 땅이랑 가까운 상어를 잡는다.
			killShark(i);
			
			
			//step 3. 상어 이동시킨다.
			// 상어 리스트에 있는 상어 좌표 값에 방향과 속도에 맞게 값을 더하고 범위가 넘어가면 방향을 변경하여 이동하게 만든다.
			
			changePosition();
			// 전부 바꿔주고 map에다가 넣어주는데 넣기전에 맵 초기화한다.
			mapInit();
			
			// map에 상어들을 배치한다.
			setShark();
			
//			System.out.println("====================");
//			for (int j = 0; j < sharkList.size(); j++) {
//				System.out.println(sharkList.get(j).toString());
//			}
			// 이동시킨 상어의 위치가 같으면 더 큰놈이 잡아먹는다.
			// 이동시키는 로직은 정말 하나씩 이동시키는 것이 아니고 주어진 방향으로
			// 이동하게 좌표값에 합해준다.
			// 해당 좌표에 뭔가 있으면 크기비교해서 둘중 하나만 남게 해야하는데 아직 이동한 최종값은 모르기 때문에 
			// 좀 더 생각해보자.
		}
		System.out.println(sum);
		

	}
	// 상어 재배치 함수.
	private static void setShark() {
		int mi,mj;
		for (int i = sharkList.size()-1; i >=0 ; i--) {
			mi = sharkList.get(i).x;
			mj = sharkList.get(i).y;
			// 이동을 확정 시킬 위치에 이미 다른 상어가 있으면 싸워야하는데 그전에 없는 상황먼저 처리.
			if(map[mi][mj]==null) {
				map[mi][mj] = sharkList.get(i);
			}else {// 이미 다른 상어가 있다면 크기가 큰놈을 놓고 작은 놈은 상어 리스트에서 삭제시킨다.
				// 누가 더 큰지 비교
				if(sharkList.get(i).z > map[mi][mj].z) { // 현재 값이 더 크면 
					// 잡아 먹힌 상황
					sharkList.remove(map[mi][mj]);
					// 있던 값 없애고 내가 들어가기.
					map[mi][mj] = sharkList.get(i);
				
				}else { // 내가 더 작으면, 나 없애기.
					sharkList.remove(i);
				}
				
			}
		}
	}
	// 맵초기화 함수.
	private static void mapInit() {
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[i].length; j++) {
				map[i][j] = null;
			}
		}
	}
	// 상어 위치 변경함수.
	private static void changePosition() {
		int ni,nj,C,ci,cj;
		
		for (int i = 0; i < sharkList.size(); i++) { // 모든 상어들의 위치를 변경한다.
			// 현재상어 위치
			ci = sharkList.get(i).x;
			cj = sharkList.get(i).y;
			C =  sharkList.get(i).s;
			while(C>0) {
				ni = ci + dx[sharkList.get(i).d];
				nj = cj + dy[sharkList.get(i).d];
				if(isIn(ni,nj)) {
					C--;
					ci = ni;
					cj = nj;
				}else {// 범위를 벗어나면 반대 방향으로 변경한다.
					if(sharkList.get(i).d==1) {
						sharkList.get(i).d=2;
					}else if(sharkList.get(i).d==2) {
						sharkList.get(i).d=1;
					}else if(sharkList.get(i).d==3) {
						sharkList.get(i).d=4;
					}else if(sharkList.get(i).d==4) {
						sharkList.get(i).d=3;
					}
				}
			}
			// 마지막값으로 변경
			sharkList.get(i).x = ci;
			sharkList.get(i).y = cj;
		}
		
	}

	private static boolean isIn(int ni, int nj) {
		return 1<=ni&&ni<=R && 1<=nj&&nj<=C;
	}

	private static void killShark(int i) {
		for (int j = i; j <= i; j++) {
			for (int k = 1; k < R+1; k++) {
				if(map[k][j]!=null) { // 상어가 있으면 
					sum+=map[k][j].z; // 상어 크기 합.
//					System.out.println(map[k][j].s+ " i="+i);
					// 상어 목록에서도 지워준다.

					sharkList.remove(map[k][j]);
					map[k][j] = null; // 잡으면 그자리 비워줌.
					return;
				}
			}
		}
	}

}
