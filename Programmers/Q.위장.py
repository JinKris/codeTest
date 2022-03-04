from collections import Counter
def solution(clothes):
  answer = 1

#["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"] >> {headgear:2,eyewear:1} >> [2,1]
#closet = list(dict(Counter(x[1] for x in clothes)).values())
  closet = {}
  for i in clothes:
    if(closet.get(i[1])):
      closet[i[1]]+=1
    else:
      closet[i[1]]=1
  closet = list(closet.values())

  
  for i in closet:
    answer *= (i+1)
    
  return answer-1