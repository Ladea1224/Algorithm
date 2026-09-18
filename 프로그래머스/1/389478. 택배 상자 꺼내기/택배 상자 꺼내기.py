def solution(n, w, num):
    answer = 0
    while True:
        print(num)
        answer += 1
        step = (w*((num//w)+1)-num)*2+1 if num%w!=0 else 1
        if(num+step>n): break
        num += step
        
    return answer