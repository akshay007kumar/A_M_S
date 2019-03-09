# import mysql.connector

# mydb = mysql.connector.connect(host='localhost',user='root',passwd='admin',database='studentAttend')

# c = mydb.cursor()

# sql="UPDATE teacher SET gender = %s Where t_id='t105'"
# val=('male',)
# c.execute(sql,val)
# mydb.commit()

# mydb.close()

# from datetime import time

# # today=datetime.date.today()

# # today1=str(today)

# today='2019-03-05'
# today1=datetime.datetime.strptime(today,'%Y-%m-%d')

# print('\n\n',today,today1)

# date1="01-01-2018"
# date2="10-01-2018"

# newDate1=time.strptime(date1,'%d-%m-%Y')
# newDate2=time.strptime(date2,'%d-%m-%Y')

# print(date1,date2,newDate1,newDate2)

# import datetime
# date1=datetime.datetime.strptime('2019,01,01','%Y,%m,%d')
# age=datetime.date.today()-date1
# print(age)
# print(date1)
# print(datetime.date(2018,1,1)>datetime.date(2018,1,2))




if "":
    print('abc')
else:
    print('xyz')

hi='hello'
hi1='   hello'
hi2='   hello'.strip()
print(hi,hi1,hi2)
print(bool("            ".strip()))






