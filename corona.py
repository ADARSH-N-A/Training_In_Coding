n = int(input())
num = list(map(int, input().split()))
spike = int(input())
for i in range(n-1,-1,-1):
  if spike == 0:
    num[i] = 0
  else:
    num[i] = 1
    spike -= 1
print(*num)