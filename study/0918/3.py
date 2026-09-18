#https://atcoder.jp/contests/adt_all_20240320_1/tasks/abc268_d
from itertools import permutations
import sys
sys.setrecursionlimit(10**6)

"""
일단 다 만들어본다고 생각하면? 
-> 가능한 경우 개수 세는건 쉽겠다, 그럼 T랑 개수 비교로?  
-> 아 근데 마지막 예제 보니까 T 개수가 뻥튀기 될수 있어서 이걸론 안되려나 
-> 8글자 7공간이 제일 많나? 아니네 이건 오히려 금방 끝이네, 공간에 _ 하나 이상 필수니까. 그럼..
-> 4글자 3공간, 3공간에 12개 _ 자유롭게 분배.. 이거도 dfs식으로 다 해보고 비교해야 하는건가? N도 작기도하고...   
T를 set으로 해놓으면 in으로 검색하는거 O(1) 에 가능할거고, 
모든 경우 만들어보면서 T에 있나 찾아보기, 없으면 프린트하고 종료, 못찾으면 -1, 이런 느낌으로 구현하면 되는건가..진짜 그건가? 뭔가 다른방법없나? 근데 T 배열 개수 조작 가능하고 뭐있을지 전혀모른다는점이 너무 결정적이다.. 그래서 결국 다 dfs로 돌려보는거 말곤 없지않나.

구현:
어떻게 할까.. 어차피 in으로 직접 비교해야하니까 꼼수부리지말고 앞에서부터 글자 붙여나가는 방식이 맞는것같다
근데 글자만 permutation 도는거면 몰라도 언더바 개수까지 유동적으로 변하니까 어떻게 해야할지 좀 어렵네

1.일단 단어 permutation 박는다(순서있음)
2.각 사이에 _ 하나는 필수로 박는다
- 이게 기본, 이때 글자수 초과하면 불가능이므로 -1 반환
3.각 사이에 남은 _를 분배한다
- 순서있음, 다 안써도 됨, ...

1,2까진 할수있을거같은데 3이 ...
0개썼을때, 1개썼을떄, 2개썼을떄, ... , 남은거 다 썼을때 이렇게 반복?

아니면 분배한다 라는 관점이 잘못됐나? 분배가 아니라 앞에서부터 _ 개수 정하면서 순서대로 박아넣으면서 들어가야하나? 

아 그게맞네. 재귀 타고 들어가면서 0,0,0/ 0,0,1, .../ 0,0,9 까지 하고 
다음 나와서 0,1,0, /0,1,1, /... 이런식으로 . 

구현:
글자 직접 박으면서 만들려니까 햇갈린다
그냥 _ 개수의 관점에서 구현하고, 갖추어지면 합쳐서 문자 만드는 방식으로 해보자.

일단 구현은 성공... 근데 WA랑 TLE 일부 있네
아니 찾앗는데도 다돌아보고 잇엇네..근데 이거때문에 TLE라 하기엔? 어차피 시간복잡도 따라 나오는거 아니려나?


 
"""

def rec(case,underbars):  # case = [ab,cd,ef,gh]
    #이미 발견
    global flag
    if flag: return

    #글자 수 초과
    if len("".join(case))+sum(underbars) > 16:
        return

    #문자 만들고 확인
    if len(underbars) == len(case)-1:
        result = ""
        for i in range(len(case)-1):
            result += case[i]
            result += "_" * underbars[i]
        result += case[-1]

        if(result not in T):
            print(result)
            flag = True
            return
        else:
            return
    
    for i in range(1,17-len("".join(case))): #case 글자 길이가 8이면, _의 합은 16-8 = 8 을 넘을 수 없다, 즉 _ 하나는 8보다 반드시 작거나 같다. (처음엔 대충 16 잡았는데 시간초과 때문에 수정해봄)  
        underbars.append(i)
        rec(case,underbars)
        underbars.pop()

N,M = map(int,input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

flag = False
for case in permutations(S):  # case = (ab,cd,ef,gh),  최대 8!= 4* 10^4 가지
    rec(list(case),[]) #dfs, 재귀는 시간 복잡도 잘 가늠이 안된다..
    if flag: break

if not flag: print(-1)

