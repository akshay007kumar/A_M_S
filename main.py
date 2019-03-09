from BLL import *
import datetime

a_user=admin_login[0]
a_pass=admin_login[1]

print('******************** Student Attendence System *********************')

ex='n'
while ex=='n':
	ch=input('''Available users:
	1. Admin
	2. Teacher
	3. Student
		your choice: ''')
	
	if ch == '1':
		user = input('username:')
		passw = input('password: ')
		if user == a_user and passw == a_pass:
			print('login successfull')
			while True:
				a_ch=input('''
	1. Add Teacher
	2. Add Student 
	3. Update Student's Details
	4. Update Teacher's Details
	5. View All teachers
	6. View all students
	7. Search Teacher
	8. Remove teacher
	9. Add course
	10. View available courses
	11. Add Batch
	12. View available batches
	0. Exit
	your choise: ''')

				if a_ch=='1':
					tea=Teacher()
					tid=input('Enter id: ')
					tfname=input('first name: ')
					tlname=input('last name: ')
					gen=input('gender: ')
					dob=input('Date of Birth(yyyy-mm-dd): ')
					addr=input('Address: ')
					email=input('Email: ')
					mob=input('mobile no: ')
					data=tea.addTeacher(tid,tfname,tlname,gen,dob,addr,email,mob)
					print(data,'record inserted')
					print('\nEnter Login Details...')
					uname=input('username: ')
					passw=input('password: ')
					data=tea.createTeacherLogin(tid,uname,passw)
					print(data,'data inserted')
 
				elif a_ch=='2':
					stu=Student()
					sid=input('Enter id: ')
					sfname=input('first name: ')
					slname=input('last name: ')
					gen=input('gender: ')
					dob=input('Date of Birth(yyyy-mm-dd): ')
					age=input('Age: ')
					addr=input('Address: ')
					mob=input('mobile no: ')
					cour=Course()
					data1=cour.viewCourse()
					print("Select from available courses\n")
					for d in data1:
						print('ID:',d[0],'CourseName: ',d[1])
					myCour=input("course id: ")
					bat=Batch()
					data2=bat.viewCourseBatch(myCour)
					print("Select from available batches\n")
					for d in data2:
						tea=Teacher()
						teach=tea.searchTeacher(d[4])
						print('ID:',d[0],'Start Date:',d[1],'Teacher: ',teach[1],teach[2])
					myBat=input("batch id: ")
					data=stu.addStudent(sid,sfname,slname,gen,dob,age,addr,mob,myCour,myBat)
					print(data,"record insert")
					print('\nEnter Login Details...')
					uname=input('username: ')
					passw=input('password: ')
					data=stu.createStudentLogin(sid,uname,passw)
					print(data,'data inserted')
					
				elif a_ch=='3':
					pass
					#Update Student's details
					
				elif a_ch=='4':
					print('Select item you want to update\n','1.First name 2.Last name 3.Address 4.Mobile 5.All details',end=': ')
					upd=input()
					tid=input('teacher id: ')
					tea=Teacher()
					avail=tea.searchTeacher(tid)
					print(cur.rowcount,'record found')
					if avail is None:
						pass
					mydata = ''
					if upd == '1' or upd == '2' or upd == '3' or upd == '4':
						if avail!=None:
							if upd=='1':
								mydata=input('First name: ')
							elif upd=='2':
								mydata=input('Last name: ')
							elif upd=='3':
								mydata=input('Adress: ')
							else:
								mydata=input('Mobile: ')
							data=tea.updateTeacherDetails(upd,tid,mydata)
							print(data,'record updated')
					elif upd=='5':
						if avail!=None:
							tea.removeTeacher(tid)
							tfname=input('first name: ')
							tlname=input('last name: ')
							gen=input('gender: ')
							dob=input('Date of Birth(yyyy-mm-dd): ')
							addr=input('Address: ')
							email=input('Email: ')
							mob=input('mobile no: ')
							data=tea.addTeacher(tid,tfname,tlname,gen,dob,addr,email,mob)
							print(data,'record updated')
					else:
						print('invalid input')
				elif a_ch=='5':
					tea=Teacher()
					data=tea.viewTeacher()
					for d in data:
						print('ID:',d[0],'NAME:',d[1],d[2],'GENDER:',d[3],'DOB:',d[4],'\nADDRESS:',d[5],'EMAIL:',d[6],'MOBILE:',d[7],'\n')
					print(cur.rowcount,'records Available')
				elif a_ch=='6':
					stu=Student()
					data=stu.viewAllStudent()
					for d in data:
						print(d)
				elif a_ch=='7':
					tea=Teacher()
					tid=input('teacher id: ')
					data=tea.searchTeacher(tid)
					print(data)
				elif a_ch=='8':
					tea=Teacher()
					tid=input('teacher id: ')
					data=tea.removeTeacher(tid)
					print(data,'record deleted')
				elif a_ch=='9':
					cour=Course()
					cid=input('course id: ')
					cname=input('course name: ')
					data=cour.addCourse(cid,cname)
					print(data,'record added')
				elif a_ch=='10':
					cour=Course()
					data=cour.viewCourse()
					for d in data:
						print(d)
					print(cur.rowcount,'records Available')
				elif a_ch=='11':
					bat=Batch()
					tea=Teacher()
					cour=Course()
					bid=input('Batch id: ')
					sd=input('Start date(yyyy-mm-dd): ')
					ed=input('End date(yyyy-mm-dd): ')
					print('Choose from available teachers')
					data1=tea.viewTeacher()
					for d in data1:
						print('id=',d[0],'name=',d[1])
					tid=input('Teacher id: ')
					data2=cour.viewCourse()
					for d in data2:
						print('id=',d[0],'name=',d[1])
					print('Choose from available courses')
					cid=input('Course id: ')
					data=bat.addBatch(bid,sd,ed,cid,tid)
					print(data,'record inserted')

				elif a_ch=='12':
					bat=Batch()
					data=bat.viewBatch()
					for d in data:
						print(d)
					print(cur.rowcount,'records available')
					
				elif a_ch=='0':
					break
				else:
					print('Invalid input')

		else:
			print('Invalid username or password')
	elif ch == '2':
		t_user=input('username: ')
		t_pass=input('password: ')
		validUser=0
		for t in teacher_login:
			if t[1]==t_user and t[2]==t_pass:
				validUser=1
				print('Teacher Login Successfull')
				print('                 Active user id: ',t[0])
				while True:
					t_ch=input('''
	1. View Students
	2. Search Student
	3. Mark Attendence
	4. View Attendence
	5. Update Password
	0. Exit
		your choise: ''')
					if t_ch=='1':
						stu = Student()
						bat = Batch()
						myBat=bat.searchTeacherBatch(t[0])
						print('Your batches')
						for b in myBat:
							print(b)
						mystu=input('Enter batch id to view students: ')
						data=stu.viewBatchStudent(mystu)
						for d in data:
							print(d)
						print(cur.rowcount,'record found')

					elif t_ch=='2':
						stu = Student()
						sid=input('student id: ')
						data=stu.searchStudent(sid)
						print(data)
						print(cur.rowcount,'record found')

					elif t_ch=='3':
						stu = Student()
						bat = Batch()
						att=Attendence()
						today=datetime.date.today()
						myBatches=bat.searchTeacherBatch(t[0])
						print('Your batches')
						for b in myBatches:
							print(b)
						bid=input('Batch ID: ')
						data=stu.viewBatchStudent(bid)
						print('Mark attendence( p or a )')
						for d in data:
							print(d[1],d[2],':',end=' ')
							attend=input()
							att.markAttendence(d[0],bid,today,attend)
						print('Attendence of batch',bid,'for date ',today,'is marked')					

					elif t_ch=='4':
						att=Attendence()
						bat = Batch()
						myBatches=bat.searchTeacherBatch(t[0])
						print('Your batches')
						for b in myBatches:
							print(b)
						bid=input('Batch ID: ')
						data=att.viewBatchAttendence(bid)
						for d in data:
							print(d)
						print(cur.rowcount,'data recieved')

					elif t_ch=='5':
						tea=Teacher()
						newPass=input('New Password: ')
						confirmPass=input('Confirm Password:')
						if newPass == confirmPass:
							date=tea.updatePassword(t[0],newPass)
							print(date,'record updated')
							break
						else:
							print('Password doesnot match,Please Re-enter!')

					elif t_ch=='0':
						break

					else:
						print('invalid input')

		if validUser == 0:
			print('invalid username or password!')

	elif ch== '3':
		s_user=input('username: ')
		s_pass=input('password: ')
		validStu=0
		for s in student_login:
			if s[1] == s_user and s[2] == s_pass:
				validStu=1
				print('Login successfull!')
				print('                 Active User ID: ',s[0])
				while True:
					s_ch=input('''
	1. View Attendence
	2. Update Password
	0.Exit		
		your choise: ''')
					if s_ch=='1':
						att=Attendence()
						data=att.viewStudentAttendence(s[0])
						for d in data:
							print(d)
					elif s_ch=='2':
						stu=Student()
						newPass=input('New Password: ')
						confirmPass=input('Confirm Password:')
						if newPass == confirmPass:
							date=stu.updatePassword(s[0],newPass)
							print(date,'record updated')
							break
						else:
							print('Password doesnot match,Please Re-enter!')
					elif s_ch=='0':
						break
		if validStu==0:
			print('Invalid Username or password!')
	else:
		print('Invalid Input')

	ex=input('want to exit(y/n): ')
print("********************************************************************")
cur.close()
mydb.close()