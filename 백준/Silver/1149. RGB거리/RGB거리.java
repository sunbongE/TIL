import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호
 * dp문제
 * 
 * 점화식 
 * dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2])+arr[i][0];
 * dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2])+arr[i][1];
 * dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1])+arr[i][2];
 * 
 *
 */
public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(bf.readLine());
		int[][] arr,dp;
		arr = new int[N+1][3]; // 점화식을 적용하기 위해 배열크기 늘린다.
		dp = new int[N+1][3];
		StringTokenizer st;
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(bf.readLine());
			for (int j = 0; j < 3; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 1; i <= N; i++) {
			dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2])+arr[i][0];
			dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2])+arr[i][1];
			dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1])+arr[i][2];
		}
		
		System.out.println(Math.min(dp[N][0], Math.min(dp[N][1], dp[N][2])));
	
	}

}
