import mysql.connector as C

db=C.connect(host='localhost',database='devdarshan',user='root',passwd='Mysql')

c=db.cursor()

#to create database if not exist

def database():
    
    c.execute("create database priyanshuchamp")
    
def use():
    c.execute("use priyanshuchamp")
    
inp=int(input("enter if the database not created 10 and enter 30 if created"))
if inp==10:
    
    database()
    use()
use()

#choices
mch=int(input("enter 1 for continuation or 2 for not"))
if mch==1:
    while mch==1:
        def choices():
            use()
            
            print("1.to create table")
            
            print("2.to insert rows")
            
            print("3.to display rows")
            
            print("4.to delete some rows")
            
            print("5.to update the rows")
            
            print("6.to close the connection")
            
        choices()
        
        ch=eval(input("enter the value from above"))
        
        #to create table
        
        if ch==1:
            
            def table():
                
                c.execute("create table freesim(som varchar(30),pn varchar(30), ac varchar(30) not null primary key,cc varchar(30))")
                
                c.execute("create table freebroadband(bbi varchar(30),tn varchar(30) not null primary key, plan int,ac varchar(30))")
                
                db.commit()
                
                print("table has been successfully created")
                
            table()
            mch=int(input("enter 1 for continuation or 2 for not"))
       
        
        #to insert rows in a table
            
        if ch==2:
            
            def insertion():
                print("*****************************")
                print("ALL DATABASE IS - ")
                c.execute("show databases")
                d=c.fetchall()
                for i in d:
                    print(i)
                print("ALL DATABASE WAS -")
                print("*****************************")
                print("FREESIM HAS TABLE  AS FOLLOWS:-")
                c.execute("desc freesim")
                d=c.fetchall()
                for i in d:
                    print(i)
                print("FREESIM HAS TABLE AS ABOVE ")
                print("*****************************")
                print("FREEBROADBAND HAS TABLE AS BELOW")
                c.execute("desc freebroadband")
                d=c.fetchall()
                for i in d:
                    print(i)
                print("FREEBROADBAND HAS TABLE AS ABOVE")
                print("*****************************")
                    
                print("*****************************")
                print("now insertion ")
                
                som=input("enter the sim owner name")
                
                pn=input("enter the phone number")
                
                ac=input("enter the aadhar card number")
                
                cc=input("enter the country code")
                
                bbi=input("enter the broadband id")
                
                tn=input("enter the telephone number")
                
                plan=eval(input("enter the plan"))
                
                c.execute("insert into freebroadband values('{}','{}',{},'{}')".format(bbi,tn,plan,ac))
                
                db.commit()
                
                c.execute("insert into freesim values('{}','{}','{}','{}')".format(som,pn,ac,cc))
                
                db.commit()
                
                print("records have been successfully entered")
                
                print("*****************************")
                
            insertion()
       
            mch=int(input("enter 1 for continuation or 2 for not"))
        #to display record stored in a table
            
        if ch==3:
            
            def display():
                print("*****************************")
                print("*****************************")
                
                print("FOR DISPLAY")
                
                cho=input("enter A for printing all rows together,(without quotes), or B for printing for by your choice")
                
                if cho=='A' or cho=='a':
                    print("FOR ALL ROWS TOGETHER")
                    
                    c.execute("select * from freesim")
                    print("*****************************")
                    
                    for i in c:
                        
                        print("ROWS OF FREESIM TABLE",i)
                        
                    print("*****************************")    
                    
                    c.execute("select * from freebroadband")
                    
                    for i in c:
                        
                        print("ROWS OF FREEBROADBAND",i)
                    print("*****************************")
                   
                        
                if cho=='B' or cho=='b':
                    print("*****************************")
                    
                    print("FOR DISPLAYING USING CONDITION")
                    
                    v=eval(input("how you want to print? 1 for through sim owner name,2 for through phone number, 3 for through aadhar card number, 4 forthrough country code, 5 for through bbi, 6 for through telephone number, 7 for through plan"))
                    
                    r=int(input("enter 10 for printing all records or enter 20 for printing required number of rows"))
                    
                    
                    if v==1:
                        
                        som=input("enter the sim owner (without quotes) name that you want to print")
                        
                        if r==10:
                            
                            c.execute("select * from freesim where som=('{}')".format(som))
                            
                            d=c.fetchall()
                            
                            for i in d:
                                
                                print(i)
                                
                        if r==20:
                            x=eval(input("enter how many records you want to display"))
                            
                            c.execute("select * from freesim where som=('{}')".format(som))
                            
                            d=c.fetchmany(x)
                            
                            for i in d:
                                
                                print(i)
                                
                    if v==2:
                        
                        pn=input("enter the (without quotes)  phone number")
                        
                        if r==10:
                            
                            c.execute("select * from freesim where pn = ({})".format(pn))
                            
                            d=c.fetchall()
                            
                            for i in d:
                                
                                print(i)
                                
                        if r==20:
                            
                            x=eval(input("enter how many records you want to display"))
                            
                            c.execute ("select * from freesim where pn=({})".format(pn))
                            
                            d=c.fetchmany(x)
                            
                            for i in d:
                                
                                print(i)
                                
                    if v==3:
                        
                        ac=input("enter aadhar (without quotes) card number")
                        
                        if r==10:
                            
                            c.execute("select * from freesim where ac=({})".format(ac))
                            
                            d=c.fetchall()
                            
                            for i in d:
                                
                                print(i)
                                
                        if r==20:
                            
                            x=eval(input("enter how many records you want to display"))
                            
                            c.execute("select * from freesim where ac=({})".format(ac))
                            
                            d=c.fetchmany(x)
                            
                            for i in d:
                                
                                print(i)
                                
                    if v==4:
                        
                        cc=input("enter the (without quotes) country code")
                        
                        if r==10:
                            
                            c.execute("select * from freesim where cc=('{}')".format(cc))
                            
                            d=c.fetchall()
                            
                            for i in d:
                                
                                print(i)
                                
                        if r==20:
                            
                            x=eval(input("enter how many records you want to display"))
                            
                            c.execute("select * from freesim where cc=('{}')".format(cc))
                            
                            d=c.fetchmany(x)
                            
                            for i in d:
                                
                                print(i)
                                
                    if v==5:
                        
                        bbi=input("enter the (without quotes) broadband id")
                        
                        if r==10:
                            
                            c.execute("select * from freebroadband where bbi=({})".format(bbi))
                            
                            d=c.fetchall()
                            
                            for i in d:
                                
                                print(i)
                                
                        if r==20:
                            
                            x=eval(input("enter how many records you want to display"))
                            
                            c.execute("select * from freebroadband where bbi=({})".format(bbi))
                            
                            d=c.fetchmany(x)
                            
                            for i in d:
                                
                                print(i)
                                
                    if v==6:
                        
                        tn=input("enter telephone number (without quotes) that you want to display")
                        
                        if r==10:
                            
                            c.execute("select * from freebroadband where tn=({})".format(tn))
                            
                            d=c.fetchall()
                            
                            for i in d:
                                
                                print(i)
                                
                        if r==20:
                            
                            x=eval(input("enter how many records you want to display"))
                            
                            c.execute("select * from freebroadband where tn=({})".format(tn))
                            
                            d=c.fetchmany(x)
                            
                            for i in d:
                                
                                print(i)
                                
                    if v==7:
                        
                        plan=eval(input("enter (without quotes) the plan"))
                        
                        if r==10:
                            
                            c.execute("select * from freebroadband where plan=({})".format(plan))
                            
                            d=c.fetchall()
                            
                            for i in d:
                                
                                print(i)
                                
                        if r==20:
                            
                            x=eval(input("enter how many records you want to display"))
                            
                            c.execute("select * from freebroadband where plan=({})".format(plan))
                            
                            d=c.fetchmany(x)
                            
                            for i in d:
                                
                                print(i)
                    print("*****************************")
                print("*****************************")         
                print("*****************************")
            display()
            mch=int(input("enter 1 for continuation or 2 for not"))
        
        #to delete a record from a table
            
        if ch==4:
            
            def deletion():
                print("*****************************")
                print("*****************************")
                print("for deletion")
                
                print("for deleting the reocrds you must have aadhar card number")
                
                d=input("enter the table name (without quotes) from which you want to delete")
                
                
                ac=input("enter aadahar card number that you want to delete")
                
                if d=='freesim':
                    
                    c.execute("delete from freesim where ac=('{}')".format(ac))
                    
                    db.commit()
                    
                if d=='freebroadband':
                    
                    c.execute("delete from freebroadband where ac=('{}')".format(ac))
                    
                    print("successfully deleted records of aadhar number of",ac)
                    
                    db.commit()
                print("*****************************")
                print("*****************************")
            deletion()
            mch=int(input("enter 1 for continuation or 2 for not"))
        #to upadate a record in a table
            
        if ch==5:
            
            def updation():
                print("*****************************")
                print("*****************************")
                print("FOR UPDATING A RECORD")
                
                
                m=input("enter which records you want to update (without quotes)i.e. son or pn or ac or cc or bbi or tn or plan")
                
                acs=input("enter aadhar number")
                
                if m=='son':
                    
                    g=input("enter the new updated value of sim owner name")
                    
                    c.execute("update freesim set som=('{}') where ac=('{}')".format(g,acs))
                    
                    db.commit()
                    
                if m=='pn':
                    
                    h=input("enter the new (without quotes) phone number")
                    
                    c.execute("update freesim set pn=('{}') where ac=('{}')".format(h,acs))
                    
                    db.commit()
                    
                if m=='ac':
                    
                    a=input("enter new aadhar (without quotes)  number")
                    
                    c.execute("update freesim set ac=('{}') where ac=('{}')".format(a,acs))
                    
                    db.commit()
                if m=='cc':
                    
                    c2=input("enter the new (without quotes) country code")
                    
                    c.execute("update freesim set cc=('{}') where ac=('{}')".format(c2,acs))
                    
                    db.commit()
                    
                if m=='bbi':
                    
                    bb=input("enter the (without quotes) new broadband id")
                    
                    c.execute("update freebroadband set bbi=('{}') where ac=('{}')".format(bb,acs))
                    
                    db.commit()
                    
                if m=='tn':
                    
                    t=input("enter new (without quotes) telephone number")
                    
                    c.execute("update freebroadband set tn=('{}') where ac=('{}')".format(t,acs))
                    
                    db.commit()
                    
                if m=='plan':
                    
                    p=eval(input("enter the (without quotes) new plan"))
                    
                    c.execute("update freebroadband set plan=({}) where ac=('{}')".format(p,acs))
                    
                    db.commit()
                    
                print("records have been successfully updated of",acs)
                print("*****************************")
                print("*****************************")
            updation()
            mch=int(input("enter 1 for continuation or 2 for not"))
        if ch==6:
            print("*****************************")
            print("*****************************")
            print("FOR CLOSING CONNECTION ")
            
            db.close()
            print("connection has been stopped")
            print("*****************************")
            print("*****************************")

            mch=int(input("enter 1 for continuation or 2 for not"))
        
            #DONE
        
            
print("CONGRATULATIONS  YOU  HAVE SUCCESSFULLY  IMPLEMENTED ")
    
print(" BALLE BALLE SHAYAVA SHAYAVA ")
    
    
        
    
print("*****************************")
print("*****************************")
    
