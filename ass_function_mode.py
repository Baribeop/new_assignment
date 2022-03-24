# A program to find the mode of numbers in any array
data = [5, 6, 4, 7, 3, 6, 5, 5, 8, 9]
k = {}
for i in data:
 k[i] = k.get(i,0) + 1
print(k)
data_val = []
frequence_val = []
for m, n in k.items():
 data_val.append(m)
 frequence_val.append(n)
print(data_val)
print(frequence_val)
d = frequence_val[0]
for g in frequence_val:
  if g > d:
    d = g
for x, y in k.items():
  if y == d:
   modal_value = x
   print(f"The mode is {modal_value}")