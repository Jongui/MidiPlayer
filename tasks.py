import MySQLdb
import json

class Tasks:
    def __init__(self, idCourses, idClasses, idTasks, name, description, keyboard, participants):
        self.idClasses = idClasses
        self.idTasks = idTasks
        self.name = name
        self.description = description
        self.keyboard = keyboard
        self.participants = participants
        self.idCourses = idCourses
    
    def to_json(self):
        ret = json.dumps({"idCourses":self.idCourses, "idClasses":self.idClasses, "idTasks": self.idTasks, "name":self.name, "description":self.description, "keyboard":self.keyboard, "participants":self.participants})
        return ret

class TasksDAO:
    def classes_tasks(self, id_classes, id_cours):
        output = '{"Tasks":['
        db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
        curs = db.cursor()
        curs.execute("SELECT * FROM Tasks WHERE idClasses=%s AND idCourses=%s", (id_classes, id_cours))
        sql = "SELECT * FROM Tasks WHERE idClasses=%s AND idCourses=%s" % (id_classes, id_cours)
        print(sql)
        for reading in curs.fetchall():
            task = Tasks(reading[0], reading[1], reading[2], reading[3], reading[4], reading[5], reading[6])
            output += task.to_json() + ","
        db.close()
        if output[-1:] == ",":
            output = output[:-1]
        output += "]}"
        return output

    def task_info(self, id_cours, id_classes, id_task):
        db = MySQLdb.connect("localhost", "MusicPlayerUser", "PlayNice", "MusicClasses")
        curs = db.cursor()
        curs.execute("SELECT file FROM Tasks WHERE idCourses=%s AND idClasses=%s AND idTasks=%s ", (id_cours, id_classes, id_task))
        for reading in curs.fetchall():
            file_name = reading[0]
        db.close()
        file = open(file_name, "r")
        if file.mode == "r":
            return file.read()
