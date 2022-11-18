import mysql.connector

con= mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pythonproj',
)

class atm:
    def intro(self):
        print("***********************************************************************************")
        print("*                                                                                 *")
        print("*                           WELCOME TO DP ATM SERVICES                            *")
        print("*                                                                                 *")
        print("***********************************************************************************")
        print("1.REGISTER NEW ACCOUNT FOR ATM SERVICE")
        print("2.LOGIN")
        print("3.Exit")
        print("***Note: click 1 if Register or 2 if a Login***")
        print("***********************************************************************************")


    def register(self):
        name=input("Enter Account Holder Name:")
        accn=int(input("Enter Account Number:"))
        amount=int(input("Enter Starting amount to deposit:"))
        pw=int(input("Set password:"))
        res=con.cursor()
        val=(name,accn,pw,amount)
        sql="Insert into data(name,account,password,deposit) values(%s,%s,%s,%s)"
        res.execute(sql,val)
        print("***********************************************************************************")
        print("User Registered Successfully.....!")
        print("***********************************************************************************")
        con.commit()

    def login(self):
        info=int(input("Enter userid:"))
        passw=int(input("Enter Password:"))
        res=con.cursor()
        sql1="SELECT * FROM data where account=%s"
        val1=(info,)
        res.execute(sql1,val1)
        row=res.fetchone()
        if res.rowcount==1:
            sql2="SELECT * FROM data where password=%s"
            val2=(passw,)
            res.execute(sql2,val2)
            row=res.fetchone()
            if res.rowcount==1:
                print("***********************************************************************************")
                print("login successfully")
                print("***********************************************************************************")
                print("1.Check Balance")
                print("2.Withdraw")
                print("3.Deposit")
                print("***********************************************************************************")
                d=int(input("Enter choice:"))
                if d==1:
                    sql3=("Select deposit from pythonproj.data where password=%s")
                    val3=(passw,)
                    res.execute(sql3,val3)
                    ans1=res.fetchone()
                    print("***********************************************************************************")
                    print(f"Your Available Balance:{ans1}")
                    print("***********************************************************************************")
                if d==2:
                    withdraw=int(input("howmuch withdraw:"))
                    sql4=("Select deposit from pythonproj.data where password=%s")
                    val4=(passw,)
                    res.execute(sql4,val4)
                    ans1=res.fetchone()
                    x=list(ans1)
                    for i in x:
                        z=((int(i)))
                    if withdraw>z:
                        print("Insufficient amount")
                        print("***********************************************************************************")
                        print(f"Your Available Balance:{ans1}")
                        print("***********************************************************************************")
                        withdraw=int(input("howmuch withdraw:"))
                        c=z-withdraw
                        sql5="UPDATE data SET deposit=%s where password=%s"
                        val5=(c,passw)
                        res.execute(sql5,val5)
                        print("***********************************************************************************")
                        print(f"Available Balance Amount:{c}")
                        print("***********************************************************************************")
                        con.commit()
                    else:
                        c=z-withdraw
                        sql5="UPDATE data SET deposit=%s where password=%s"
                        val5=(c,passw)
                        res.execute(sql5,val5)
                        print("***********************************************************************************")
                        print(f"Available Balance Amount:{c}")
                        print("***********************************************************************************")
                        con.commit()

                if d==3:
                    dep=int(input("How much you want to Deposit:"))
                    sql6=("Select deposit from pythonproj.data where password=%s")
                    val6=(passw,)
                    res.execute(sql6,val6)
                    ans2=res.fetchone()
                    x=list(ans2)
                    for i in x:
                        z=(int(i))
                        c=z+dep
                    sql7="UPDATE data SET deposit=%s where password=%s"
                    val7=(c,passw)
                    res.execute(sql7,val7)
                    print("***********************************************************************************")
                    print(f"Available Balance Amount:{c}")
                    print("***********************************************************************************")
                    con.commit()
            else:
                print("Invalid password")

        else:
            print("Account Doesn't Exist")
    
        
a1=atm()
a1.intro()
n=int(input("CHOOSE ANYONE:"))
ch1='y'
ch2='y'
again='y'
while again=='y':
    if n==1:
        if(ch1=='y'):
            a1.register()
            ch1=input("Do you need to add another user type y/n:")

    if n==2:
        if ch2=='y':
            a1.login()
            ch2=input("Do you need to check again type y/n:")

    if n==3:
        exit(0)
    again=input("Do you need to again do any process y/n:")
    if again=='n':
        exit(0)
    a1.intro()
    n=int(input("CHOOSE ANYONE:"))