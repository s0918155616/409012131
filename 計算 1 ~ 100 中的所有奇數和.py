(A1)
sum = 0 
for x in range(1, 101): 
   if x % 2 != 0:
    sum = sum + x 
   
print(sum) 




(A2)
sum = 0 
for x in range(1, 101): 
    if x % 2 == 0:
       continue
    sum = sum + x 
   
print(sum)





(A3)
sum = 0 
for x in range(1, 101,2): 
    sum = sum + x 
   
print(sum)