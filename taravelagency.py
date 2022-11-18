import mysql.connector
from tabulate import tabulate

con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='travel',
)

class travel:
    
    def munnar(self):
        print("***********************************************************************************")
        print("Munnar 03 Days2 Nights/ 3 Days")
        print("***********************************************************************************")
        print("PLACES:-")
        print("Day 1 - Cochin to Munnar -140KM 4Hrs Drive")
        print("Day 2 - At Munnar ")
        print("Day 3 - Drop at Cochin")
        print("Hotel : Nishkara HOTEL")
        print("PACKAGE:10000")
        print("***********************************************************************************")

    def vietnam(self):
        print("***********************************************************************************")
        print("A Glimpse Of North Vietnam 3 Days")
        print("***********************************************************************************")
        print("PLACES:-")
        print("Day 1 - ARRIVAL")
        print("Day 2 - Ha Noi city tour full day ")
        print("Day 3 - Hanoi to Ha Long")
        print("Hotel : North Vietnam Barbara HOTEL")
        print("PACKAGE:17000")
        print("***********************************************************************************")

    def kullumanali(self):
        print("***********************************************************************************")
        print("Delhi Kullu Manali-03 Days")
        print("***********************************************************************************")
        print("PLACES:-")
        print("Day 1 - Delhi - Manali")
        print("Day 2 - Manali Local Sightseeing")
        print("Day 3 - Manali")
        print("Hotel : Kullu Manali zebran HOTEL")
        print("PACKAGE:12000")
        print("***********************************************************************************")

    def intro(self):
        print("***********************************************************************************")
        print("*                                                                                 *")
        print("*                         DP TRAVEL AGENCY TO EXPLORE WORLD                       *")
        print("*                                                                                 *")
        print("***********************************************************************************")
        print("1.Munnar")
        print("2.A Glimpse Of North Vietnam")
        print("3.Delhi Kullu Manali")
        print("----------------------------------------------------------------------------------")

    def signup(self):
        print("----------------------------------------------------------------------------------")
        print(" FOR SIGNUP:- ")
        print("----------------------------------------------------------------------------------")
        name=input("Enter Name:")
        mob=input("Enter Mobile Number:")
        mail=input("Enter Mail-ID:")
        print("----------------------------------------------------------------------------------")
        self.userinp={'name':name,'mob':mob,'mail':mail,}
        return self.userinp

    def payment(self,choice):
        if choice==1:
            count=int(input("Enter number of Persons:"))
            amount=count*10000
            place="munnar"
            print(f'Total amount:{amount}')
        elif choice==2:
            count=int(input("Enter number of Persons:"))
            amount=count*17000
            place="vietnam"
            print(f'Total amount:{amount}')
        elif choice==3:
            count=int(input("Enter number of Persons:"))
            amount=count*12000
            place="kullumanali"
            print(f'Total amount:{amount}')
        self.userinp.update({'place':place})
        self.userinp.update({'amount':amount})
        return self.userinp
        
    def showdetails(self,ch):
        if ch==1:
           t.munnar()
        elif ch==2:
           t.vietnam()
        elif ch==3:
           t.kullumanali()
        
    def insert(self,name,mobile,mail,place,amount):
        res=con.cursor()
        ins_query='Insert into users(name,mobile,mail,place,amount) Values(%s,%s,%s,%s,%s)'
        self.user=(name,mobile,mail,place,amount)
        res.execute(ins_query,self.user)
        con.commit()

    # def update(self,place,amount,name):
    #     res=con.cursor()
    #     update='Update users set place=%s, amount=%s where name=%s'
    #     self.user=(place,amount,name)
    #     res.execute(update,self.user)
    #     con.commit()

t = travel()
t.intro()
inp={}
print('To view Details:--')
ch=int(input('Enter choice:'))
t.showdetails(ch)
exit=input('Do you want to continue type y/n:')
while exit=='y':
    t.intro()
    if exit=='y':
        print('To view Details:--')
        ch=int(input('Enter choice:'))
        t.showdetails(ch)
    else:
        print("Thanks for visiting")
    exit=input('Do you want to explore more places type y/n:')

print('Do you Need to continue visit places:')
sign=(input('Type y/n:'))
if sign=='y':
    print('For signup:-')
    inp =t.signup()
    print(inp)
    print('User Registeration success')
else:
    print('Thanks for visiting...!')

print('Do you Need to continue Payment:')
pay=(input('Type y/n:'))
if pay=='y':
    print('Payment:-')
    t.intro()
    print("Choose place For continue payament:")
    ch=int(input('Enter choice:'))
    inp=t.payment(ch)
    print(inp)
    t.insert(inp['name'],inp['mob'],inp['mail'],inp['place'],inp['amount'])  
    print("----------------------------------------------------------------------------------")
    print("*                                HAPPY JOURNEY                                    *")
    print("----------------------------------------------------------------------------------")
else:
    print('Thanks for visiting...!')


