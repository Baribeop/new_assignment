

a = [["names", "Eng", "Math", "chemistry"], 
["jude", 70, 90, 80],
["kate", 50, 60, 90], 
["caleb", 90, 77, 70]]

def subject_average(array, subject):
     u = []
     for l in range(0, len(array)):
          y =[]
          for i in array:
               y.append(i[l])
          u.append(y)
     for k in u:
          if subject in k:
               b = k[1:]
     total = 0
     for m in b:
          total += m
     average = round(total/len(b), 2)
     return average

d = subject_average(a, 'Eng')
print(d)

aa = int(input('Enter value: '))
ab = int(input('Enter value: '))
ac = int(input('Enter value: '))
ad = int(input('Enter value: '))
ae = int(input('Enter value: '))
af = int(input('Enter value: '))
ag = int(input('Enter value: '))
data = [aa, ab, ac, ad, ae, af, ag]

def modal_value(array):
     x = {}
     for i in array:
          x[i] = x.get(i,0) + 1
     value = []
     frequency = []
     for j,k in x.items():
          value.append(j)
          frequency.append(k)
     d = frequency[0]
     for e in frequency:
          if e > d:
               d = e
     for g,h in x.items():
          if h == d:
               return g

v = modal_value(data)
print(v)