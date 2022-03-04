import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(scoville[0] < K): #최소값이 < k 일경우
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer+=1
        
        if len(scoville)==1 and scoville[0] < K :
            return -1
        
    return answer