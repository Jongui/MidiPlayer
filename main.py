import pygame
import pygame.midi
import web
import sys
import thread
import player
import students
import classes
import tasks
import metronome

from time import sleep

urls = (
    '/', 'index',
    '/playScript', 'playScript',
    '/majorscale', 'majorscale',
    '/login', 'login',
    '/createUser', 'createUser',
    '/studentCourses', 'studentCourses',
    '/coursClasses', 'coursClasses',
    '/classesTasks', 'classesTasks',
    '/loadTaskInfo', 'loadTaskInfo',
    '/handleMetronome', 'handleMetronome',
    '/sendAnswer', 'sendAnswer',
    '/playTask', 'playTask'
)

class index:
    def GET(self):
        user_data = web.input()
        time = float(user_data.time)
        note = int(user_data.note)
        inst = int(user_data.inst)
        channel = int(user_data.channel)
        action = int(user_data.action)
        dynamic = int(user_data.dynamic)
        pl = player.Player();
        thread.start_new_thread( pl.play, (note, channel, action, inst, dynamic,) )

class playScript:
    def GET(self):
        user_data = web.input()
        time = float(user_data.time)
        note = int(user_data.note)
        inst = int(user_data.inst)
        channel = int(user_data.channel)
        dynamic = int(user_data.dynamic)
        pl = player.Player();
        pl.playScriptNote(note, channel, inst, dynamic, time)


class majorscale:
    def GET(self):
        user_data = web.input()
        note = int(user_data.note)
        inst = int(user_data.inst)
        dynamic = int(user_data.dynamic)
        channel = 0
        pl = Player()
        thread.start_new_thread( pl.play_major_scale, (note, inst, dynamic, channel,) )

class login:
    def GET(self):
        user_data = web.input()
        id_student = user_data.idStudent;
        password = user_data.password;
        student_dao = students.StudentDAO();
        return student_dao.loginUser(id_student, password)

class createUser:
    def GET(self):
        user_data = web.input()
        id_student = user_data.idStudent
        name = user_data.name
        email = user_data.email
        password = user_data.password
        student_dao = students.StudentDAO();
        student_dao.createUser(id_student, name, email, password)

class studentCourses:
    def GET(self):
        user_data = web.input()
        id_student = user_data.idStudent
        student_dao = students.StudentDAO()
        return student_dao.student_courses(id_student)

class coursClasses:
    def GET(self):
        user_data = web.input()
        id_cours = user_data.idCours
        classes_dao = classes.ClassesDAO()
        return classes_dao.cours_classes(id_cours)

class classesTasks:
    def GET(self):
        user_data = web.input()
        id_classes = user_data.idClasses
        id_cours = user_data.idCours
        tasks_dao = tasks.TasksDAO();
        return tasks_dao.classes_tasks(id_classes, id_cours)

class loadTaskInfo:
    def GET(self):
        user_data = web.input()
        id_cours = user_data.idCours
        id_classes = user_data.idClasses
        id_task = user_data.idTask
        tasks_dao = tasks.TasksDAO();
        return tasks_dao.task_info(id_cours, id_classes, id_task);

class handleMetronome:
    def GET(self):
        user_data = web.input()
        tack = float(user_data.tack)
        action = int(user_data.action)
        metr = metronome.Metronome(tack)
        if action == 0:
            thread.start_new_thread( metr.instance.start_metronome, (tack,))
        else:
            metr.instance.stop_metronome()

class sendAnswer:
    def GET(self):
        user_data = web.input()
        id_cours = user_data.idCours
        id_classes = user_data.idClasses
        id_task = user_data.idTask
        id_student = user_data.idStudent
        answer = user_data.answer
        student_dao = students.StudentDAO()
        return student_dao.save_answer(id_cours, id_classes, id_task, id_student, answer)

class playTask:
    def GET(self):
        user_data = web.input()
        file_name = user_data.fileName
        pl = player.Player()
        return pl.play_task(file_name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
