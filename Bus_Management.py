#import login
#import signup
#import pandas as
import pandas as pd
import mysql.connector
from getpass import getpass
import stdiomask
mydb = mysql.connector.connect(
  host="localhost",
  user="Nimish",
  password="XXXXXX",
  database='BusMgmt'
)
l ='='*74


def booking():
    mydb = mysql.connector.connect(
      host="localhost",
      user="Nimish",
      password="password123#",
      database='BusMgmt'
    )
    print(l)
    print("\t\tD E P A R T U R E    &   D E S T I N A T I O N")
    print(l)
    #taking input of wished buses
    Departure = input("Enter the Departure City : ")
    Destination = input("Enter the Destination City : ")
    Date = input("Enter date of Departure (DD-MM-YYYY) : ")
    #selecting favourable buses from database
    buses="SELECT * FROM Buses WHERE Departure='"+Departure+"'\
    AND Destination ='"+Destination+"'AND DateOfDeparture ='"+Date+"';"
    mycursor = mydb.cursor()
    mycursor.execute(buses)
    myresult=mycursor.fetchall()
    #checking availability
    if not myresult :
        dep = "SELECT * FROM Buses WHERE Departure='"+Departure+"';"
        arr = "SELECT * FROM Buses WHERE Destination='"+Destination+"';"
        lol= "SELECT * FROM Buses WHERE DateOfDeparture='"+Date+"';"
        mycursor1 = mydb.cursor()
        mycursor1.execute(dep)
        myresult1=mycursor1.fetchall()
        mycursor2 = mydb.cursor()
        mycursor2.execute(arr)
        myresult2=mycursor2.fetchall()
        mycursor3= mydb.cursor()
        mycursor3.execute(lol)
        myresult3=mycursor3.fetchall()
        if not myresult1 or not myresult2:
            print("No buses available for specified Departure Location or Destination")
            x = input("Press 1 to exit\nPress 2 to Rebook\n")
            if x == '1':
                print("Exiting...")
                exit()
            elif x == '2':
                booking()
            else:
                print("Invalid Input")
                booking()
        else:
            if not myresult3:
                print("No buses available for specified Date")
                print("Below are the buses running on the specified route")
                avail="SELECT * FROM Buses WHERE Departure='"+Departure+"'\
                AND Destination ='"+Destination+"';"
                mycursor4 = mydb.cursor()
                mycursor4.execute(avail)
                myresult4=mycursor4.fetchall()
                sequence = mycursor4.column_names
                #print(sequence)
                df = pd.DataFrame(myresult4,columns=sequence)
                pd.set_option('display.max_columns', None)
                print(df)
                a = input("Enter 1 for finalizing buses \nEnter 2 to go back \nEnter 3 to exit\n")
                if a == '1':
                    Selection=int(input("Press 1 for 1st bus\nPress 2 for 2nd bus and so on..\n"))
                    SelectedBus=myresult4[Selection-1]
                    #print(SelectedBus)
                    print(l)
                    print("\t\t\t\t C H E C K O U T")
                    print(l)
                    print("The following the Selected Bus by you")
                    #print(SelectedBus)
                    #print(sequence)
                    df1= pd.DataFrame([SelectedBus],columns=sequence)
                    print(df1)
                    y = input("Press 1 to Confirm Booking\nPress 2 to Rebook\n")
                    if y == '1':
                        print("The Booking has been Sucessfully Confirmed")
                        exit()
                    elif y == '2':
                        booking()
                    else:
                        print("Invalid Input")
                        booking()

                elif a == '2':
                    booking()
                elif a == '3':
                    exit()
                else:
                    print("Invalid Input")
                    booking()
    else:
        sequence = mycursor.column_names
        df = pd.DataFrame(myresult,columns=sequence)
        pd.set_option('display.max_columns', None)
        print(df)
        a = input("Enter 1 for finalizing buses \nEnter 2 to go back \nEnter 3 to exit\n")
        if a == '1':
            Selection=int(input("Press 1 for 1st bus\nPress 2 for 2nd bus and so on..\n "))
            SelectedBus=(myresult[Selection-1])
            print(l)
            print("\t\t\t\t C H E C K O U T")
            print(l)
            print("The following the Selected Bus by you")
            df1=pd.DataFrame([SelectedBus],columns=sequence)
            print(df1)
            y = input("Press 1 to Confirm Booking\nPress 2 to Rebook\n")
            if y == '1':
                print("The Booking has been Sucessfully Confirmed")
            elif y == '2':
                booking()
            else:
                print("Invalid Input")
                booking()
        elif a == '2':
            booking()
        elif a == '3':
            exit()
        else:
            print("Invalid Input")
            booking()



def signup():
#connecting to database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Nimish",
      password="password123#",
      database='BusMgmt'
    )
    mycursor1 = mydb.cursor()
    mycursor1.execute("SELECT * FROM User;")
    myresult=mycursor1.fetchall()
    #print(myresult)
    y = len(myresult)
#taking input for database
    UserName = input("Enter Username : ")
    for x in range(0,y):
        if myresult[x][0] == UserName:
            print("Username already taken")
            signup()
        else:
            Pass = stdiomask.getpass("Enter Password of your choice : ")
            Email = input("Enter Email Address : ")
            MobileNo = input("Enter Mobile No. : ")
            if len(MobileNo) != 10 :
                print("Invalid MobileNo")
                signup()
            else:
                Gender = input("Enter Gender : ")
                Age = input("Enter Age : ")
                        #inserting values into the database in table User
                str="INSERT INTO User VALUES ('"+UserName+"','"+Pass+"','"+Email+"','"+MobileNo+"','"+Gender+"','"+Age+"');"
                mycursor = mydb.cursor()
                mycursor.execute(str)
                mydb.commit()
                print("Account Sucessfully created")
                login()








def login():
    mydb = mysql.connector.connect(
        host="localhost",
        user="Nimish",
        password="password123#",
        database="BusMgmt"
    )
    l='='*74
    print(l)
    print("\t\t\t\tL O G I N")
    print(l)
    #mycursor1 = mydb.cursor()
    #mycursor1.execute("SELECT * FROM User")
    #myresult1 = mycursor1.fetchall()
    #for y in myresult1:
    #    print(y)
#taking input of username and password
    UserName=input("Enter a valid Username : ")
    Pass = stdiomask.getpass("Enter Password : ")
#getting database values
    str="SELECT * FROM User WHERE UserName = '"+UserName+"';"
    mycursor = mydb.cursor()
    mycursor.execute(str)
    myresult=mycursor.fetchall()
    #for x in myresult:
        #print(x)
#checking Pass and username
    if not myresult:
        print("Invalid Username")
        a = input("Press 1 to Signup \nPress 2 to retry\nPress 3 to \n")
        if a == '1':
            signup()
        elif a == '2':
            login()
        elif a == '3':
            exit()
        else :
            print("Invalid input")
            login()
    else:
        if myresult[0][1] == Pass:
            print("correct Password")
            booking()
        else :
            print("Incorrect Password")
            a = input("Press 1 to Retry \nPress 2 to signup\nPress 3 to exit\n")
            if a == '1':
                login()
            elif a == '2':
                signup()
            elif a == '3':
                exit()
            else:
                print("Invalid Input")
                login()





def main():
    print(l)
    print("\t\tB U S   M A N A G E M E N T   S Y S T E M")
    print(l)
    a = input("Press 1 to Login\nPress 2 to Signup\nPress 3 to exit\n")
    if a == '1':
        login()
    elif a == '2':
        signup()
    elif a == '3':
        exit()
    else:
        print("Invalid input")
        main()
main()
