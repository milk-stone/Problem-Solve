def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    # Total Seconds
    start_ts = h1 * 3600 + m1 * 60 + s1
    end_ts = h2 * 3600 + m2 * 60 + s2
    
    now = start_ts
    
    if start_ts == (12 * 3600) or start_ts == 0:
        answer += 1
    
    while now < end_ts:
#         curDegree_h = now / 120 % 360
#         curDegree_m = now / 10 % 360
#         curDegree_s = now * 6 % 360
        
#         nextDegree_h = 360 if (now + 1) / 120 % 360 == 0 else (now + 1) / 120 % 360
#         nextDegree_m = 360 if (now + 1) / 10 % 360 == 0 else (now + 1) / 10 % 360
#         nextDegree_s = 360 if (now + 1) * 6 % 360 == 0 else (now + 1) * 6 % 360
        
        curDegree_h = now % 43200 / 120
        curDegree_m = now % 3600 / 10
        curDegree_s = now % 60 * 6
        
        nextDegree_h = 360 if (now + 1) % 43200 / 120 == 0 else (now + 1) % 43200 / 120
        nextDegree_m = 360 if (now + 1) % 3600 / 10 == 0 else (now + 1) % 3600 / 10
        nextDegree_s = 360 if (now + 1) % 60  * 6 == 0 else (now + 1) % 60 * 6
        
        
        
        if curDegree_s < curDegree_h and nextDegree_s >= nextDegree_h:
            answer += 1
        if curDegree_s < curDegree_m and nextDegree_s >= nextDegree_m:
            answer += 1
        if nextDegree_h == nextDegree_m and nextDegree_m == nextDegree_s:
            answer -= 1
        
        now += 1
        
        
    return answer