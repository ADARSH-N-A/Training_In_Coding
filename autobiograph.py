def autobiograph(s):
  freq = {}
  count_list = []
  count_set = set()
  i = 0
  for ch in s:
    freq[i] = s.count(str(i))
    i += 1
  for key in freq:
    count_list.append(freq[key])
  count_set = set(count_list)
  print(len(count_set))



s = input("Enter a string:")
autobiograph(s)
