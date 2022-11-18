import mysql.connector
from tabulate import tabulate

con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pythonproj',
)

class covid:
    
    def intro(self):
        print("***********************************************************************************")
        print("*                                                                                 *")
        print("*            Covid Patients Confirmation Data Analysis Management System          *")
        print("*                                                                                 *")
        print("***********************************************************************************")
        print("1.ADMIN")
        print("2.Patients")
        print("***Note: click 1 if admin or 2 if a patient***")
        print("***********************************************************************************")

    def addpatients(self):
                patients={}
                v1=input("Enter Name:")
                v2=input("Enter Mobile No:")
                v3=input("Enter email:")
                v4=input("Enter Address:")
                patients.update({'Name':v1})
                patients.update({'Mobile':v2})
                patients.update({'Email':v3})
                patients.update({'Address':v4})
                print(f"{patients}Patients updated Successfully!")
                print("-------------------------------------------------------------------------------------")
                return patients

    def insert(self,name,mobile,mail,address):
        self.res=con.cursor()
        ins_query='Insert into covid(patientname,mobile,email,address) Values(%s,%s,%s,%s)'
        self.patients=(name,mobile,mail,address)
        self.res.execute(ins_query,self.patients)
        con.commit()
        print('Data inserted')
    
    def delete(self,id):
        res=con.cursor()
        del_query="DELETE FROM covid WHERE id=%s"
        patient_id=(id,)
        res.execute(del_query,patient_id)
        c.select()
        print("-------------------------------------------------------------------------------------")
        con.commit()

    def select(self):
        res=con.cursor()
        select_query="SELECT `ID`, `patientname`, `mobile`, `email`, `address` FROM `covid`"
        res.execute(select_query)
        patients=res.fetchall()
        print(tabulate(patients,headers=["ID","PATIENTS_NAME","MOBILE","EMAIL"]))
        return patients

    def patients_check(self):
        print("***Patient Checking corona Possibilities***")
        cough=input("Are you feeling Cough?(y/n)...")
        drycough=input("Are you feeling Dry Cough?(y/n)...")
        throat=input("Are you feeling Throat Pain?(y/n)...")
        fever=input("Are you feeling High Temperature?(y/n)...")
        sneeze=input("Are you feeling sneeze?(y/n)...")
        nose=input("Are you feel Running nose?(y/n)...")
        weak=input("Are you feeling weak?(y/n)...")
        pain=input("Are you feeling Body pain?(y/n)...")
        breath=input("Are you feeling Difficulty in Breathing?(y/n)...")
        print("-------------------------------------------------------------------------------------")
        if cough=='y'and drycough=='y' and nose=='y' and sneeze=='y'and throat=='y' and fever=='y' and weak=='y' and pain=='y' and breath=='y':
            print("You're affected by Covid")
            v1=input("Enter Name:")
            v2=input("Enter Mobile No:")
            v3=input("Enter email:")
            v4=input("Enter Address:")
            patients.update({'Name':v1})
            patients.update({'Mobile':v2})
            patients.update({'Email':v3})
            patients.update({'Address':v4})
            c.insert(patients['Name'],patients['Mobile'],patients['Email'],patients['Address'])
            print(f"{patients}Patients updated Successfully!")
            print("You should take quarantine for 14 days")
            print("-------------------------------------------------------------------------------------")
            print("Active Patients.")
            print(patients)
            print("-------------------------------------------------------------------------------------")
            
        elif drycough=='y' and sneeze=='y':
            print("It's just a Air pollution take some Rest")
            print("-------------------------------------------------------------------------------------")
            
        elif cough=='y' and nose=='y' and sneeze=='y':
            print("It's just a Common cold take some Rest")
            print("-------------------------------------------------------------------------------------")
        
        elif cough=='y' and weak=='y' and fever=='y' and pain=='y' and nose=='y':
            print("It is Flu take a prescription properly and take Rest")  
            print("-------------------------------------------------------------------------------------")
        
        else:
            print("No issues you're in Good Health")     
            print("-------------------------------------------------------------------------------------")
        
c=covid()

patients={}
c.intro()
again='y'
count=0
while again=='y' and again!='n':
    if count!=0:
        c.intro()
    check='y'
    exit='y'
    choice=int(input("Enter choice:"))
    if choice==1:
        c.intro()
        while exit=='y' :
            print("-------------------------------------------------------------------------------------")
            print("1.Add Patient:")
            print("2.Remove Patient")
            print("3.Display Patients")
            print("4.Exit")
            print("-------------------------------------------------------------------------------------")
            ad_ch=int(input("Enter choice:"))
            if ad_ch==1:
                n=int(input("Number of Patients:"))
                for i in range(0,n):
                    patients=c.addpatients()
                    print(patients)
                    c.insert(patients['Name'],patients['Mobile'],patients['Email'],patients['Address'])
                    i+=1
            elif ad_ch==2:
                c.select()
                id=input("Enter ID to Remove Patient:")
                c.delete(id)
            elif ad_ch==3:
                c.select()
            exit=input('Need to AGAIN to ADMIN PROCESS Y/N:')
            if exit=='n':
                break

    elif choice==2:     
        if check=='y':
            c.patients_check()
            print('Do you need to check again:')
            check=input('Type y/n:-')

    again=input('DO you need to continue:press y/n:')
    count=count+1
    if again=="n":
       break

