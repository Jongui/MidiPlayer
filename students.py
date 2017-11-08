import MySQLdb
import json
import courses
import resource

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

    def loginUser(self, user_name, password, locale):
        db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
        curs = db.cursor()
        sql = "SELECT * FROM Students WHERE idStudents=%s" % (user_name)
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
            message = resource.loadResourceData(locale, "userConnected")
            output = '{"status":"0", "message":' + '"' + message + '"' + ', "Student":' + student.to_json() + '}'
        else:
            message = resource.loadResourceData(locale, "userNotConnected")
            output = '{"status":"1", "message":' + '"' + message + '"}'
            #json.dumps({"status":"1", "message":"Password or User name fail"})
        return output

    def createUser(self, idStudent, name, email, password):
        try:
            db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
            curs = db.cursor()
            sql = "insert into Students VALUES('%s', '%s', '%s', '%s')" % (idStudent, name, email, password,)
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

    def save_answer(self, id_cours, id_classes, id_task, id_student, answer, locale):
        try:
            file_name = "Answers/" + id_student + str(id_cours) + str(id_classes) + str(id_task)
            file= open(file_name,"w+")
            file.write(answer)
            message = resource.loadResourceData(locale, "answerSaved")
            output = json.dumps({"status": "0", "message": message})
        except MySQLdb.Error as err:
            print("Something went wrong: {}". format(err))
            output = json.dumps({"status": "1", "message":str(err)})
        return output

    def student_answer(self, id_student, id_cours, id_classes, id_task):
        file_name = "Answers/" + id_student + str(id_cours) + str(id_classes) + str(id_task)
        file= open(file_name,"r")
        if file.mode == "r":
            return file.read()
