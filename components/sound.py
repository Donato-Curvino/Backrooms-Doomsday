import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'assets/sound/'
        self.running = pg.mixer.Sound(self.path + 'running-on-the-road-6220.mp3')
        self.jump = pg.mixer.Sound(self.path + 'Piano_crescendo.wav')
        self.chased = pg.mixer.Sound(self.path + 'creeping-horror-73989.mp3')
        self.ambient = pg.mixer.Sound(self.path + 'walkandgrunt.mp3')