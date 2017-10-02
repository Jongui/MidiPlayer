
import player
import pygame
import pygame.midi
import web
import sys
import thread

from time import sleep

urls = (
    '/', 'arpegio'
	
)
pl = player.Player();

class arpegio:
    def GET(self):
        #?time=1&note=60&inst=20&dynamic=127
        user_data = web.input()
        time = float(user_data.time)
        note = int(user_data.note)
        inst = int(user_data.inst)
        pl.set_inst(inst,)
        channel = int(user_data.channel)
        action = int(user_data.action)
        dynamic = int(user_data.dynamic)
        if action == 0:
            first = False
            thread.start_new_thread( pl.start_arpegio, (note, time, channel, dynamic,) )
        elif action == 1:
            pl.stop_arpegio()
        elif action == 2:
            pl.change_all(note, time, channel, dynamic, inst,)
        #    pl.change_inst(inst)
        #elif action == 3:
        #    pl.change_note(note)
        #elif action == 4:
        #    pl.change_dynamic(dynamic)
        #elif action == 5:
        #    pl.change_time(time)
        #else:
            

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()