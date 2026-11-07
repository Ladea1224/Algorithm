# <<기둥,보 정보 저장된거 어떻게 쓰이는지 기준으로 -> 미리 전체 구조 잡고 코딩 했어야>>
# 즉 검증 때 (기둥,보 둘다) 있는지,없는지만 따지는게 전부이므로, 그냥 set에 x,y,a 로 넣어도 된다
# 그리고 n^2*row ~= 10^7 이므로 그냥 전체 검증 해도 됨.




# 설치 검증 각각 해야하나? if문 4개 써야하나? switch로 나눌까? 
    # 각각 안해도 됨. n^2*row ~= 10^7 이므로 그냥 전체 검증 해도 됨.
    # 따라서 동작 - 검증 - 취소 흐름으로만 나누면 된다. 즉 동작 구분하는 분기만. 기둥인지 보인지는 검증 부분에서 확인

# 기둥, 보 정보 저장 어떻게??/  한꺼번에 vs 따로/ set vs list
    # set으로 (x,y,a) 식으로 저장하면 따로 할 필요가 없고 접근도 O(1).
    # 반사적으로 따로 나누지말고, 항상 필요 따져보고 결정.

        
    
        
# x,y 좌표축 기준: 리스트 행,열과 혼동 주의. 

# 변수 scope 문제: solution 안인지 밖인지 주의.

# 0,1 뭐가 기둥인지 보인지 등 계속 혼동되므로 그냥 전역 변수 선언해서 명확히 하기(magic number 방지)

# or 줄바꿈: 괄호 안에서는 자유롭게 가능

GI, BO = 0, 1

def solution(n, build_frame):
    things = set()

    def can_gi(x, y):
        return (y == 0
            or (x, y, BO) in things
            or (x-1, y, BO) in things
            or (x, y-1, GI) in things
        )

    def can_bo(x, y):
        return ((x, y-1, GI) in things
               or (x+1, y-1, GI) in things
               or ( (x-1, y, BO) in things and (x+1, y, BO) in things )
               )
        
    def is_valid():
        for x, y, a in things:
            if a == GI:
                if not can_gi(x, y): return False
            elif a == BO:
                if not can_bo(x, y): return False
        return True

    for x, y, a, b in build_frame:
        if b == 0:
            things.remove((x, y, a))

            if not is_valid():
                things.add((x, y, a))

        else:
            things.add((x, y, a))

            if not is_valid():
                things.remove((x, y, a))

    return sorted(list(things))
