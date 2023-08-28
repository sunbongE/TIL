import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int thIdx[][] = new int[4][2];
	static List<Integer>[] lst = new ArrayList[4];
	public static void main(String[] args) throws IOException {
		for (int i = 0; i < 4; i++) {
			lst[i] = new ArrayList<>();
		}
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String inp;
		int val;
		for (int i = 0; i < 4; i++) {
			inp = bf.readLine();
			for (int j = 0; j < 8; j++) {
				val =Character.getNumericValue(inp.charAt(j));
				lst[i].add(val);
				if(j==2) {
					thIdx[i][0] = val;// 3번째 
				}else if(j==6) {
					thIdx[i][1] = val;// 7번째 
				}
			}
		}
		int K = Integer.parseInt(bf.readLine());
		int idx, dir,allDir[];
		boolean target[];
		String  command[];
		for (int i = 0; i < K; i++) {
			command = bf.readLine().split(" ");
			idx = Integer.parseInt(command[0])-1;
			dir = Integer.parseInt(command[1]);
			// idx 짝수면 0,2 번 인덱스 dir 으로 
			// 나머지 dir반대로 설정,
			allDir = getDir(idx,dir);
			
			// 대상이 되는 것을 찾는 메서드 하나 만듬.
			target=getTarget(idx);

			
			// 대상이 되는 것과 방향을 넘겨주면 위치를 변경시키는 작업을 하는 메서드.
			change(target,allDir);
//			for (int j = 0; j < 4; j++) {
//				for (int j2 = 0; j2 < 8; j2++) {
//					System.out.print(lst[j].get(j2)+" ");
//				}
//				System.out.println();
//			}
			thIdx = research();
		}
		
		// 점수 갱신 각 0번 인덱스의 값을 가지고 합산한다.
		int ans=0;
		if(lst[0].get(0)==1) ans+=1;
		if(lst[1].get(0)==1) ans+=2;
		if(lst[2].get(0)==1) ans+=4;
		if(lst[3].get(0)==1) ans+=8;
		
		System.out.println(ans);
	}
	
	private static int[][] research() {
		int[][] result = new int[4][2];
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 8; j++) {
				if(j==2) {
					result[i][0] = lst[i].get(j);
				}else if(j==6) {
					result[i][1] = lst[i].get(j);
				}
			}
		}
		return result;
	}

	private static void change(boolean[] target, int[] allDir) {
//		System.out.println();
//		System.out.println(Arrays.toString(target));
//		System.out.println(Arrays.toString(allDir));
		// target == true 인 인덱스 lst의 값을 변경해야하는데 
		int tmp=-1;
		for (int i = 0; i < 4; i++) {
			if(target[i]) {// 타겟이면.
				//위치를 본다.
				// 방향이 1이면 시계방향 뒤에 값을 제거하고 앞으로 넣음
				if(allDir[i]==1) {
					tmp = lst[i].remove(7);
					lst[i].add(0, tmp);
				}else {
					// 반대는 앞에꺼 하나빼서 뒤로 넣음.
					tmp = lst[i].remove(0);
					lst[i].add(tmp);
				}
				
			}
		}
		
	}

	// 변경할 톱니 찾기.
	private static boolean[] getTarget(int idx) {
		boolean result[]=new boolean[4];
		result[idx] = true;
		// 뒤에 연결된거 찾기
		for (int i = idx; i < 3; i++) {
			// i번째의 3번째 수와 i+1의 7번재 수가 같으면 break;
			if(thIdx[i][0]==thIdx[i+1][1]) break;
			else result[i+1] = true;
			//다르면 result[i+1] = true
		}
		//앞에 연결된거 찾기. ( 만약 값이 서로 같으면 break;)
		for (int i = idx; i > 0; i--) {
			if(thIdx[i][1]==thIdx[i-1][0]) break;
			else result[i-1] = true;
		}
		
		return result;
	}
	// 변경할 방향을 찾음.
	private static int[] getDir(int idx, int dir) {
		int Rdir=0;// 반대방향.
		if(dir==1) {
			Rdir=-1;
		}else {
			Rdir=1;
		}

		if(idx%2==0) {
			return new int[] {dir,Rdir,dir,Rdir};
		}else {
			return new int[] {Rdir,dir,Rdir,dir};
		}
	}

}
