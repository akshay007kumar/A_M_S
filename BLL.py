import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='admin', database='studentAttend')
cur = mydb.cursor()
cur.execute('select * from admin')
admin_login = cur.fetchone()
cur.execute('select * from teacherlogin')
teacher_login = cur.fetchall()
cur.execute('SELECT * FROM studentLogin')
student_login = cur.fetchall()
# SYSTEM HAS ONLY ONE ADMINISTRATOR #

class Student:

    def __init__(self):
        self.s_id = ''
        self.fname = ''
        self.lname = ''
        self.gender = ''
        self.DOB = ''
        self.address = ''
        self.mobile = ''
        self.course_id = ''
        self.batch_id = ''

    def addStudent(self, s_id, fname, lname, gen, dob, age, add, mob, c_id, b_id):
        self.s_id = s_id
        self.fname = fname
        self.lname = lname
        self.gender = gen
        self.DOB = dob
        self.age = age
        self.address = add
        self.mobile = mob
        self.course_id = c_id
        self.batch_id = b_id

        cur.execute('INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
        self.s_id, self.fname, self.lname, self.gender, self.DOB, self.age, self.address, self.mobile, self.course_id,
        self.batch_id))
        mydb.commit()
        return cur.rowcount

    def modifyStudentDetails(self):
        pass

    def deleteStudent(self):
        pass

    def searchStudent(self, sid):
        cur.execute('SELECT * FROM student WHERE s_id=%s', (sid,))
        return cur.fetchall()

    def viewBatchStudent(self, bid):
        cur1 = mydb.cursor()
        cur1.execute('SELECT * FROM student WHERE batch_id=%s', (bid,))
        return cur1.fetchall()

    def viewAllStudent(self):
        cur.execute('SELECT * FROM student')
        return cur.fetchall()

    def createStudentLogin(self, sid, uname, passw):
        cur.execute('INSERT INTO studentLogin VALUES(%s,%s,%s)', (sid, uname, passw))
        mydb.commit()
        return cur.rowcount
    
    def updatePassword(self,sid,spass):
        cur.execute('UPDATE studentlogin SET password=%s WHERE s_id=%s',(spass,sid))
        mydb.commit()
        return cur.rowcount


class Teacher:

    def __init__(self):
        self.t_id = ''
        self.fname = ''
        self.lname = ''
        self.gender = ''
        self.DOB = ''
        self.address = ''
        self.email = ''
        self.mobile = ''

    def addTeacher(self, tid, tfname, tlname, gen, dob, addr, email, mob):
        self.t_id = tid
        self.fname = tfname
        self.lname = tlname
        self.gender = gen
        self.DOB = dob
        self.address = addr
        self.email = email
        self.mobile = mob
        sql = "INSERT INTO teacher VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.t_id, self.fname, self.lname, self.gender, self.DOB, self.address, self.email, self.mobile)
        cur.execute(sql, val)
        mydb.commit()
        return cur.rowcount

    def searchTeacher(self, tid):
        cur.execute('SELECT * FROM teacher WHERE t_id = %s', (tid,))
        return cur.fetchone()

    def updateTeacherDetails(self, upd, tid, mydata):
        if upd == '1':
            cur.execute('UPDATE teacher SET fname = %s WHERE t_id = %s', (mydata, tid))
            mydb.commit()
            return cur.rowcount
        elif upd == '2':
            cur.execute('UPDATE teacher SET lname = %s WHERE t_id = %s', (mydata, tid))
            mydb.commit()
            return cur.rowcount
        elif upd == '3':
            cur.execute('UPDATE teacher SET address = %s WHERE t_id = %s', (mydata, tid))
            mydb.commit()
            return cur.rowcount
        else:
            cur.execute('UPDATE teacher SET mobile = %s WHERE t_id = %s', (mydata, tid))
            mydb.commit()
            return cur.rowcount

    def removeTeacher(self, tid):
        cur.execute('DELETE FROM teacher WHERE t_id = %s', (tid,))
        mydb.commit()
        return cur.rowcount

    def viewTeacher(self):
        cur.execute('select * from teacher')
        return cur.fetchall()

    def createTeacherLogin(self, tid, uname, passw):
        cur.execute('INSERT INTO teacherLogin VALUES(%s,%s,%s)', (tid, uname, passw))
        mydb.commit()
        return cur.rowcount
    
    def updatePassword(self,tid,tpass):
        cur.execute('UPDATE teacherlogin SET password=%s WHERE t_id=%s',(tpass,tid))
        mydb.commit()
        return cur.rowcount


class Course:

    def __init__(self):
        self.course_id = None
        self.course_name = None

    def addCourse(self, cid, cname):
        cur.execute('INSERT INTO course VALUES (%s,%s)', (cid, cname))
        mydb.commit()
        return cur.rowcount

    def viewCourse(self):
        cur.execute('select * from course')
        return cur.fetchall()


class Batch:

    def __init__(self):
        self.batch_id = ''
        self.start_date = ''
        self.end_date = ''

    def addBatch(self, bid, sd, ed, cid, tid):
        self.batch_id = bid
        self.start_date = sd
        self.end_date = ed
        cur.execute("INSERT INTO batch VALUES (%s,%s,%s,%s,%s)", (bid, sd, ed, cid, tid))
        mydb.commit()
        return cur.rowcount

    def viewBatch(self):
        cur.execute('select * from batch')
        return cur.fetchall()

    def viewCourseBatch(self, cid):
        cur.execute("SELECT * FROM batch WHERE course_id=%s", (cid,))
        availableBatch = cur.fetchall()
        return availableBatch

    def searchTeacherBatch(self, tid):
        cur.execute('SELECT * FROM batch WHERE t_id=%s', (tid,))
        print(cur.rowcount)
        return cur.fetchall()


class Attendence:

    def __init__(self):
        self.date = ''
        self.attend = ''

    def markAttendence(self, sid, bid, today, attend):
        cur.execute('INSERT INTO attendence VALUES(%s,%s,%s,%s)', (sid, bid, today, attend))
        mydb.commit()
        return cur.rowcount

    def viewStudentAttendence(self,sid):
        cur.execute('SELECT * FROM attendence WHERE s_id=%s',(sid,))
        return cur.fetchall()

    def viewBatchAttendence(self, bid):
        cur.execute('SELECT * FROM attendence WHERE batch_id=%s', (bid,))
        return cur.fetchall()