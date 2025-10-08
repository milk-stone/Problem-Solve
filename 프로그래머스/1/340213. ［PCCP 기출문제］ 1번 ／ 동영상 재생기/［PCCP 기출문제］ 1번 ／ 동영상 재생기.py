def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    minuteList = []
    for item in [video_len, pos, op_start, op_end]:
        itemList = item.split(":")
        minuteList.append(int(itemList[0]) * 60 + int(itemList[1]))
    
    video_len, pos, op_start, op_end = minuteList
    
    if op_start <= pos <= op_end:
        pos = op_end
    for command in commands:
        if command == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
        elif command == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        if op_start <= pos <= op_end:
            pos = op_end
    print(minuteList)
    print(pos//60, pos%60)
    
    answer = ""
    
    if 0 <= (pos//60) <= 9:
        answer += '0'
    answer += str(pos//60)
    answer += ":"
    
    if 0 <= (pos%60) <= 9:
        answer += '0'
    answer += str(pos%60)
    return answer