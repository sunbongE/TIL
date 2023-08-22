import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int[] parents;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(bf.readLine());
		int n, m;
		StringTokenizer st;
		int a, b, result;
		String command;
		for (int tc = 1; tc <= T; tc++) {
			
			st = new StringTokenizer(bf.readLine(), " ");
			
			n = Integer.parseInt(st.nextToken());// 수
			m = Integer.parseInt(st.nextToken());// 연산 수
			
			parents = new int[n + 1];// 부모기록.
			for (int i = 1; i <= n; i++) {
				parents[i] = i;
			}
			
			sb.append("#"+tc+" ");
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(bf.readLine(), " ");
				command = st.nextToken();
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				result = (union(a, b, command));
				if (command.equals("1"))
					sb.append(result);
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	private static int union(int a, int b, String command) { // 합한다. b가 -> a아래로 들어감.
		int aRoot = find(a);
		int bRoot = find(b);
		if (command.equals("0")) {
			parents[bRoot] = aRoot;
		}
		if (aRoot == bRoot) {
			return 1;
		}

		return 0;
	}

	private static int find(int a) { // 부모를 찾는다.
		if (a == parents[a])
			return a;
		return parents[a] = find(parents[a]);
	}

}
