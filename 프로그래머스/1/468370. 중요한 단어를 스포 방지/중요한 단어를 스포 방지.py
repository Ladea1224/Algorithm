opened = set()
hidden = []
secret = set()

     
def solution(message, spoiler_ranges):
    ws,we = 0,0
    for word in message.split():
        #단어 범위 구하기
        t = ws
        while(t+1 < len(message) and message[t+1]!=" "): t+=1
        we = t
        
        #단어 범위가 스포방지 범위인지 확인 
        isHidden = False
        for ss,se in spoiler_ranges:
            if not (se<ws or ss>we):
                isHidden = True
                break
                
        #확인 결과에 따라 추가
        if(isHidden):
            hidden.append(word)
        else:
            opened.add(word)
            
        #다음 단어로 이동
        ws = we+2
            
    #중요 단어인지 확인
    answer = 0
    for word in hidden:
        if (word in opened) or (word in secret):
            continue
        answer += 1
        secret.add(word)

    return answer