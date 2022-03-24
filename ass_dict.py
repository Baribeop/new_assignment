### if the person is female and white increase by 20%
# wrote for 'if female and black increase by 20%', since there is no female of white origin

data = [{"name":"jane", "sex":"female", "origin":"black", "age":27, "salary": 40},
        {"name":"frank", "sex":"male", "origin":"white", "age": 30, "salary": 50},
        {"name":"kate", "sex":"female", "origin":"caucasian", "age":27, "salary": 44}]
for n in data:

 if n["sex"] == "female" and n["origin"] == "black":  
  n["salary"] = 1.2*n["salary"]
  print(n)
