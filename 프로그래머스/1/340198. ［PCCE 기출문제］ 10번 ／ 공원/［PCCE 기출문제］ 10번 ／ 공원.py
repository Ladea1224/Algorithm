def solution(mats, park):
    answer = -1
    row,col = len(park),len(park[0]) #6,8
    
    for mat in mats:
        for x in range(row-mat+1):
            for y in range(col-mat+1):
                if all(park[x+i][y+j]=="-1" for i in range(mat) for j in range(mat)):
                    answer = max(answer,mat)
        
    return answer


"""
def solution(mats, park):
    answer = -1
    row,col = len(park),len(park[0]) #6,8
    
    for mat in mats:
        if any(all(park[x+i][y+j]=="-1" 
                    for i in range(mat) 
                    for j in range(mat)
                  ) for x in range(row-mat+1) 
                    for y in range(col-mat+1)
            ):
            answer = max(answer,mat)
        
    return answer
"""
