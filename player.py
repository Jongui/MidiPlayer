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
        self.midiOutput = pygame.midi.Output(port, channel)
        self.midiOutput.set_instrument(inst)
        if action == 0:
            self.midiOutput.note_on(note,dynamic,channel)
        elif action == 1:
            self.midiOutput.note_off(note,dynamic,channel)
            del self.midiOutput
            pygame.midi.quit()

    def playScriptNote(self, note, channel, inst, dynamic, time):
        print("Note: " + str(note) + " Channel: " + str(channel) + " Inst: " + str(inst) + " Dynamic: " + str(dynamic) + " Time: " + str(time))
        pygame.init()
        pygame.midi.init()
        port = 2
        self.midiOutput = pygame.midi.Output(port, channel)
        self.midiOutput.set_instrument(inst)
        self.midiOutput.note_on(note,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note,dynamic,channel)
        del self.midiOutput
        pygame.midi.quit()

    def play_task(self, file_name):
        file = open(file_name, "r")
        if file.mode == "r":
            ret = file.read()
            data = json.loads(ret)
        
        port = 2
        pygame.init()
        pygame.midi.init()
        midiOutput = pygame.midi.Output(port, 0)
        channel = 0;
        inst_code = 10
        for lines in data["lines"]:
            notes = lines["notes"]
            instr = lines["inst"]
            thread.start_new_thread( self.play_instrument, (inst_code, notes, channel, midiOutput, ) )
            channel = channel + 1
            inst_code = 14

    def play_instrument(self, inst, notes, channel, midiOutput):
        dynamic = 120
        midiOutput.set_instrument(inst, channel)
        for note in notes:
            midiOutput.note_on(note["note"],dynamic,channel)
            sleep(note["time"])
            midiOutput.note_off(note["note"],dynamic,channel)
