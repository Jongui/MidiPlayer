import MySQLdb
import json

class Classes:
    def __init__(self, idCourses, idClasses, date):
        self.idCourses = idCourses
        self.idClasses = idClasses
        self.date = date

    def to_json(self):
        ret = json.dumps({"idCourses":self.idCourses, "idClasses": self.idClasses, "date":self.date.strftime('%Y-%m-%d')})
        return ret

class ClassesDAO:
    def cours_classes(self, id_cours):
        output = '{"Classes":['
        db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
        curs = db.cursor()
        curs.execute("SELECT * FROM Classes WHERE idCourses=%s", id_cours,)
        print("SELECT * FROM Classes WHERE idCourses=%s".format(id_cours))
        for reading in curs.fetchall():
            classes = Classes(reading[0], reading[1], reading[2])
            output += classes.to_json() + ","
        db.close();
        output = output[:-1]
        output += "]}"
        return output
