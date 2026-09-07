d = int(input())
result = ""
b = bin(d)[2:]
for ch in str(b):
  if ch == "0":
    result += "1"
  else:
    result += "0"
d = str(result)
print(int(d,2))