
import math,random
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4

#######Function_1######
#This function contain lambda expression

#@decorator_4
#@decorator_1
#@decorator_2
#@decorator_3
def fun1(n):
  '''This function contain lambda expression and returns triple'''
  fun1= lambda a : a * n
  triple=fun1(3)   
  print( triple)

#######Function_2######
#@decorator_4
#@decorator_1
#@decorator_2
#@decorator_3
def fun2(lis):
  '''Program to filter out only the even items from a list'''
  new_lis = list(filter(lambda x: (x%2 == 0) , lis))
  print(new_lis)

#print(fun2([1, 5, 4, 6, 8, 11, 3, 12]))


#######Function_3######
#@decorator_4
#@decorator_1
#@decorator_2
#@decorator_3
def fun3(a,b,c):

  '''Solve the quadratic equation'''
  d = (b**2) - (4*a*c)

  # find two solutions
  sol1 = (-b-math.sqrt(d))/(2*a)
  sol2 = (-b+math.sqrt(d))/(2*a)
  print( sol1 ,sol2)


#######Function_4######
  
#@decorator_4
#@decorator_1
#@decorator_2
@decorator_3
def fun4(n):
  '''print pascal traingle'''  
  top = [1]
  app_val=[0]
  result=[]
  for _ in range(n):
    result.append(top)
    top = [l + r for l,r in zip(top+app_val,app_val+top)]
  print( result)
		
		
if __name__=="__main__":
#  fun1(4)
 # fun2([1,2,3,4,5,6,10])
  #fun3(2,6,1)
  fun4(100)
