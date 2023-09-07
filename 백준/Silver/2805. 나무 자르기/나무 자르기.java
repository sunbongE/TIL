import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 
 * @author 박태호
 * <pre>
 * 풀이
 * 이분탐색
 * 1. 입력 받으면서 최대값과 최소값을 찾는다.
 * 2. 배열에 있는 수를 정렬한다. 안해도 될듯.
 * 
 * 3. while(s>=e):
 * 4. mid = (s+e)/2 중간값 설정
 * 5. 중간값으로 모든 나무를 순회하면서 mid보다 크면 그 차이를 tmp값에 더해주고
 * 6. 만약 tmp가 M보다 작거나 같으면 출력하고 
 * 7. 아니면 s=mid+1
 * </pre>
 *
 */
public class Main {
	static int N,M,trees[];
	static long result;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(bf.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		trees = new int[N];
		
		long e=-1;
		st = new StringTokenizer(bf.readLine()," ");
		int in;//  입력값, 최소, 최대값
		for (int i = 0; i < trees.length; i++) {
			in = Integer.parseInt(st.nextToken());
			trees[i] = in;
			if(in>e)e=in;
		}
		long s=1;
		long mid;
		
		while(s<=e) {
			result=0;
			mid = (s+e)/2; //  중간값
			for (int tree : trees) {
				result+=Math.max(0, tree-mid);
			}
			if(result>=M) {
				s = mid+1;
			}else {
				e = mid-1;
			}
		}
		System.out.println(e);
	}

}
