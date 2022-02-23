def solution(brown, yellow):
    answer = []
    gridNum = brown + yellow
    
    for i in range(1,gridNum+1):
        if gridNum % i == 0:
            row = i
            col = int(gridNum/i)
            predictBrown = row*2 + col*2 -4
            
            if predictBrown == brown:
                answer.append(col)
                answer.append(row)
                break
    
    return answer