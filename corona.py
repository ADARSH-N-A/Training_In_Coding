n = int(input())
num = list(map(int, input().split()))
spike = int(input())
result = []
for i in range(len(num)):
  s = bin(num[i])[2:]
  if len(s) <= spike:
    result.append(0)
  else:
    r = s[:-spike]
    d = int(r,2)
    result.append(d)
print(*result)