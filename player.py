import pygame
import pygame.midi
import thread
import json

from time import sleep

class Player(object):
    
    def __init__(self):
        self.stop = False;
    
    def play(self, note, channel, action, inst, dynamic):
        pygame.init()
        pygame.midi.init()
        port = 2
        midiOutput = pygame.midi.Output(port, channel)
        midiOutput.set_instrument(inst, channel)
        if action == 0:
            midiOutput.note_on(note,dynamic,channel)
        elif action == 1:
            midiOutput.note_off(note,dynamic,channel)
            del midiOutput
            pygame.midi.quit()

    def playScriptNote(self, note, channel, inst, dynamic, time):
        pygame.init()
        pygame.midi.init()
        port = 2
        midiOutput = pygame.midi.Output(port, channel)
        midiOutput.set_instrument(inst, channel)
        midiOutput.note_on(note,dynamic,channel)
        sleep(time)
        midiOutput.note_off(note,dynamic,channel)
        del midiOutput
        pygame.midi.quit()

    def play_task(self, file_name):
        local_name = "Activities/" + file_name
        file = open(local_name, "r")
        if file.mode == "r":
            ret = file.read()
            data = json.loads(ret)
        port = 2
        pygame.init()
        pygame.midi.init()
        midiOutput = pygame.midi.Output(port, 0)
        channel = 0;
        for lines in data["lines"]:
            notes = lines["notes"]
            instr = lines["inst"]
            thread.start_new_thread( self.play_instrument, (instr["code"], notes, channel, midiOutput, ) )
            channel = channel + 1
        return str(ret)
    
    def play_instrument(self, inst, notes, channel, midiOutput):
        midiOutput.set_instrument(inst, channel)
        for note in notes:
            dynamic = note["dynamic"]
            midiOutput.note_on(note["note"],dynamic,channel)
            sleep(note["time"])
            midiOutput.note_off(note["note"],dynamic,channel)
