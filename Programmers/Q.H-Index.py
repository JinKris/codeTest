def solution(citations):    
  for h in range(len(citations),0,-1):   
    hcnt = 0    
    for x in citations:
      if x >= h:
        hcnt=hcnt+1
    if hcnt >= h:
      return h
  return 0