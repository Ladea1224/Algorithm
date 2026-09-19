#재귀 테스트

cnt = 0
def test_recur(remain_sum):
    global cnt
    cnt += 1
    for i in range(1, 8):
        if remain_sum + i <= 8:
            test_recur(remain_sum + i)

test_recur(0)
print(cnt)
