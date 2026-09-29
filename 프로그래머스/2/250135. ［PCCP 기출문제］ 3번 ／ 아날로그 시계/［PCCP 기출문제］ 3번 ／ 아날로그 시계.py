"""
처음 시도: 전체 60개 좌표로 나누고, 연속인 경우(칸과 칸 사이에 위치한 경우)는 if문으로 처리하려 했으나, 결국 그 사이의 상태에 관한 정보도 필요하게 돼서 복잡해짐.

-> AI:전체 60개가 아니라 1초당 시침 움직이는 칸도 1칸 될 수 있도록 스케일링 해서 매번 상태 반영하도록 풀이 방향 수정(연속도 각 상태 세부적으로 나누면 상황따라 이산적으로 취급할 수 있다..)
"""
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    # 0시 0분 0초, 12시 0분 0초 정각 출발일 때 카운트
    if start == 0 or start == 12 * 3600:
        answer += 1
        
    for t in range(start, end):
        # 1. t초일 때의 위치 (720 스케일링)
        # 전체 한 바퀴가 43200이므로, 모듈러(%) 연산을 사용
        s_curr = (t % 60) * 720
        m_curr = (t % 3600) * 12
        h_curr = (t % 43200) * 1
        
        # 2. t+1초(다음 지점)일 때의 위치
        s_next = ((t + 1) % 60) * 720
        m_next = ((t + 1) % 3600) * 12
        h_next = ((t + 1) % 43200) * 1
        
        # 3. 59초 -> 0초로 넘어가는 순간의 보정 (크기 비교를 위해 0을 43200으로 취급)
        s_n = 43200 if s_next == 0 else s_next
        m_n = 43200 if m_next == 0 else m_next
        h_n = 43200 if h_next == 0 else h_next
        
        # 4. 현재는 뒤에 있었는데, 다음 초에 역전했는가?
        cross_m = (s_curr < m_curr) and (s_n >= m_n)
        cross_h = (s_curr < h_curr) and (s_n >= h_n)
        
        if cross_m and cross_h:
            # 시침, 분침을 동시에 역전했는데 셋이 정확히 한 점에서 만난 경우 (12시 정각 등)
            if s_n == m_n == h_n:
                answer += 1
            else:
                answer += 2
        elif cross_m or cross_h:
            answer += 1
            
    return answer