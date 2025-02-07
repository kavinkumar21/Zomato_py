#Zomato App for ordering food
from random import *

class Zomato:
    def __init__(self):
        self.count=0
        self.price=0
        self.a=0
        self.b=0
        self.c=0
        self.d=0
    def parota(self, price):
        while True:
            Par=price*25
            print(f'Price of your order is {Par}')
            con=input('Type yes - conformation \n     add - adding more items \n     no -  cancel this selected item ')   
            con.lower()
            if con=='yes':
               print('You confirmed the order')
               self.a+=self.price
            #    print(f'Your OTP -- {self.otp()}')
               self.otp()
               self.bill()
               break
            elif con=='add':
                print('\nAdd new items to order -')
                self.order()
            elif con=='no':
               self.price-=Par
               self.a-=price
               print('Order Cancelled')
               self.order()
            else:
                print('Enter valid data')
                self.order()

    def poori(self,price):
        while True:
            Par=price*20
            self.price+=Par
            print(f'Price of your order is {Par}')
            con=input('Type yes - conformation \n     add - adding more items \n     no -  cancel this selected item ')   
            con.lower()
            if con=='yes':
               print('You confirmed the order')
               self.b+=price
            #    print(f'Your OTP -- {self.otp()}')
               self.otp()
               self.bill()
               break
            elif con=='add':
                print('\nAdd new items to order -')
                self.order()
            elif con=='no':
               self.price-=Par
               self.b-=self.price
               print('Order Cancelled')
               self.order()
            else:
                print('Enter valid data')     
                self.order() 

    def pongal(self,price):
        while True:
            Par=price*35
            print(f'Price of your order is {Par}')
            con=input('Type yes - conformation \n     add - adding more items \n     no -  cancel this selected item ')   
            con.lower()
            if con=='yes':
               print('You confirmed the order')
               self.c+=self.price
               self.otp()
               self.bill()
               break
            elif con=='add':
                print('\nAdd new items to order -')
                self.order()
            elif con=='no':
               self.price-=Par
               self.c-=price
               print('Order Cancelled')
               self.order()
            else:
                print('Enter valid data')
                self.order()             
    
    def briyani(self,price):
        while True:
            Par=price*120
            self.aa=price
            print('\n')
            print(f'Price of your order is {Par}')
            con=input('Type yes - conformation \n     add - adding more items \n     no -  cancel this selected item ')   
            con.lower()
            if con=='yes':
               print('You confirmed the order')
               self.d+=price
               self.price+=price
               self.otp()
               self.bill()
               break
            elif con=='add':
                print('\nAdd new items to order -')
                self.order()
            elif con=='no':
               self.price-=Par
               print('Order Cancelled')
               self.order()
            else:
                print('Enter valid data')          
                self.order()

    def bill(self):
        while True:
         if self.a!=0 or self.b!=0 or self.c!=0 or self.d!=0:
            print('\n')
            print('  - -  Your Bill - -')
            if self.a!=0:  
                print(f'   {self.a} Parota  Rs {self.a*25}')  
            self.poor(self.b)
            self.pon(self.c)
            self.bri(self.d)
            at=self.a*25
            bt=self.b*20
            ct=self.c*35
            dt=self.d*120
            print(' ---- Total - ',at+bt+ct+dt,'----')
            break

    def poor(self,que):
        if self.b!=0:
                print(f'   {que} Poori   Rs {que*20}')   

    def pon(self,que):
            if self.c!=0:
                print(f'   {que} Pongal  Rs {que*35}')

    def bri(self,que):
            if self.d!=0:
                print(f'   {que} Briyani Rs {que*120}')
            
    def otp(self):
           l=[1,2,3,4,'a','b','c','!','@','#','$','%','&','*']
           print('Your OTP --')
           for i in range(5):
              print(choice(l),end='')    
    def order(self):
        while True:
            if self.count==0:
               print('\n   - - Welcome to Zomato - -\n')
               self.count=1
            print('Order price ',self.price)
            print('        Items      Price')
            print('\n  1    Barota     Rs- 25 per Pair')
            print('  2    Poori      Rs- 20 per Pair')
            print('  3    Pongal     Rs- 35')
            print('  4    Briyani    Rs- 120')
            print('\n0 for Quit')
    
            num=int(input('Enter the item no '))
            if num==1:
                print('You have choosen Barota')
                pquan=int(input('Enter the quantity '))
                self.a+=pquan
                self.parota(pquan)
                break
                
            elif num==2:
                print('You have choosen Poori')
                poquan=int(input('Enter the quantity '))
                self.b+=poquan
                self.poori(poquan)
                break
                
            elif num==3:
                print('You have choosen pongal')
                plquan=int(input('Enter the quantity '))
                self.c+=plquan
                self.pongal(plquan)
                break

            elif num==4:
                print('You have choosen Briyani')
                bquan=int(input('Enter the quantity '))
                self.d+=bquan
                self.briyani(bquan)
                break

            elif num==0:
                print('Thank you')
                break
            else:
                print('\nEnter valid No')
ob=Zomato()
ob.order()
