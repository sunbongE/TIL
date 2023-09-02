import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static int nums[],N,S,cnt;
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st =new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		nums = new int[N];
		st =new StringTokenizer(bf.readLine());
		for (int i = 0; i < nums.length; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		dfs(0,0,0);
		System.out.println(cnt);
		
	}
	private static void dfs(int n, int sm,int selectCnt) {
		if(n==N) {
			if(sm==S && selectCnt>0) {
				cnt++;
			}
			return;
		}
		// 선택하는 경우. 
		dfs(n+1, sm+nums[n],selectCnt+1);
		// 선택 안 하는 경우.
		dfs(n+1, sm,selectCnt);
	}
}