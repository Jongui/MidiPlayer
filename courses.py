import MySQLdb
import json

class Courses:
    def __init__(self, idCourses, coursName, initDate, endDate, creationDate, hours):
        self.idCourses = idCourses
        self.coursName = coursName
        self.initDate = initDate
        self.endDate = endDate
        self.creationDate = creationDate
        self.hours = hours

    def to_json(self):
        ret = json.dumps({"idCourses":self.idCourses, "coursName": self.coursName, "initDate":self.initDate.strftime('%Y-%m-%d'), "endDate":self.endDate.strftime('%Y-%m-%d'), "creationDate":self.creationDate.strftime('%Y-%m-%d'), "hours":self.hours})
        return ret

class CoursesDAO:
    def find_user_courses(self, courses):
        output = '{"Courses":['
        db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
        curs = db.cursor()
        for idCourses in courses:
            curs.execute ("SELECT * FROM Courses WHERE idCourses=%s", idCourses,)
            for reading in curs.fetchall():
                cours = Courses(reading[0], reading[1], reading[2], reading[3], reading[4], reading[5])
                output += cours.to_json() + ","
        db.close()
        output = output[:-1]
        output += "]}"
        return output

