import random

def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

p = 7
q = 9
m = p * q
random.seed()
s = random.randint(1, m-1)

while(compute_lcm(m, s) != 1):
    s = random.randint(1, m-1)

print(m, s)




