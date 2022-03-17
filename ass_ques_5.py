# question 5
p = int(input ("Enter number : "))
div_value = []
for i in range (1,p+1):
    if p%i ==  0:
        div_value.append(i)
print(div_value)
b = 0
for i in (div_value):
    b = b+i
print(b)