# #star는 각각 숫자 하나를 고른다 .
# #앞에서 골라야 뒤에 영향이 없으므로 가장 좋다.
# #그게 안될 경우 뒤를 보고 고르는게 최선이다.
# #--------------------
# #다시 생각해보니 단순히 많으면 되는게 아니다.. 연속해서 붙어있으면 안됨. ex) 12121000000001
# #00000... 같은건 00, 즉 2개로 세야 함
# #-------------------
# #근데 523353 에서 3을 3개로 세면 안되지않나? 2개로 세야 하지 않나?
# #-> 121233533533121212 의 경우 - 1은 5개에 5쌍, 3은 6개에 4쌍. 즉 353 같은 상황 하나당 하나씩 줄어듬
# #문제가 되는 상황 = 가운데 하나밖에 없다 & 양쪽 다 바깥에서는 못고른다
# #-> 이거만 해결하면 그게 곧 쌍의 수 ? 
# #-----------


# from collections import Counter
# def solution(a):
#     cnt = Counter()
    
#     #처음
#     if len(a)>=2 and a[0]!=a[1]:
#         cnt[a[0]]+=1
    
#     #중간
#     for i,num in enumerate(a):
#         if i==0 or i==len(a)-1: continue # 따로 계산
        
#         if a[i]!=a[i-1] or a[i]!=a[i+1]:
#             cnt[a[i]]+=1
            
#         if a[i-1]==a[i+1]:
#             if (i-1==0 or a[i-1]==a[i-2]) and (i+1==len(a)-1 or a[i+1]==a[i+2]):
#                 cnt[a[i-1]]-=1
                
#     #끝
#     if len(a)>=2 and a[-1]!=a[-2]:
#         cnt[a[-1]]+=1
        
#     answer = cnt.most_common(1)[0][1]*2 if cnt else 0
#     print(answer)
    
#     return answer
    

from collections import Counter

def solution(a):
    answer = 0
    counts = Counter(a)

    for x, count in counts.items():
        # x가 등장하는 횟수보다 많은 쌍은 만들 수 없음
        if count * 2 <= answer:
            continue

        pairs = 0
        i = 0

        while i < len(a) - 1:
            # 서로 다른 숫자이며 x가 포함된 쌍
            if a[i] != a[i + 1] and (a[i] == x or a[i + 1] == x):
                pairs += 1
                i += 2
            else:
                i += 1

        answer = max(answer, pairs * 2)

    return answer

    