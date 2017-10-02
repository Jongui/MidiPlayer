import pygame
import pygame.midi
import sys

from time import sleep

def majorChord(note, output, time, channel):
    note1 = note + 4
    note2 = note + 7
    output.note_on(note,127,channel)
    output.note_on(note1,127,channel)
    output.note_on(note2,127,channel)
    sleep(time)
    output.note_off(note,127,channel)
    output.note_off(note1,127,channel)
    output.note_off(note2,127,channel)

def arpMajorChord(note, output, time, channel):
    note1 = note + 4
    note2 = note + 7
    note3 = note + 12
    bass = note - 12
    bass5 = bass - 5
    output.note_on(bass,127,channel)
    output.note_on(note,127,channel)
    sleep(time)
    output.note_off(note,127,channel)
    output.note_on(note1,127,channel)
    sleep(time)
    output.note_off(note1,127,channel)
    output.note_off(bass,127,channel)
    output.note_on(bass5,127,channel)
    output.note_on(note2,127,channel)
    sleep(time)
    output.note_off(note2,127,channel)
    output.note_on(note3,127,channel)
    sleep(time)
    output.note_off(note3,127,channel)
    output.note_off(bass5,127,channel)
    
def dominantCadence(note, time, inst, channel,times):
    pygame.init()
    pygame.midi.init()
    for id in range(pygame.midi.get_count()):
        print(pygame.midi.get_device_info(id))
    port = 2
    midiOutput = pygame.midi.Output(port, 0)
    midiOutput.set_instrument(inst)
        
    note1 = note + 5
    note2 = note + 7
    while times != 0:
        arpMajorChord(note, midiOutput, time, channel)
        arpMajorChord(note1, midiOutput, time, channel)
        arpMajorChord(note2, midiOutput, time, channel)
        arpMajorChord(note, midiOutput, time, channel)
        times = times - 1
    del midiOutput
    pygame.midi.quit()

def play_single_note(note, time, inst, channel):
    pygame.init()
    pygame.midi.init()
    for id in range(pygame.midi.get_count()):
        print(pygame.midi.get_device_info(id))
    port = 2
    midiOutput = pygame.midi.Output(port, 0)
    midiOutput.set_instrument(inst)
    midiOutput.note_on(note,127,channel)
    sleep(time)
    midiOutput.note_off(note,127,channel)
    del midiOutput
    pygame.midi.quit()