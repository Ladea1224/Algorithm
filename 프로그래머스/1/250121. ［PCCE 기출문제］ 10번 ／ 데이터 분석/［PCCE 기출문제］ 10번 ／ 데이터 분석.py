def solution(data, ext, val_ext, sort_by):
    dict = {"code":0, "date":1, "maximum":2, "remain":3} 
    
    answer = [dt for dt in data if dt[dict[ext]]<val_ext]
    answer.sort(key=lambda x: x[dict[sort_by]])
            
    return answer