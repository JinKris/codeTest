def solution(numbers):
    answer = 0
    numArr = list(numbers) #['1','7']

    def isIn(num):# ex num : '11'
      ar = list(num) #['1','1']
      numArr2 = numArr[:] 
      for i in ar:
        if i not in numArr2:
          return False
        if i in numArr2:
          numArr2.remove(i)
      return True

    def isPrime(n):
      n = int(n)
      if n==1 or n==0 :
        return False
      for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
      return True

    max=int("".join(sorted(numArr,reverse=True)))
    
    # arr = ['0','1','2','3'...'71']
    arr = list(map(str,[i for i in range(max+1)]))
    # arr2 = ['1',7','17','71']
    arr2 = list(filter(isIn,arr))
    # arr3 = ['7','17','71']
    arr3 = list(filter(isPrime,arr2))
    answer = len(arr3)
    return answer