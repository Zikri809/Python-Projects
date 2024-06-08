from decimal import Decimal, getcontext


class numdecimal:
   def __init__(self, num, n):
     self.num = num
     self.n = n


   def decimal(self):
      getcontext().prec =self.n
      number=self.num
      statement=print (self.num,'to',self.n,'decimal places is :',number)
      return statement
      
status=True
while status==True:
   print('\n\n\nThis system outputs number to the nth decimlas of your likng')
   num=Decimal('22')/Decimal('7')
   n=int(input('Enter the decimal places of your choice : '))
   a=numdecimal(num,n)
   a.decimal()
   statuschar=input('wanted to repeat (t/f) :')
   if statuschar=='t':
      status=True
   else:
      status=False
      print('Thanks For Using My Service\n\n\n')    