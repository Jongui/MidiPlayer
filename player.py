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

    def play_major_scale(self, note, inst, dynamic, channel):
        pygame.init()
        pygame.midi.init()
        port = 2
        time = 0.5
        self.midiOutput = pygame.midi.Output(port, channel)
        self.midiOutput.set_instrument(inst)
        note1 = note + 2
        note2 = note + 4
        note3 = note + 5
        note4 = note + 7
        note5 = note + 9
        note6 = note + 11
        note7 = note + 12
        self.midiOutput.note_on(note,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note,dynamic,channel)
        self.midiOutput.note_on(note1,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note1,dynamic,channel)
        self.midiOutput.note_on(note2,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note2,dynamic,channel)
        self.midiOutput.note_on(note3,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note3,dynamic,channel)
        self.midiOutput.note_on(note4,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note4,dynamic,channel)
        self.midiOutput.note_on(note5,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note5,dynamic,channel)
        self.midiOutput.note_on(note6,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note6,dynamic,channel)
        self.midiOutput.note_on(note7,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note7,dynamic,channel)
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

    def play_instrument_1(self, inst, midiOutput):
        tempo = 0.5
        for x in range(0, 3):
            note = 79
            time = tempo
            dynamic = 127
            midiOutput.set_instrument(inst)
            midiOutput.note_on(note,dynamic,0)
            sleep(time)
            midiOutput.note_off(note,dynamic,0)
            note = 76
            time = tempo
            midiOutput.note_on(note,dynamic,0)
            sleep(time)
            midiOutput.note_off(note,dynamic,0)
            note = 79
            time = tempo / 2
            midiOutput.note_on(note,dynamic,0)
            sleep(time)
            midiOutput.note_off(note,dynamic,0)
            note = 79
            time = tempo / 2
            midiOutput.note_on(note,dynamic,0)
            sleep(time)
            midiOutput.note_off(note,dynamic,0)
            note = 76
            time = tempo
            midiOutput.note_on(note,dynamic,0)
            sleep(time)
            midiOutput.note_off(note,dynamic,0)
        del midiOutput
        pygame.midi.quit()
    
    def play_instrument_2(self, inst, midiOutput):
        channel = 1
        tempo = 0.5
        for x in range(0, 3):
            note = 60
            note2 = 67
            time = tempo * 2
            dynamic = 110
            midiOutput.set_instrument(inst, channel)
            midiOutput.note_on(note,dynamic,channel)
            midiOutput.note_on(note2,dynamic,channel)
            sleep(time)
            midiOutput.note_off(note,dynamic,channel)
            midiOutput.note_off(note2,dynamic,channel)
            note = 67
            note2 = 74
            time = tempo
            midiOutput.note_on(note,dynamic,channel)
            midiOutput.note_on(note2,dynamic,channel)
            sleep(time)
            midiOutput.note_off(note,dynamic,channel)
            midiOutput.note_off(note2,dynamic,channel)
            note = 60
            note2 = 67
            time = tempo
            midiOutput.note_on(note,dynamic,channel)
            midiOutput.note_on(note2,dynamic,channel)
            sleep(time)
            midiOutput.note_off(note,dynamic,channel)
            midiOutput.note_off(note2,dynamic,channel)
        del midiOutput
        pygame.midi.quit()
    
    def play_instrument_3(self, inst, midiOutput):
        channel = 2
        tempo = 0.5
        for x in range(0, 3):
            note = 36
            dynamic = 110
            time = tempo
            midiOutput.set_instrument(inst, channel)
            midiOutput.note_on(note,dynamic,channel)
            sleep(time)
            midiOutput.note_off(note,dynamic,channel)
            note = 40
            time = tempo
            midiOutput.note_on(note,dynamic,channel)
            sleep(time)
            midiOutput.note_off(note,dynamic,channel)
            note = 43
            time = tempo
            midiOutput.note_on(note,dynamic,channel)
            sleep(time)
            midiOutput.note_off(note,dynamic,channel)
            note = 40
            time = tempo
            midiOutput.note_on(note,dynamic,channel)
            sleep(time)
            midiOutput.note_off(note,dynamic,channel)
        
        del midiOutput
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
        
        return "Terminou"
        '''thread.start_new_thread( self.play_instrument_1, (10, midiOutput, ) )
        thread.start_new_thread( self.play_instrument_2, (14, midiOutput, ) )
        thread.start_new_thread( self.play_instrument_3, (36, midiOutput, ) )'''

    def play_instrument(self, inst, notes, channel, midiOutput):
        dynamic = 120
        midiOutput.set_instrument(inst, channel)
        for note in notes:
            midiOutput.note_on(note["note"],dynamic,channel)
            sleep(note["time"])
            midiOutput.note_off(note["note"],dynamic,channel)


class Player1(object):
    def __init__(self):
        self.stop = False;

    def set_inst(self, inst):
        self.inst = inst;

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
            print("NoteOf: " + str(inst))
        else:
            arpMajorChord(self, note, 1, channel);

    def arpMajorChord(self, note, time, channel, dynamic):
        note1 = note + 4
        note2 = note + 7
        note3 = note + 12
        bass = note - 12
        bass5 = bass - 5
        self.midiOutput.note_on(bass,dynamic,channel)
        self.midiOutput.note_on(note,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note,dynamic,channel)
        self.midiOutput.note_on(note1,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note1,dynamic,channel)
        self.midiOutput.note_off(bass,dynamic,channel)
        self.midiOutput.note_on(bass5,dynamic,channel)
        self.midiOutput.note_on(note2,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note2,dynamic,channel)
        self.midiOutput.note_on(note3,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note3,dynamic,channel)
        self.midiOutput.note_off(bass5,dynamic,channel)
    
    def play_major_scale(note, inst, dynamic, channel):
        note1 = note + 2
        note2 = note + 4
        note3 = note + 5
        note4 = note + 7
        note5 = note + 9
        note6 = note + 11
        note7 = note + 12
        self.midiOutput.note_on(note,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note,dynamic,channel)
        self.midiOutput.note_on(note1,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note1,dynamic,channel)
        self.midiOutput.note_on(note2,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note2,dynamic,channel)
        self.midiOutput.note_on(note3,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note3,dynamic,channel)
        self.midiOutput.note_on(note4,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note4,dynamic,channel)
        self.midiOutput.note_on(note5,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note5,dynamic,channel)
        self.midiOutput.note_on(note6,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note6,dynamic,channel)
        self.midiOutput.note_on(note7,dynamic,channel)
        sleep(time)
        self.midiOutput.note_off(note7,dynamic,channel)


    def change_all(self, note, time, channel, dynamic, inst):
        self.note = note
        self.dynamic = dynamic
        self.time = time
        self.inst = inst;

    def start_arpegio(self, note, time, channel, dynamic):
        self.stop = False
        self.note = note
        self.dynamic = dynamic
        self.time = time
        pygame.init()
        pygame.midi.init()
        port = 2
        self.midiOutput = pygame.midi.Output(port, channel)
        self.midiOutput.set_instrument(self.inst)
        while self.stop==False:
            print("Instrument: " + str(self.inst))
            self.arpMajorChord(self.note, self.time, channel, self.dynamic,)
        del self.midiOutput
        pygame.midi.quit()

    def stop_arpegio(self):
        print("Stop Arpegio")
        self.stop = True

    def change_inst(self, inst):
        self.inst = inst;
        self.midiOutput.set_instrument(self.inst)

    def change_note(self, note):
        self.note = note;
    
    def change_dynamic(self, dynamic):
        self.dynamic = dynamic

    def change_time(self, time):
        self.time = time
