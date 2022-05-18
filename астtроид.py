import random, math
from superwires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)
class Wrapper(games.Sprite):
    def update(self):
        if self.bottom < 0:
            self.top = games.screen.height
        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        self.destroy()


class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(explosion)
        self.destroy()


class Explosion(games.Animation):
    sound = games.load_sound('explosion.wav')
    explosion_files = ['explosion1.bmp', 'explosion2.bmp', 'explosion3.bmp',
                       'explosion4.bmp', 'explosion5.bmp', 'explosion6.bmp',
                       'explosion7.bmp', 'explosion8.bmp', 'explosion9.bmp']

    def __init__(self, x, y):
        super(Explosion, self).__init__(images=Explosion.explosion_files, x=x, y=y,
                                        repeat_interval=4, n_repeats=1, is_collideable=False)


class Asteroid(Wrapper):
    SMALL=1
    MEDIUM=2
    LARGE=3
    POINTS=30
    total=0
    images={SMALL:games.load_image('asteroid_small.bmp'),
            MEDIUM:games.load_image('asteroid_med.bmp'),
            LARGE:games.load_image('asteroid_big.bmp')}
    SPEED=3
    SPAWN=2
    def __init__(self, x, y, size, game):
        Asteroid.total+=1
        self.game=game
        super(Asteroid, self).__init__(image=Asteroid.images[size], x=x, y=y,
                                       dx=random.choice([1, -1])*Asteroid.SPEED*random.random()/size,
                                       dy=random.choice([1, -1])*Asteroid.SPEED*random.random()/size)
        self.size=size
    def die(self):
        Asteroid.total-=1
        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10
        if self.size!=Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid=Asteroid(x=self.x, y=self.y, size=self.size-1, game=self.game)
                games.screen.add(new_asteroid)
        if Asteroid.total==0:
            self.game.advance()
        super(Asteroid, self).die()
class Ship(Collider):
    ship_image = games.load_image('ship.bmp')
    ROTATION_STEP=3
    SPEED=0.07
    sound = games.load_sound('thrust.wav')
    DELAY=25
    VELOCITY_MAX = 3

    def __init__(self, x, y, game):
        super(Ship, self).__init__(image=Ship.ship_image, x=x , y=y)
        self.missile_wait=0
        self.game=game
    def update(self):
        if self.missile_wait > 0:
            self.missile_wait-=1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle-=Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle+=Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
            angle=self.angle*math.pi/180
            self.dx+=Ship.SPEED*math.sin(angle)
            self.dy+=Ship.SPEED*-math.cos(angle)
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait==0:
            missile=Missile(ship_x=self.x, ship_y=self.y, ship_angle=self.angle)
            games.screen.add(missile)
            self.missile_wait=Ship.DELAY
        super(Ship, self).update()
    def die(self):
        self.game.end()
        super(Ship, self).die()

class Missile(Collider):
    image=games.load_image('missile.bmp')
    sound = games.load_sound('missile.wav')
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        Missile.sound.play()
        angle=ship_angle*math.pi/180
        x=ship_x+Missile.BUFFER*math.sin(angle)
        y=ship_y+Missile.BUFFER*-math.cos(angle)
        dx=Missile.VELOCITY_FACTOR*math.sin(angle)
        dy=Missile.VELOCITY_FACTOR*-math.cos(angle)
        super(Missile, self).__init__(image=Missile.image, x=x, y=y, dx=dx, dy=dy)
        self.lifetime=Missile.LIFETIME

    def update(self):
        self.lifetime-=1
        if self.lifetime==0:
            self.destroy()
        super(Missile, self).update()
class Game(object):
    def __init__(self):
        self.level=0
        self.sound=games.load_sound('level.wav')
        self.score=games.Text(value=0, size=30, color=color.red, top=5,
                              right=games.screen.width-10, is_collideable=False)
        games.screen.add(self.score)
        self.ship = Ship(x=games.screen.width / 2,
                        y=games.screen.height / 2,
                        game=self)
        games.screen.add(self.ship)
    def play(self):
        games.music.load('theme.mid')
        games.music.play(-1)
        image = games.load_image('nebula.jpg', transparent=False)
        games.screen.background = image
        self.advance()
        games.screen.mainloop()
    def advance(self):
        self.level+=1
        BUFFER=150
        for i in range(self.level):
            x_min=random.randrange(BUFFER)
            y_min=BUFFER-x_min
            x=self.ship.x+random.randrange(x_min, games.screen.width-x_min)
            y=self.ship.y+random.randrange(y_min, games.screen.height-y_min)
            x%=games.screen.width
            y%=games.screen.height
            asteroid = Asteroid(x=x, y=y, size=Asteroid.LARGE, game=self)
            games.screen.add(asteroid)

        message=games.Message(value='Уровень '+str(self.level),size=40,color=color.black,
                              x=games.screen.width/2, y=games.screen.height/10,
                              lifetime=3*games.screen.fps, is_collideable=False)
        games.screen.add(message)
        if self.level > 1:
            self.sound.play()
    def end(self):
        message=games.Message(value='Game Over', size=90, color=color.red,
                              x=games.screen.width/2, y=games.screen.height/2,
                              lifetime=5*games.screen.fps, is_collideable=False,
                              after_death=games.screen.quit)
        games.screen.add(message)

def main():
    astrocrash=Game()
    astrocrash.play()
main()