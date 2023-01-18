import heapq
import sys  
input = sys.stdin.readline

N=int(input())
card_deck = []

for _ in range(N):
    heapq.heappush(card_deck, int(input()))

if len(card_deck) == 1:
    print(0)
else:
    answer = 0
    while len(card_deck) > 1:
        temp1 = heapq.heappop(card_deck)
        temp2 = heapq.heappop(card_deck)
        answer += temp1 + temp2
        heapq.heappush(card_deck,temp1 + temp2)
    print(answer)