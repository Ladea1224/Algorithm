def ts(pos):
    minu,sec = map(int,pos.split(":"))
    return minu*60 + sec
    
def solution(video_len, pos, op_start, op_end, commands):
    #초 변환
    tsPos = ts(pos)
    tsStart = ts(op_start)
    tsEnd = ts(op_end)
    #오프닝 스킾
    if tsStart<= tsPos <= tsEnd:
        tsPos = tsEnd
    for command in commands:
        #커맨드 수행
        if command == "prev":
            tsPos = max(0,tsPos-10)
        if command == "next":
            tsPos = min(ts(video_len),tsPos+10)
        #오프닝 스킾
        if tsStart<= tsPos <= tsEnd:
            tsPos = tsEnd
    #포맷팅
    pos = ("0" if tsPos//60 <10 else "") + str(tsPos//60) + ":" + ("0" if tsPos%60 <10 else "") + str(tsPos%60)
    return pos