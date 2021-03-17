import mysql.connector as sql
from tabulate import tabulate
import webbrowser
conn=sql.connect(host = 'localhost',port='3306',user='root',passwd='bwcc')
mycursor=conn.cursor()
#mycursor.execute('DROP DATABASE IF EXISTS movie_ticket')
#mycursor.execute('CREATE DATABASE movie_ticket')
mycursor.execute('USE movie_tickets')
#mycursor.execute('DROP TABLE IF EXISTS theater')
#sql = '''CREATE TABLE theater(
 #                   MOVIES CHAR(20),
  #                  PHONE_NO INT NOT NULL,
   #                 TICKET INT NOT NULL,SEX CHAR(20) NOT NULL,
    #                FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20),SNACKS CHAR(20))'''
#mycursor.execute(sql)
#sql2='''CREATE TABLE name(
 #                   MOVIES CHAR(20),
  #                  SHOW_TIME  CHAR(20),
   #                 DATE char(20),PRICE _Rs int,CATEGORY char(20))'''
#mycursor.execute(sql2)
#mycursor=conn.cursor()
print ("LOG IN")
Enter_user=input("Enter userID :")
Enter_passwd=input("Enter password :")
if Enter_user=='asa' and Enter_passwd=='asa':
    print('')
    print('')
    print (" _ _ _ _ _ _ _ _ _ _ _ _WELCOME BACK_ _ _ _ _ _ _ _ _ _ _ _")
#elif :
 #5   print("ACCESS DENIED")
    
    if conn.is_connected():
        print('')
        print('')
        print('')
        print ("|$|$$$$$$$$$$ ASA THEATRE BOOKING (AC & NON AC) $$$$$$$$$$|$|")
        print ("|$|                                                       |$|")
        print ("|$|                                                       |$|")
        print ("|$|_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_|$|")
        print ("|$|                                                       |$|")
        print ("|$|~~~~~~~~~~~~~~~~~~~ASA THEATRES~~~~~~~~~~~~~~~~~~~~~~~~|$|")
        print ("|$|                                                       |$|")
        print ("|$|         1.          BOX OFFICE                        |$|")
        print ("|$|         2.    SHOW MOVIE RATING/REVIEW                |$|")
        print ("|$|         3.         BOOKING COUNTER                    |$|")
        print ("|$|         4.      SHOW BOOKING DETAILS                  |$|")
        print ("|$|         5.                                            |$|")
        print ("|$|         6.          RECIPT BILL                       |$|")
        print ("|$|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|$|")
    ch=int(input("Enter your choice :"))
while True:
    if ch==1:
        mycursor.execute("select * from name")
        data1=mycursor.fetchall()
        print(tabulate(data1,headers=['MOVIES','SHOW_TIME','DATE','PRICE','GENRE'], tablefmt='psql'))
        ch=int(input("Enter your choice :"))
    elif ch ==2:
        webbrowser.open('https://www.imdb.com/',new=1)
        break
        ch=int(input("Enter your choice :"))
    elif ch ==3:
        S_No = input("Enter the S_No :")
        MOVIES = input("Enter the movie name :")
        PHONE_NO = input("Enter phone number :")
        TICKET = input("Enter total tickets :" )
        SEX = input ("Enter your sex :" )
        FIRST_NAME = input ("Enter your first name :")
        LAST_NAME = input ("Enter your last name :")
        SNACKS = input ("Order your snacks :")
        ins="insert into theater values( '{}','{}','{}','{}','{}','{}','{}','{}')".format(S_No,MOVIES,
                                                                                             PHONE_NO,TICKET,SEX,FIRST_NAME,LAST_NAME,SNACKS)

        mycursor.execute(ins)
        conn.commit()
        print (" ticket booked congrats")
        print ("Thank you for visiting asa theatre")
        print ("ratings")
        ch=int(input("Enter your choice :"))
    elif ch==4:
        mycursor.execute("select * from theater")
        data=mycursor.fetchall()
        print(tabulate(data,headers=['MOVIES','PHONE_NO','TICKET','SEX','FIRST_NAME','LAST_NAME','SNACKS'], tablefmt='psql'))
        ch=int(input("Enter your choice :"))
    elif ch==5:
         print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!WELCOME TO 2nd CLASS TICKET BOOKING !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
         a = input ("Enter your name :")
         b = input ("Enter your movie name :")
         c = input ("Enter your ph_no :")
         d = input ("Enter total tickets :")
         pswd= input("Enter the password :")
         sks = input(" Order your snacks :")
         print ("///////////////ENJOY THE MOVIE AND HAVE FUN/////////////////")
         ch=int(input("Enter your choice :"))
      
    else:
        mycursor.execute(" select name.MOVIES,PRICE*TICKET,theater.FIRST_NAME FROM name INNER JOIN theater ON name.MOVIES=theater.MOVIES;")
        data3=mycursor.fetchall()
        print(tabulate(data3,headers=['Payable_amount', 'Name'], tablefmt='psql'))
        ch=int(input("Enter your choice :"))
else:
    print('lol')
