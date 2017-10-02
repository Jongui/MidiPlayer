import pygame
import pygame.midi

from time import sleep

class Metronome:
    class __Metronome:
        def __init__(self, tack):
            self.tack = tack
            self.stop = False

        def start_metronome(self, tack):
            pygame.init()
            pygame.midi.init()
            port = 2
            channel = 0
            self.midiOutput = pygame.midi.Output(port, channel)
            self.midiOutput.set_instrument(13)
            while self.stop==False:
                self.midiOutput.note_on(72,120,channel)
                sleep(tack)
                self.midiOutput.note_off(72,120,channel)
                self.midiOutput.note_on(72,80,channel)
                sleep(tack)
                self.midiOutput.note_off(72,80,channel)
            self.stop = False
            del self.midiOutput
            pygame.midi.quit()

        def stop_metronome(self):
            self.stop = True

    instance = None

    def __init__(self, tack):
        if not Metronome.instance:
            Metronome.instance = Metronome.__Metronome(tack)
        else:
            Metronome.instance.tack = tack
