def compare(a,b):
  if a==b:
    return True
  else:
    return False

def solution(phone_book):
  phone_book.sort()
  for i in range(0,len(phone_book)-1):
    a = phone_book[i]
    b = phone_book[i+1]
    if( compare(a,b[0:len(a)]) ):
      return False
      
  return True