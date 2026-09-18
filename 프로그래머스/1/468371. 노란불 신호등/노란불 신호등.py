import math
def solution(signals):
    answer = 0

    #모든 수의 최소 공배수 구하기(최소 공배수 = 주기)
    seconds = []
    for case in signals:
        seconds.append(sum(case))
    lcm = math.lcm(*seconds)

    #각 case 에서 노란불 표시(1~lcm 까지)
    yellow = [0]*(lcm+1)
    for case in signals:
        s = case[0]+1  #노란불 표시 시작 지점
        cycle = sum(case)

        while s<=lcm:
            for p in range(s,s+case[1]):
                if p>lcm: break
                yellow[p] += 1
            s += cycle

    #yellow 에 신호등 수만큼 표시된 첫번째 지점 = 정답
    for i in range(1,lcm+1):
        if yellow[i] == len(signals):
            return i

    return -1