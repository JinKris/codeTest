def solution(numbers, target):
    cnt = 0
    
    def dfs(numbers,target,idx=0):
        if idx < len(numbers):
            numbers[idx] *= 1
            dfs(numbers,target,idx+1)
        
            numbers[idx] *= -1
            dfs(numbers,target, idx+1)
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1
    dfs(numbers,target)

    return cnt