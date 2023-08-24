# [Gold III] 가스관 - 2931 

[문제 링크](https://www.acmicpc.net/problem/2931) 

### 성능 요약

메모리: 12996 KB, 시간: 88 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>러시아 가스를 크로아티아로 운반하기 위해 자그레브와 모스코바는 파이프라인을 디자인하고 있다. 두 사람은 실제 디자인을 하기 전에 파이프 매니아 게임을 이용해서 설계를 해보려고 한다.</p>

<p>이 게임에서 유럽은 R행 C열로 나누어져 있다. 각 칸은 비어있거나, 아래 그림과 같은 일곱가지 기본 블록으로 이루어져 있다.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="" style="width: 37px; height: 59px;"></td>
			<td><img alt="" src="" style="width: 64px; height: 59px;"></td>
			<td><img alt="" src="" style="width: 58px; height: 59px;"></td>
			<td><img alt="" src="" style="width: 46px; height: 59px;"></td>
			<td><img alt="" src="" style="width: 45px; height: 59px;"></td>
			<td><img alt="" src="" style="width: 45px; height: 59px;"></td>
			<td><img alt="" src="" style="width: 45px; height: 59px;"></td>
		</tr>
		<tr>
			<td>블록 '<code>|</code>'</td>
			<td>블록 '<code>-</code>'</td>
			<td>블록 '<code>+</code>'</td>
			<td>블록 '<code>1</code>'</td>
			<td>블록 '<code>2</code>'</td>
			<td>블록 '<code>3</code>'</td>
			<td>블록 '<code>4</code>'</td>
		</tr>
	</tbody>
</table>

<p>가스는 모스크바에서 자그레브로 흐른다. 가스는 블록을 통해 양방향으로 흐를 수 있다. '<code>+</code>'는 특별한 블록으로, 아래 예시처럼 두 방향 (수직, 수평)으로 흘러야 한다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 253px; height: 158px;"></p>

<p>파이프 라인의 설계를 마친 후 두 사람은 잠시 저녁을 먹으러 갔다. 그 사이 해커가 침임해 블록 하나를 지웠다. 지운 블록은 빈 칸이 되어있다.</p>

<p>해커가 어떤 칸을 지웠고, 그 칸에는 원래 어떤 블록이 있었는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 유럽의 크기 R과 C가 주어진다. (1 ≤ R, C ≤ 25)</p>

<p>다음 R개 줄에는 C개 글자가 주어지며, 다음과 같은 글자로 이루어져 있다.</p>

<ul>
	<li>빈칸을 나타내는 '<code>.</code>'</li>
	<li>블록을 나타내는 '<code>|</code>'(아스키 124), '<code>-</code>','<code>+</code>','<code>1</code>','<code>2</code>','<code>3</code>','<code>4</code>'</li>
	<li>모스크바의 위치를 나타내는 '<code>M</code>'과 자그레브를 나타내는 '<code>Z</code>'. 두 글자는 한 번만 주어진다.</li>
</ul>

<p>항상 답이 존재하고, 가스의 흐름이 유일한 경우만 입력으로 주어진다, 또, 모스크바와 자그레브가 하나의 블록과 인접해 있는 입력만 주어진다. 또, 불필요한 블록이 존재하지 않는다. 즉, 없어진 블록을 추가하면, 모든 블록에 가스가 흐르게 된다.</p>

### 출력 

 <p>지워진 블록의 행과 열 위치를 출력하고, 어떤 블록이었는지를 출력한다.</p>

