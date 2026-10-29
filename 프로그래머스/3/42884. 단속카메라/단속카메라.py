def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 0
    prev = -1e9 #prev position
    for route in routes:
        s,e = route
        if prev<s:
            prev = e
            answer+=1
            
    return answer