import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int ans = 0, N, M;
	static boolean flag, v[];
	static ArrayList<Integer>[] list;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		// 만들 수 있는 친구 다 만듬.
		list = new ArrayList[N];
		for (int i = 0; i < N; i++) {
			list[i] = new ArrayList<Integer>();
		}

		int a, b;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(bf.readLine(), " ");
			// 친구 관계 입력.
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			list[a].add(b);
			list[b].add(a);

		}

		for (int i = 0; i < N; i++) {
			v = new boolean[N]; // 친구들 방문상황.
			flag = false;
//			System.out.println();
			dfs(1, i);
			if (flag) {
				break;
			}
		}
		System.out.println(ans);

	}

	private static void dfs(int n, int f) {
//		System.out.println(n+" "+f);
		if (flag) {
			return;
		}
		v[f] = true;
		if (n == 5) {
			ans = 1;
			flag = true;

			return;
		}
		// 방문체크
		for (Integer nf : list[f]) {
			if (!v[nf]) {
				dfs(n + 1, nf);
				if (flag)
					break;
			}
		}
		v[f] = false;

	}
}
