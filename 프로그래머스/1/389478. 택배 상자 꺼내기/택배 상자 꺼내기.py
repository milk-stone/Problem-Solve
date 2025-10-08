def solution(n, w, num):
    answer = 0
    
    mulc = 1
    index = 1
    curNum = 1
    
    stacks = [[] for _ in range(w + 1)]
    
    targetStackNum = -1
    
    while curNum <= n:
        stacks[index * mulc].append(curNum)
        
        if curNum == num:
            targetStackNum = index * mulc
        if index % w == 0:
            mulc *= -1
            index = 0
        index += 1
        curNum += 1
    
    lenTarget = len(stacks[targetStackNum])
    for i in range(lenTarget):
        if stacks[targetStackNum][i] == num:
            return lenTarget - i
    
    return answer