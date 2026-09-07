import statistics as st
n1 = int(input())
n2 = int(input())
result = []
num1 = set(map(int, input().split()))
num2 = set(map(int, input().split()))

result = sorted(list(num1) + list(num2))
print(st.median(result))