# 프로세스 # 성공
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42587

#import heapq
from collections import deque

def solution(priorities, location):
    answer = 1
    
    '''
    heap = []
    for i in range(len(priorities)) :
        heapq.heappush(heap, (-priorities[i], i))
        print(heap)
    while heap :
        tmp = heapq.heappop(heap)
        print(tmp)
        if tmp[1] == location :
            break
        answer+=1
        heap.append(tmp)
    '''
    
    q = deque([])
    for i in range(len(priorities)) :
        q.append((priorities[i], i))
    pri = max(priorities) # 이게 효율적일까...

    while q :
        tmp = q.popleft()
        # print(tmp)
        if tmp[0] == pri :
            if tmp[1] == location :
                break
            priorities.remove(tmp[0])
            pri = max(priorities)
            answer+=1
        else :
            q.append(tmp)
        # print(q)
    
    
    return answer