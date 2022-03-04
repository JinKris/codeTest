#스택
def solution(prices):
    answer = []

    for i in range(len(prices)):
        sum=0;
        for j in range(i+1,len(prices)):
            sum+=1
            if prices[i]>prices[j]:
                break
        answer.append(sum)    
    return answer