import MySQLdb
import json
import courses

class Student:
    def __init__(self, idStudent, name):
        self.idStudent = idStudent
        self.name = name

    def __init__(self, idStudent, name, email, password):
        self.idStudent = idStudent
        self.name = name
        self.email = email
        self.password = password

    def to_json(self):
        ret = json.dumps({"idStudent":self.idStudent, "name": self.name, "email":self.email, "password":self.password})
        return ret

class StudentDAO:
    def __init__(self):
        db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")

    def loginUser(self, user_name, password):
        db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
        curs = db.cursor()
        sql = "SELECT * FROM Students WHERE idStudents=%s" % (user_name)
        print(sql)
        curs.execute ("SELECT * FROM Students WHERE idStudents=%s", user_name,)
        db.close()
        output = ""
        sucess = False;
        for reading in curs.fetchall():
            student = Student(reading[0], reading[1], reading[2], reading[3])
            db_password = str(reading[3]);
            if db_password == password:
                sucess = True
            else:
                sucess = False;
        if sucess == True:
            output = '{"status":"0", "message":"User connected", "Student":' + student.to_json() + '}'
        else:
            output = json.dumps({"status":"1", "message":"Password or User name fail"})
        print str(output)
        return output

    def createUser(self, idStudent, name, email, password):
        try:
            db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
            curs = db.cursor()
            sql = "insert into Students VALUES('%s', '%s', '%s', '%s')" % (idStudent, name, email, password,)
            print("Comando SQL: " + sql)
            curs.execute (sql)
            db.commit()
            db.close()
            output = json.dumps({"status":"0", "message":"User successfully created"})
        except MySQLdb.Error as err:
            print("Something went wrong: {}".format(err))
            output = json.dumps({"status":"1", "message":err.msg})

    def student_courses(self, id_student):
        try:
            coursesDAO = courses.CoursesDAO()
            coursesArray = []
            db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
            curs = db.cursor()
            sql = "SELECT idCourses FROM Students_Courses WHERE idStudents='%s'" % (id_student,)
            print("Comando SQL: " + sql)
            curs.execute (sql)
            db.commit()
            db.close()
            for reading in curs.fetchall():
                coursesArray.append(reading[0])
            output = coursesDAO.find_user_courses(coursesArray)
        
        except MySQLdb.Error as err:
            print("Something went wrong: {}".format(err))
            output = json.dumps({"status":"1", "message":str(err)})

        return output

    def save_answer(self, id_cours, id_classes, id_task, id_student, answer):
        try:
            file_name = id_student + str(id_cours) + str(id_classes) + str(id_task)
            file= open(file_name,"w+")
            file.write(answer)
            output = json.dumps({"status": "0", "message": "File saved"})
        except MySQLdb.Error as err:
            print("Something went wrong: {}". format(err))
            output = json.dumps({"status": "1", "message":str(err)})
        return output


