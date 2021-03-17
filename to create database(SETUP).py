 #program to create mysql database movie_ticket
import mysql.connector as sql
conn=sql.connect(host = 'localhost',port='3306',user='root',passwd='bwcc')
mycursor=conn.cursor()
mycursor.execute('DROP DATABASE IF EXISTS movie_tickets')
mycursor.execute('CREATE DATABASE movie_tickets')
mycursor.execute('USE movie_tickets')
mycursor.execute('DROP TABLE IF EXISTS theater')
sql = '''CREATE TABLE theater(S_No int NOT NULL,MOVIES CHAR(20) NOT NULL,
                    PHONE_NO INT NOT NULL,
                    TICKET INT NOT NULL,SEX CHAR(20) NOT NULL,
                    FIRST_NAME CHAR(20) NOT NULL,LAST_NAME CHAR(20) NOT NULL,SNACKS CHAR(20) NOT NULL)'''
mycursor.execute(sql)
mycursor.execute('USE movie_tickets')
sql2= '''CREATE TABLE name(S_No int NOT NULL,MOVIES CHAR(20) NOT NULL,
                    SHOW_TIME  CHAR(20) NOT NULL,
                    DATE char(20) NOT NULL,PRICE int NOT NULL,GRNRE char(20) NOT NULL)'''
mycursor.execute(sql2)
mycursor=conn.cursor()
mycursor.execute('USE movie_tickets')
#M1
sql3A='''INSERT INTO name values(001,'Alladin','9am-12noon','20-march-2021',250,'Fantacy\\Family')'''
mycursor.execute(sql3A)

#M2
sql4A='''INSERT INTO name values(002,'Insepion','12non-3pm','20-march-2021',150,'Sci-Fi')'''
mycursor.execute(sql4A)

#M3
sql5A='''INSERT INTO name values(003,'Kgf2','3pm-6pm','20-march-2021',200,'Action\\Drama')'''
mycursor.execute(sql5A)

#M4
sql6A='''INSERT INTO name values(004,'War','6pm-9pm','20-march-2021',150,'Action')'''
mycursor.execute(sql6A)

#M5
sql7A='''INSERT INTO name values(005,'A Walk To Remember','9pm-12pm','20-march-2021',350,'Romantic')'''
mycursor.execute(sql7A)
mycursor=conn.cursor()
conn.commit()
