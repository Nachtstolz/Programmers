# 기능개발 # 성공
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    answer = []

    q = deque(progresses)
    idx = 0 # speeds의 idx
    work = 0 # 작업수 저장

    while q :
        print(q)
        work = 0
        day = (100-q[0]) // speeds[idx]
        if (100-q[0]) % speeds[idx] > 0 :
            day+=1
        print(day)

        while q :
            print(q)
            if q[0]+speeds[idx]*day >= 100 :
                work+=1
                idx+=1
                q.popleft()
                continue
            break
        answer.append(work)

    print(answer)

    return answer