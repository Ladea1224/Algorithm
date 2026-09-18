#https://atcoder.jp/contests/abc026/tasks/abc026_c

"""

풀이 생각
1.재귀로 구하면 될거같다(시간 복잡도? 같은건 잘 모르겠는데 N<=20 이니까 아마 될거같다?)
2.그럼 탑다운 말고 바텀업(DP) 식으로도 되려나? 근데 거꾸로 생각하려니까 잘 모르겠어서 그냥 재귀로 해보자
3.짜던 중에: 혹시 money 계산한거 DP배열에 저장해둬야하나? -> 아니다 똑같은 부하 직원 안가지니까 중복해서 쓸 일 없겠구나

궁금한거
1.바텀업 방식 풀이 있는지, 뭐가 더 쉬운지?
2.이런 문제는 시간복잡도 같은거 안따져도 되나? 따져야되면 어떻게 생각해야되나?
"""
import sys
sys.setrecursionlimit(10**6)

def money(num):
    unders = under[num]
    if len(unders) == 0:
        return 1
    elif len(unders) == 1:
        return money(unders[0])*2 + 1
    else:
        moneys = [money(x) for x in unders]
        return min(moneys)+max(moneys)+1

n = int(input())
under = [ list() for _ in range(n+1)] #under[k] = k번 직원의 부하 직원 리스트
for i in range(2,n+1):
    k = int(input())
    under[k].append(i)

print(money(1))
