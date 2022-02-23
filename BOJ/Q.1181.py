a = int(input())
array = []
for i in range(a):
  x = input()
  array.append(x)

array = list(map(lambda x:[len(x),x],set(array)))
answer = list(map(lambda x:x[1] ,sorted(array)))

for i in answer:
  print(i)
