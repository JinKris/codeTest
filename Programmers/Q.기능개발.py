#스택
import math
def calDay(a,b):
  return math.ceil((100-a)/b)

def solution(progresses, speeds):
  answer = []
  for i in range(0,len(progresses)):
    progresses[i]=[progresses[i],calDay(progresses[i],speeds[i])]

  cnt = 1;
  standard = progresses[0][1]
  for i in range(1,len(progresses)):
    if standard < progresses[i][1]:
      answer.append(cnt)
      standard = progresses[i][1]
      cnt=1
    else:
      cnt+=1
  answer.append(cnt)
  return answer