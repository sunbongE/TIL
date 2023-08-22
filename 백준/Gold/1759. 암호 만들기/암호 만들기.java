import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호
 * 
 *         L 개로 구성 - 최소 1개의 모음 필요. - 최소 2개의 자음으로 구성. - 오름차순.
 * 
 *         백트 n==L이 되면 종료. 선택 한다 안한다로 계속 간다.
 *
 */
public class Main {
	static char alpa[], result[];
	static boolean[] v;
	static int L, C;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());

		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		v = new boolean[C];// 방문.
		result = new char[L];
		alpa = bf.readLine().replaceAll(" ", "").toCharArray();
		Arrays.sort(alpa);
		dfs(0, 0); //
		System.out.println(sb);
	}

	private static void dfs(int n, int i) {
		if (n == L) {
			if(check(result)) {
				for (int j = 0; j < result.length; j++) {
					sb.append(result[j]);
				}
				sb.append("\n");
			}
			return;
		}
		if (i==C) {
			return;
		}
		result[n] = alpa[i];
		dfs(n + 1, i + 1);
		dfs(n, i + 1);

	}

	private static boolean check(char[] result) {
		// 최소 모음 1개
		// 최소 자음 2개	
		int preLen=result.length;
		// 모음 제거 작업을 하고 제거 후에 길이가 전에 길이와 같다면 false
		int cnt=0;
		for (int i = 0; i < result.length; i++) {
			if(result[i]=='a'||result[i]=='e'||result[i]=='i'||result[i]=='o'||result[i]=='u') {
				cnt++;
			}
		}
		
		// 모음을 제거하고 길이가 2보다 작으면 false
		if(cnt==0) {
			return false;
		}else {// 모음이 있고 모음개수를 뺐더니 길이가 2보다 작으면 안된다.
			if(preLen-cnt<2) {
				return false;
			}
		}
		// 그 외에 true;
		return true;
	}

}
