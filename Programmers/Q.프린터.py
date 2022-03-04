#deque
from collections import deque

def solution(priorities, location):
  answer = 0
  que = deque()
  arr = [] # 순서대로..
  stack = sorted(priorities) 
  for i in range(0,len(priorities)):
    que.append([priorities[i],i])
  item = que[location] 

  while(len(que)!=0):
    x = que.popleft()
    if( x[0] < stack[-1]):
      que.append(x)
    else:
      arr.append(x)
      stack.pop()

  answer = arr.index(item)+1
  return answer