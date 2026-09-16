def solution(wallpaper):
    minR,minC,maxR,maxC = 100,100,0,0
    
    for i,row in enumerate(wallpaper):
        for j,element in enumerate(row):
            if element=="#":
                minR,minC,maxR,maxC = min(minR,i),min(minC,j),max(maxR,i),max(maxC,j)
                
    

    return [minR,minC,maxR+1,maxC+1]