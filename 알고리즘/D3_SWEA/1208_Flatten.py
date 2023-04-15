for _ in range(10):
    dump = int(input())
    h_list = list(map(int, input().split()))
    ans = 0
    while dump:
        min_num = min(h_list)
        max_num = max(h_list)
        if max_num - min_num <= 1:  # 미리 종료된 상황
            ans = max_num - min_num
            print(f"#{_+1} {ans}")
            break

        max_num = h_list.pop(h_list.index(max_num)) - 1
        min_num = h_list.pop(h_list.index(min_num)) + 1
        h_list.extend([max_num, min_num])
        dump -= 1
    else:
        ans = max(h_list) - min(h_list)
        print(f"#{_+1} {ans}")
