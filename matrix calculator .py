print()                                     
print('                     **MATRIX CALCULATOR**                 ')
print()
n=int(input('Enter number of rows/columns for the square matrix:'))
print()
while True:
  print('OPERATIONS MENU')
  print('1. Addition')
  print('2. Substraction')
  print('3. multiplication')
  print('4. Exit')
  print()    
  matrix_1=list()
  matrix_2=list()
  m=int(input('Enter option number:'))
  if m>=4 or m<0:
    print('EXIT,SORRY :)')
    break
  for i in range(1,3):
    for j in range(1,n+1):  
       print('Enter values for matrix',i,'row',j,'seperated by commas:',end="")
       values=input()
       lvalues=values.split(',')
       if len(lvalues)==n:
         if i==1:
           matrix_1.append(lvalues)
         if i==2:
           matrix_2.append(lvalues)
  result=[] 
  for i in range(1,n+1): 
      f=[]
      result.append(f)
      for j in range(1,n+1):
          f.append(0)
  if m==1: 
    for i in range(len(matrix_1)):
      for j in range(len(matrix_1)):
         result[i][j]=int(matrix_1[i][j]) + int(matrix_2[i][j])
    print('YOUR ANSWER:')
    for i in result:
       for k in i:
          print(k,"\t",end="")
       print()
    print()
  if m==2:
    for i in range(len(matrix_1)):
      for j in range(len(matrix_1)):
        result[i][j]=int(matrix_1[i][j]) - int(matrix_2[i][j])
    print('YOUR ANSWER:')
    for i in result:
       for k in i:
          print(k,"\t",end="")
       print()
    print()
  if m==3:
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result[i][j]+=int(matrix_1[i][k]) * int(matrix_2[k][j])
    print('YOUR ANSWER:')
    for i in result:
       for k in i:
          print(k,"\t",end="")
       print()
    print()
  


      
 
   

  

       
       
       
 


 
