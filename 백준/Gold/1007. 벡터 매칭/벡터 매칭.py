import sys
import math
from itertools import combinations

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dots = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 모든 점의 x, y 좌표 총합을 미리 구함
    total_x = sum(dot[0] for dot in dots)
    total_y = sum(dot[1] for dot in dots)
    
    min_dist = float('inf')
    
    # 2. N개의 점 중 뺄 점(N/2 개)을 선택하는 모든 조합
    # (효율성을 위해 dots[0]는 무조건 더하는 쪽으로 빼두고 조합을 짜도 되지만, 
    # 파이썬 combinations는 N=20일 때(184,756개)도 충분히 빠르므로 그냥 돌려도 통과합니다)
    for minus_dots in combinations(dots, N // 2):
        # 뺄 점들의 x, y 합
        minus_x = sum(dot[0] for dot in minus_dots)
        minus_y = sum(dot[1] for dot in minus_dots)
        
        # 3. 벡터의 합 = Total - 2 * (뺄 점들의 합)
        cur_x = total_x - 2 * minus_x
        cur_y = total_y - 2 * minus_y
        
        # 4. 최솟값 갱신 (math.hypot이 빠르고 정확함)
        dist = math.hypot(cur_x, cur_y)
        if dist < min_dist:
            min_dist = dist
            
    print(min_dist)